
#!/usr/bin/env bash
set -euo pipefail

# ---------- CONFIG ----------
# add account info in .env (see azure-credentials.env.example)
if [ ! -f "./infra/cli/azure_credentials.env" ]; then
  echo "! azure_credentials.env not found. Please copy azure_credentials.example.env and fill it in." >&2
  exit 1
fi

# shellcheck source=/dev/null
source ./infra/cli/azure_credentials.env

SUBSCRIPTION="${SUBSCRIPTION:-}"
RG="${RG:-rg-shep-dev}"
LOC="${LOC:-westeurope}"

# Prefer explicit SA from env, otherwise fall back to preferred name
SA="${SA:-stshepdev}"

ADF="${ADF:-adf-shep-dev}"
# ----------------------------

if [ -z "$SUBSCRIPTION" ]; then
  echo "! SUBSCRIPTION is not set in infra/cli/azure-credentials.env" >&2
  exit 1
fi

echo "Using subscription: $SUBSCRIPTION"
echo "Resource group:     $RG"
echo "Location:           $LOC"
echo "Storage account:    $SA"
echo "Data Factory:       $ADF"
echo

az account set --subscription "$SUBSCRIPTION"

az config set extension.use_dynamic_install=yes_without_prompt >/dev/null
az config set extension.dynamic_install_allow_preview=true >/dev/null

# Resource group
echo "Creating resource group (if not existing)..."
az group create -n "$RG" -l "$LOC" >/dev/null

# Storage account
echo "Creating ADLS Gen2 storage account (if not existing)..."
az storage account create -n "$SA" -g "$RG" -l "$LOC" \
  --sku Standard_LRS --kind StorageV2 --hns true >/dev/null

ACCOUNT_KEY=$(az storage account keys list \
  --account-name "$SA" \
  --resource-group "$RG" \
  --query "[0].value" -o tsv)

# Containers
echo "Creating lake containers (raw, silver, gold)..."
for c in raw silver gold; do
  az storage container create \
    --account-name "$SA" \
    --account-key "$ACCOUNT_KEY" \
    --name "$c" >/dev/null
done

# Data Factory with managed identity
echo "Creating Data Factory (with managed identity)..."
az datafactory create -g "$RG" -n "$ADF" -l "$LOC" >/dev/null

echo "Fetching ADF managed identity principalId..."
ADF_MI_PRINCIPAL_ID=$(az datafactory show -g "$RG" -n "$ADF" --query identity.principalId -o tsv)

if [ -z "$ADF_MI_PRINCIPAL_ID" ]; then
  echo "! Could not get ADF managed identity principalId. Try re-running in a minute." >&2
  exit 1
fi

ST_ID=$(az storage account show -n "$SA" -g "$RG" --query id -o tsv)

echo "Granting ADF managed identity access to storage (Storage Blob Data Contributor)..."

EXISTING_ROLE=$(az role assignment list \
  --assignee-object-id "$ADF_MI_PRINCIPAL_ID"  \
  --role "Storage Blob Data Contributor" \
  --scope "$ST_ID" \
  --query "[0].id" -o tsv)

if [ -z "$EXISTING_ROLE" ]; then
  az role assignment create \
    --assignee-object-id "$ADF_MI_PRINCIPAL_ID" \
    --role "Storage Blob Data Contributor" \
    --scope "$ST_ID" >/dev/null
  echo "   Role assigned."
else
  echo "   Role assignment already exists, skipping."
fi

echo
echo "Done!"
echo "Resource Group: $RG"
echo "Storage:        $SA"
echo "Data Factory:   $ADF"
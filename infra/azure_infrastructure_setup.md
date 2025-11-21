# Azure Infrastructure Setup

This folder contains the CLI script used to provision the core Azure resources for the Smart Home Energy Pipeline (Stage 1).  
The script is idempotent and intended for quick environment setup during development.

---

## 1. Environment Configuration

Copy the example file:

```bash
cp infra/cli/azure_credentials.env.example infra/cli/azure_credentials.env
```

Provide your subscription and naming values in `azure_credentials.env`:

```env
SUBSCRIPTION=<subscription-id>
ENV=dev

RG=rg-shep-dev
LOC=westeurope    # choose your region

SA=stshepdev      # storage account name must be globally unique
ADF=adf-shep-dev
```

The script uses these values to derive resource names.  
If the storage account name is already in use globally, adjust your storage account name `SA` and rerun.

---

## 2. Provision Resources

Run from the repository root:

```bash
chmod +x infra/cli/provision_azure_resources.sh
az login
./infra/cli/provision_azure_resources.sh
```

Resources created (or reused):

- Resource Group (`RG`)
- ADLS Gen2 storage account (`SA`)
  - Containers: `raw`, `silver`, `gold`
- Azure Data Factory (`ADF`) with a system-assigned identity
- Role assignment granting ADF access to the storage account

---

## 3. Verification

After execution, the specified resource group should contain:

- The storage account with the three lake containers
- The Data Factory instance with active managed identity

---

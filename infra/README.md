# Infrastructure

This folder contains everything that talks directly to Azure for this project.

- `cli/` – small shell scripts that use `az` and `azcopy`.
- `azure_infrastructure_setup.md` – short notes on what the scripts do and how to run them.

Mainly you need the two commands:

```bash
# 1) Create or update RG, storage account, containers and Data Factory
./infra/cli/az_setup.sh

# 2) upload local Bronze data (data_ingestion/data/bronze) to ADLS 'raw'
./infra/cli/upload_raw_to_adls.sh
```

For details (env variables, what gets created, etc.) see
`infra/azure_infrastructure_setup.md`.

---

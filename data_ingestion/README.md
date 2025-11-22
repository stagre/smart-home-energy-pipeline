# Data Ingestion

This module contains the **local data ingestion utilities** for the pipeline.  
It standardises raw CSV exports into a clean **Bronze (Hive-partitioned) folder layout**  
for downstream processing in Databricks, Azure, notebooks, etc.

Datasets currently supported:

- battery  
- energy_balance (general totals)  
- main_consumption  
- ohmpilot (heating buffer storage)  
- wattpilot (EV car charger)
- solar 

---

## Folder Structure

```text
data_ingestion/
  data/
    raw/                 # full real datasets (local only, not committed)
    bronze/              # Hive-partitioned Parquet output (local → upload to ADLS raw)
    examples/            # synthetic example datasets 
      raw/
        battery/
          battery_example.csv
      bronze/
        source=battery/
          year=2024/
            month=01/
              battery_202401.parquet
  scripts/
    column_maps.py
    standardise_raw_to_hive.py
  README.md
```

---

## Steps

### 1. Standardise raw CSV files into a Hive-style Bronze layout (CSV → Parquet)

The main script `scripts/standardise_raw_to_bronze.py` performs:

1. Read all CSV files for a dataset (e.g. `data/raw/battery/*.csv`)
2. Rename columns using the corresponding entry in `COL_MAPS`
3. Parse and normalise timestamps
4. Add `year` and `month` fields for partitioning
5. Write one Parquet file per `(year, month)` to a Hive-style Bronze layout:
```text
bronze/
  source=<dataset>/
    year=<YYYY>/
      month=<MM>/
        <dataset>_<YYYYMM>.parquet
```

`scripts/column_maps.py` defines per-dataset translation maps from  
German column names → standardised English names.

**Example (battery):**

```python
BATTERY_COL_MAP = {
    "Datum und Uhrzeit": "timestamp",
    "Batteriespannung": "battery_voltage_v",
    "Batteriestrom": "battery_current_a",
    "Batterietemperatur minimum": "battery_temp_min_c",
    "State of Charge": "state_of_charge_pct",
}
```

### 2. Upload Bronze data to Azure

For further processing, the Bronze layout can be uploaded to Azure from  
`data_ingestion/data/bronze/` into the ADLS `raw` container using:

```bash
./infra/cli/upload_raw_to_adls.sh
```

For more details see `infra/azure_infrastructure_setup.md`.
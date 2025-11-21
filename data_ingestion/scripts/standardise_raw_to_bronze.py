import pandas as pd 
from pathlib import Path
from column_maps import COL_MAPS

def build_hive_for_folder(
    in_path: Path,
    out_root: str = "hive",
    sep: str = ",",          
    decimal: str = ".",      
    timestamp_col_de: str = "Datum und Uhrzeit",
    to_parquet: bool = True,
):
    dataset_name = in_path.name           # e.g. "solar", "battery"
    col_map = COL_MAPS.get(dataset_name, {})

    files = sorted(in_path.glob("*.csv"))
    if not files:
        print(f"No CSV files in {in_path}")
        return

    for csv_file in files:
        print(f"Processing {csv_file}")
        # skip 2nd row, since it contains metadata regarding the column types
        df = pd.read_csv(csv_file, sep=sep, decimal=decimal, header=0, skiprows=[1])

        # 1) rename columns DE → EN
        df = df.rename(columns=col_map)

        # 2) normalise timestamp
        ts_col = col_map.get(timestamp_col_de, "timestamp")
        print(df.columns.to_list)
        df[ts_col] = pd.to_datetime(df[ts_col], format='%d.%m.%Y %H:%M', utc=False)

        # 3) add year & month for partitioning
        df["year"] = df[ts_col].dt.year
        df["month"] = df[ts_col].dt.month

        # 4) write one file per (year, month)
        for (year, month), grp in df.groupby(["year", "month"]):
            out_dir = (
                Path(out_root)
                / f"source={dataset_name}"
                / f"year={year}"
                / f"month={month:02d}"
            )
            out_dir.mkdir(parents=True, exist_ok=True)

            out_file = out_dir / f"{dataset_name}_{year}{month:02d}"
            grp = grp.drop(columns=["year", "month"])

            if to_parquet:
                grp.to_parquet(out_file.with_suffix(".parquet"), index=False)
            else:
                grp.to_csv(out_file.with_suffix(".csv"), index=False)

if __name__ == "__main__":
    for sub in Path("../data/raw").iterdir():
        if sub.is_dir():
            build_hive_for_folder(sub, out_root="../data/bronze")
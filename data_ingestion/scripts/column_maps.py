# translation maps for the data sets' column names (german to english)
# units are derived from the second row of the raw CSV files
# battery
BATTERY_COL_MAP = {
    "Datum und Uhrzeit": "timestamp",
    "Batteriespannung": "battery_voltage_v",
    "Batteriestrom": "battery_current_a",
    "Batterietemperatur minimum": "battery_temp_min_c",
    "State of Charge": "state_of_charge_pct",
}

# energy-balance
ENERGY_BALANCE_COL_MAP = {
    "Datum und Uhrzeit": "timestamp",
    "Direkt verbraucht": "direct_consumption_wh",
    "Energie aus Batterie bezogen": "energy_from_battery_wh",
    "Energie in Batterie gespeichert": "energy_to_battery_wh",
    "Energie ins Netz eingespeist": "energy_export_grid_wh",
    "Energie vom Netz bezogen": "energy_import_grid_wh",
    "PV Produktion": "pv_production_wh",
    "Verbrauch": "total_consumption_wh",
}

# main-consumption (grid / main power meter)
MAIN_CONSUMPTION_COL_MAP = {
    "Datum und Uhrzeit": "timestamp",
    "Energie ins Netz eingespeist | PowerMeter": "energy_export_wh",
    "Energie vom Netz bezogen | PowerMeter": "energy_import_wh",
    "Scheinleistung L1 Einspeisepunkt | PowerMeter": "apparent_power_l1_va",
    "Scheinleistung L2 Einspeisepunkt | PowerMeter": "apparent_power_l2_va",
    "Scheinleistung L3 Einspeisepunkt | PowerMeter": "apparent_power_l3_va",
    "Spannung AC L1 Einspeisepunkt | PowerMeter": "voltage_l1_v",
    "Spannung AC L2 Einspeisepunkt | PowerMeter": "voltage_l2_v",
    "Spannung AC L3 Einspeisepunkt | PowerMeter": "voltage_l3_v",
    "Wirkleistung L1 Einspeisepunkt | PowerMeter": "active_power_l1_w",
    "Wirkleistung L2 Einspeisepunkt | PowerMeter": "active_power_l2_w",
    "Wirkleistung L3 Einspeisepunkt | PowerMeter": "active_power_l3_w",
}

# ohmpilot (water buffer / heater)
OHMPILOT_COL_MAP = {
    "Datum und Uhrzeit": "timestamp",
    "Energie Ohmpilot": "ohmpilot_energy_wh",
    "Temperatur Ohmpilot": "ohmpilot_temperature_c",
}


# solar (Symo GEN24 8.0 Plus inverter)
SOLAR_COL_MAP = {
    "Datum und Uhrzeit": "timestamp",
    "Blindleistung | Symo GEN24 8.0 Plus": "reactive_power_var",
    "Energie | Symo GEN24 8.0 Plus": "energy_wh",
    "Energie MPP1 | Symo GEN24 8.0 Plus": "energy_mpp1_wh",
    "Energie MPP2 | Symo GEN24 8.0 Plus": "energy_mpp2_wh",
    "Generatorisolationswiderstand | Symo GEN24 8.0 Plus": "generator_isolation_resistance_ohm",
    "Leistungsfaktor | Symo GEN24 8.0 Plus": "power_factor",
    "Scheinleistung | Symo GEN24 8.0 Plus": "apparent_power_va",
    "Spannung AC L1 | Symo GEN24 8.0 Plus": "voltage_ac_l1_v",
    "Spannung AC L1-L2 | Symo GEN24 8.0 Plus": "voltage_ac_l1_l2_v",
    "Spannung AC L2 | Symo GEN24 8.0 Plus": "voltage_ac_l2_v",
    "Spannung AC L2-L3 | Symo GEN24 8.0 Plus": "voltage_ac_l2_l3_v",
    "Spannung AC L3 | Symo GEN24 8.0 Plus": "voltage_ac_l3_v",
    "Spannung AC L3-L1 | Symo GEN24 8.0 Plus": "voltage_ac_l3_l1_v",
    "Spannung DC MPP1 | Symo GEN24 8.0 Plus": "voltage_dc_mpp1_v",
    "Spannung DC MPP2 | Symo GEN24 8.0 Plus": "voltage_dc_mpp2_v",
    "Spezifischer Ertrag | Symo GEN24 8.0 Plus": "specific_yield_kwh_per_kwp",
    "Strom AC L1 | Symo GEN24 8.0 Plus": "current_ac_l1_a",
    "Strom AC L2 | Symo GEN24 8.0 Plus": "current_ac_l2_a",
    "Strom AC L3 | Symo GEN24 8.0 Plus": "current_ac_l3_a",
    "Strom DC MPP1 | Symo GEN24 8.0 Plus": "current_dc_mpp1_a",
    "Strom DC MPP2 | Symo GEN24 8.0 Plus": "current_dc_mpp2_a",
}

# wattpilot (EV car charger)
WATTPILOT_COL_MAP = {
    "Datum und Uhrzeit": "timestamp",
    "Energie von PV an Wattpilot": "wattpilot_energy_from_pv_wh",
    "Energie vom Netz an Wattpilot": "wattpilot_energy_from_grid_wh",
    "Energie von Batterie an Wattpilot": "wattpilot_energy_from_battery_wh",
    "Energie Wattpilot | Wattpilot_32716452": "wattpilot_energy_total_wh",
    "Eingestellte Stromstärke | Wattpilot_32716452": "wattpilot_set_current_a",
    "Typ 2 | Wattpilot_32716452": "wattpilot_type2_current_a",
    "Spannung AC L1 | Wattpilot_32716452": "wattpilot_voltage_l1_v",
    "Spannung AC L2 | Wattpilot_32716452": "wattpilot_voltage_l2_v",
    "Spannung AC L3 | Wattpilot_32716452": "wattpilot_voltage_l3_v",
    "WLAN-Signalstärke | Wattpilot_32716452": "wattpilot_wifi_signal_dbm",
}

# master dict by dataset folder name
COL_MAPS = {
    "battery": BATTERY_COL_MAP,
    "energy_balance": ENERGY_BALANCE_COL_MAP,
    "main_consumption": MAIN_CONSUMPTION_COL_MAP,
    "ohmpilot": OHMPILOT_COL_MAP,
    "solar": SOLAR_COL_MAP,
    "wattpilot": WATTPILOT_COL_MAP,
}
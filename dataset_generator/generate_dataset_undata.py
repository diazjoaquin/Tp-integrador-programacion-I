# genera_dataset_undata.py
import pandas as pd
import country_converter as coco

# Ruta al archivo descargado de UNdata
INPUT_FILE = "SYB67_1_202411_Population, Surface Area and Density.csv"
OUTPUT_FILE = "dataset_paises_undata.csv"

# Cargar CSV original de UNdata
df = pd.read_csv(INPUT_FILE, encoding="utf-8", dtype=str, low_memory=False)

# Normalizar nombres de columnas
df.columns = ["Region/Country/Area", "Col2", "Year", "Series", "Value", "Footnotes", "Source"]

# Filtrar filas válidas (con año numérico)
df_clean = df[df["Year"].str.isdigit()].copy()

# Filtrar series de interés
mask_population = df_clean["Series"].str.contains("Population mid-year estimates \\(millions\\)", na=False)
mask_area = df_clean["Series"].str.contains("Surface area", na=False)

df_pop = df_clean[mask_population].copy()
df_area = df_clean[mask_area].copy()

# Convertir valores
df_pop["Value"] = df_pop["Value"].str.replace(",", "").astype(float)
df_area["Value"] = df_area["Value"].str.replace(",", "").astype(float)

# Población en millones → personas
df_pop["Population"] = (df_pop["Value"] * 1_000_000).astype(int)

# Superficie en miles de km² → km²
df_area["Area_km2"] = (df_area["Value"] * 1000).astype(int)

# Tomar año más reciente por país
df_pop_latest = df_pop.sort_values(by="Year").groupby("Region/Country/Area").tail(1)
df_area_latest = df_area.sort_values(by="Year").groupby("Region/Country/Area").tail(1)

# Combinar población y superficie
df_merge = pd.merge(
    df_pop_latest[["Region/Country/Area", "Population"]],
    df_area_latest[["Region/Country/Area", "Area_km2"]],
    on="Region/Country/Area",
    how="inner"
)

# Mapear códigos M49 → nombres de países
df_merge["Region/Country/Area"] = df_merge["Region/Country/Area"].astype(str)
df_merge["nombre"] = coco.convert(names=df_merge["Region/Country/Area"], src="UNcode", to="name_short")

# Filtrar entradas válidas
df_final = df_merge[df_merge["nombre"] != "not found"].copy()

# Renombrar columnas
df_final = df_final.rename(columns={
    "Population": "poblacion",
    "Area_km2": "superficie"
})[["nombre", "poblacion", "superficie"]]

# Asignar continente
df_final["continente"] = coco.convert(names=df_final["nombre"], to="continent")

# Exportar a CSV
df_final.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")

print(f"Archivo generado: {OUTPUT_FILE}")
print(f"Total de países/territorios: {len(df_final)}")
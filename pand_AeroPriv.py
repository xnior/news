import pandas as pd
import os
from colorama import Fore, Style

os.system("cls" if os.name == "nt" else "clear")

print(Fore.GREEN + Style.BRIGHT + "Python - Pandas - AeroPrivados" + Style.RESET_ALL)
res = input(Fore.BLUE + Style.BRIGHT + "Ready to read the CSV file (yes/no): " + Style.RESET_ALL)
if res.lower() not in ["yes", "y"]:
    print(Fore.RED + Style.BRIGHT + "Restart the Application when ready to read the file CSV." + Style.RESET_ALL)
    exit()


try:
    # data_frame = pd.read_csv('Python/data.csv')
    data_frame = pd.read_csv(
        "C:/Users/Adhemar Jr/Downloads/AerodromosPrivados.csv",
        encoding="latin1",
        delimiter=";",
        on_bad_lines="skip",
        skiprows=1,
    )
    # Replace commas with periods
    data_frame = data_frame.replace(",", ".", regex=True)
    print(data_frame)
except FileNotFoundError:
    print("Error: 'data.csv' file not found. Please check the file path.")
    data_frame = pd.DataFrame()  # Create an empty DataFrame as a fallback
print(data_frame.shape)
print(data_frame.describe())
print(data_frame.values)

# print(data_frame["Codigo_OACI"])
print(data_frame[data_frame["Código OACI"] == "SJ3D"])

dtexp = pd.DataFrame(
    data_frame,
    columns=[
        "Código OACI",
        "Nome",
        "Município",
        "UF",
        "LATGEOPOINT",
        "LONGEOPOINT",
        "Latitude",
        "Longitude",
        "Altitude",
        "Operação Diurna",
        "Operação Noturna",
        "Designação 1",
        "Comprimento 1",
        "Largura 1",
        "Resistência 1",
        "Superfície 1",
    ],
)

# Rename columns
dtexp.rename(
    columns={
        "Código OACI": "CodigoOACI",
        "Nome": "Nome",
        "Município": "Municipio",
        "UF": "UF",
        "LATGEOPOINT": "LatGeoPoint",
        "LONGEOPOINT": "LonGeoPoint",
        "Latitude": "Latitude",
        "Longitude": "Longitude",
        "Altitude": "Altitude",
        "Operação Diurna": "OperacaoDiurna",
        "Operação Noturna": "OperacaoNoturna",
        "Designação 1":"Designacao1",
        "Comprimento 1": "Comprimento1",
        "Largura 1": "Largura1",
        "Resistência 1": "Resistencia1",
        "Superfície 1": "Superficie1",
    },
    inplace=True,
)
# Ensure specific columns are numeric
numeric_columns = ["LatGeoPoint", "LonGeoPoint", "Altitude", "Comprimento1", "Largura1"]
for col in numeric_columns:
    dtexp[col] = pd.to_numeric(dtexp[col], errors="coerce")

print(dtexp)

dtexp.to_json(
    "C:/Users/Adhemar Jr/Downloads/AeroPriv.json",
    orient="records",
    force_ascii=False,
    indent=4,
)

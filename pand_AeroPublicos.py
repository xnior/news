import pandas as pd
import os
from colorama import Fore, Style

os.system("cls" if os.name == "nt" else "clear")
print(Fore.GREEN + Style.BRIGHT + "Python - Pandas - AeroPublicos" + Style.RESET_ALL)

res = input(Fore.BLUE + Style.BRIGHT + "Did remove the first character of the CSV file (yes/no): ")
if res.lower() not in ["yes", "y"]:
    print(Fore.RED + Style.BRIGHT + "Please remove the first character of the CSV file and try again." + Style.RESET_ALL)
    exit()

try:
    # data_frame = pd.read_csv('Python/data.csv')
    data_frame = pd.read_csv(
        "C:/Users/Adhemar Jr/Downloads/AerodromosPublicos.csv",
        encoding="latin1",
        on_bad_lines="skip",
        delimiter=";",
        skiprows=1,
    )
    print(data_frame.iloc[2])
    data_frame = data_frame.replace(r',.*', '', regex=True)
    print(data_frame.iloc[2])

    
except FileNotFoundError:
    print("Error: 'data.csv' file not found. Please check the file path.")
    data_frame = pd.DataFrame()  # Create an empty DataFrame as a fallback

print(data_frame.shape)
print(data_frame.describe())
print(data_frame.values)

# print(data_frame["Codigo_OACI"])
print(data_frame[data_frame["Código OACI"] == "SBSP"])

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
dtexp.rename(
    columns={
        "Código OACI": "CodigoOACI",
        # "Nome": "Nome",
        "Município": "Municipio",
        "UF": "UF",
        "LATGEOPOINT": "LatGeoPoint",
        "LONGEOPOINT": "LonGeoPoint",
        "Latitude": "Latitude",
        "Longitude": "Longitude",
        # "Altitude": "Altitude",
        "Operação Diurna": "OperacaoDiurna",
        "Operação Noturna": "OperacaoNoturna",
        "Designação 1": "Designacao1",
        "Comprimento 1": "Comprimento1",
        "Largura 1": "Largura1",
        "Resistência 1": "Resistencia1",
        "Superfície 1": "Superficie1",
    },
    inplace=True,
    
)
print(dtexp)

numeric_columns = ["LatGeoPoint", "LonGeoPoint", "Altitude", "Comprimento1", "Largura1"]
for col in numeric_columns:
    dtexp[col] = pd.to_numeric(dtexp[col], errors="coerce")

dtexp.to_json(
    "C:/Users/Adhemar Jr/Downloads/AeroPublico.json",
    orient="records",
    force_ascii=False,
    indent=4,
)

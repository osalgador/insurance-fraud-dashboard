import pandas as pd
import numpy as np

df=pd.read_csv("insurance_claims.csv")#Leemos nuestra base de datos
df.info()#Obtenemos la información de los datos a tratar
df.describe()
#Quitaremos columnas como c39 y policy number ya que no beneficiarán a nuestro modelo
df = df.drop(columns=[
"policy_bind_date",
"incident_date",
"insured_zip",
"auto_make",
"auto_model", "policy_number",
"_c39"
])
#verificaremos los cambios
df.dtypes
print(df)
#Ahora la unica columna que tiene datos faltantes es "authorities_contacted" por lo que rellenaremos los datos faltantes
df["authorities_contacted"] = df["authorities_contacted"].fillna("Unknown")
df.info()
#Ahora solo debemos comprobar que no quede datos nulos
df.isnull().sum()
#Para nuestras gráficas en PowerBi haremos las columnas con un si/no variables binarias si=1 no=0
df["property_damage"] = df["property_damage"].map({"YES":1,"NO":0})

df["police_report_available"] = df["police_report_available"].map({"YES":1,"NO":0})

df["fraud_reported"] = df["fraud_reported"].map({"Y":1,"N":0})
print(df[["property_damage", "police_report_available", "fraud_reported"]])
#Existen valores diferentes por lo que intentaremos estandarizar todos los datos 
df["property_damage"].unique()
df["police_report_available"].unique()
# revisar valores reales
print(df["property_damage"].unique())
print(df["police_report_available"].unique())

# limpiar espacios y convertir a texto
df["property_damage"] = df["property_damage"].astype(str).str.strip().str.upper()
df["police_report_available"] = df["police_report_available"].astype(str).str.strip().str.upper()
df["fraud_reported"] = df["fraud_reported"].astype(str).str.strip().str.upper()

# reemplazar valores
df["property_damage"] = df["property_damage"].replace({"YES": 1, "NO": 0, "?": 0})
df["police_report_available"] = df["police_report_available"].replace({"YES": 1, "NO": 0, "?": 0})
df["fraud_reported"] = df["fraud_reported"].replace({"Y": 1, "N": 0})

# convertir a numérico
df["property_damage"] = pd.to_numeric(df["property_damage"], errors="coerce")
df["police_report_available"] = pd.to_numeric(df["police_report_available"], errors="coerce")
df["fraud_reported"] = pd.to_numeric(df["fraud_reported"], errors="coerce")

# rellenar faltantes si queda alguno
df["property_damage"] = df["property_damage"].fillna(0).astype(int)
df["police_report_available"] = df["police_report_available"].fillna(0).astype(int)
df["fraud_reported"] = df["fraud_reported"].fillna(0).astype(int)
#Comprobamos que ya no exista valores nulos, vacíos o NaN
print(df[["property_damage", "police_report_available", "fraud_reported"]].isnull().sum())
print(df[["property_damage", "police_report_available", "fraud_reported"]].head(10))
#Crearemos una gráfica de las edades de los clientes
import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(df["age"], bins=20)

plt.title("Distribución de edad de clientes")
plt.show()
#Gráfica de fraudes reportados
sns.countplot(x="fraud_reported", data=df)

plt.title("Casos de fraude reportados")
plt.show()
#Gráfica de reclamos por severidad
sns.countplot(x="incident_severity", data=df)

plt.title("Severidad del incidente")
plt.show()
#Reclamos por tipo de incidente
sns.countplot(y="incident_type", data=df)

plt.title("Tipo de incidente")
plt.show()
#Gráfico de reclamos por estado
df["incident_state"].value_counts().plot(kind="bar")

plt.title("Reclamos por estado")
plt.show()
#Gráfico entre monto de reclamo y fraude
sns.boxplot(x="fraud_reported", y="total_claim_amount", data=df)

plt.title("Monto del reclamo vs fraude")
plt.show()
#Crearemos algunas variables para hacer un análisis con los datos de fraude
df["vehicle_age"] = 2024 - df["auto_year"]#Edad del vehículo
df["total_damage"] = (
    df["injury_claim"] +
    df["property_claim"] +
    df["vehicle_claim"]
)#Daños totales
df["severe_accident"] = df["incident_severity"].isin([
    "Major Damage",
    "Total Loss"
]).astype(int)#indicadores de accidentes severos
df["age_group"] = pd.cut(
df["age"],
bins=[18,30,40,50,60,70],
labels=["18-30","31-40","41-50","51-60","61-70"]
)#Rangos de edades
df["claim_range"] = pd.cut(
df["total_claim_amount"],
bins=[0,20000,40000,60000,80000,120000],
labels=[
"0-20k",
"20k-40k",
"40k-60k",
"60k-80k",
"80k+"
]
)#rangos de montos de reclamación
df.to_csv("insurance_fraud_dashboard_dataset.csv", index=False)

#Importamos librerías
import pandas as pd
import numpy as np
#Cargamos el dataset del documento limpio previamente
df=pd.read_csv("data\insurance_fraud_dashboard_dataset.csv")
#Prepararemos el dataset para el modelo
y = df["fraud_reported"]#VARIABLE OBJETIVO
features = [#SELECCIÓN DE VARIABLES CARACTERÍSTICAS
    "age",#N
    "months_as_customer",#N
    "policy_annual_premium",#N
    "policy_deductable",#N
    "umbrella_limit",#N
    "incident_type",#C
    "collision_type",#C
    "incident_severity",#C
    "incident_state",#C
    "incident_hour_of_the_day",#N
    "number_of_vehicles_involved",#N
    "property_damage",#C
    "police_report_available",#C
    "bodily_injuries",#N
    "witnesses",#N
    "total_claim_amount",#N
    "vehicle_age",#N
    "total_damage",#N
    "severe_accident"#N
]

X = df[features]# Se almacenan en un dataframe nuevo las columnas seleccionadas
df.info(features)#Para mejorar la clasificación se observa la información para separar las columnas
categorical_cols = [
    "incident_type",
    "collision_type",
    "incident_severity",
    "incident_state"
]#SEPARACIÓN DE VARIABLES CATEGÓRICAS
numerical_cols = [col for col in X.columns if col not in categorical_cols]#VARIABLES NUMÉRICAS 

X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)#USO DE ONE HOT ENCODING
#COMENZAMOS A PREPARAR EL MODELO PARA ENTRENARMIENTO
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(#DIVIDIMOS EL MODELO TRAIN/TEST
    X, y,
    test_size=0.2,
    random_state=42
)
#ESCALAMOS LOS DATOS
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
#FASE 2: REGRESIÓN LOGÍSTICA
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=2000, class_weight="balanced")

# Escalado
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Modelo
model.fit(X_train_scaled, y_train)

# Predicción correcta
y_pred = model.predict(X_test_scaled)
y_prob = model.predict_proba(X_test_scaled)[:,1]
#FASE 3:EVALUACION DEL MODELO
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

print(classification_report(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, y_prob))

#MATRIZ DE CONFUSION
import seaborn as sns
import matplotlib.pyplot as plt

cm = confusion_matrix(y_test, y_pred)

sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()
#CURVA ROC
from sklearn.metrics import roc_curve

fpr, tpr, _ = roc_curve(y_test, y_prob)

plt.plot(fpr, tpr)
plt.plot([0,1],[0,1], linestyle="--")
plt.title("ROC Curve")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.show()
#INTERPRETACIÓN
import numpy as np

coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_[0]
})

coefficients = coefficients.sort_values(by="Coefficient", ascending=False)

print(coefficients.head(10))
#RANDOM FOREST
from sklearn.ensemble import RandomForestClassifier
rf_model = RandomForestClassifier(
    n_estimators=100,
    class_weight="balanced",
    random_state=42
)

rf_model.fit(X_train, y_train)

y_pred_rf = rf_model.predict(X_test)
y_prob_rf = rf_model.predict_proba(X_test)[:,1]
#EVALUACION
from sklearn.metrics import classification_report, roc_auc_score

print(classification_report(y_test, y_pred_rf))
print("ROC-AUC:", roc_auc_score(y_test, y_prob_rf))
#IMPORTACIA DE VARIABLES EN EL MODELO

feature_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf_model.feature_importances_
})

feature_importance = feature_importance.sort_values(by="Importance", ascending=False)

print(feature_importance.head(10))

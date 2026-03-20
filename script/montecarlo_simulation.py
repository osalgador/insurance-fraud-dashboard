import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("data\insurance_fraud_dashboard_dataset.csv")
#Datos objetivo
fraud_data = df[df["fraud_reported"] == 1]
#CALCULAMOS TASA DE FRAUDES
fraud_rate = df["fraud_reported"].mean()
print("Fraud Rate:", fraud_rate)
#MONTO DE FRAUDE 
fraud_amounts = fraud_data["total_claim_amount"]

mean_amount = fraud_amounts.mean()
std_amount = fraud_amounts.std()

print("Mean:", mean_amount)
print("Std:", std_amount)
#SIMULACIÓN MONTECARLO CON 1000 CASOS
n_simulations = 10000
n_claims = 1000

total_losses = []

for i in range(n_simulations):

    # 1. Simular número de fraudes
    n_frauds = np.random.binomial(n_claims, fraud_rate)

    # 2. Simular montos de fraude
    simulated_amounts = np.random.normal(mean_amount, std_amount, n_frauds)

    # evitar negativos
    simulated_amounts = np.clip(simulated_amounts, 0, None)

    # 3. pérdida total
    total_loss = simulated_amounts.sum()

    total_losses.append(total_loss)

total_losses = np.array(total_losses)
#RESULTADOS
print("Expected Loss:", total_losses.mean())
print("95th Percentile:", np.percentile(total_losses, 95))
print("99th Percentile:", np.percentile(total_losses, 99))

#VISUALIZACIÓN DE DATOS
plt.hist(total_losses, bins=50)
plt.title("Monte Carlo Simulation of Fraud Losses")
plt.xlabel("Total Loss")
plt.ylabel("Frequency")
plt.show()
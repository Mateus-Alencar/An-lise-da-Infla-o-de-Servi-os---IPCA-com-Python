import requests
import pandas as pd
import matplotlib.pyplot as plt

codigo_serie = 432

url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_serie}/dados?formato=json"

response = requests.get(url)

if response.status_code == 200:
    dados = response.json()
    df = pd.DataFrame(dados)
    df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y")
    df["valor"] = pd.to_numeric(df["valor"])
    plt.style.use('dark_background')  
    plt.figure(figsize=(8, 3))  
    plt.plot(df["data"], df["valor"], label="IPCA - Serviços", color="#FF6347", linewidth=2) 
    plt.title(f"Análise da Série Temporal - IPCA - Serviços ({codigo_serie})", fontsize=14, fontweight='bold', color='white')
    plt.xlabel("Data", fontsize=12, fontweight='bold', color='white')
    plt.ylabel("Valor", fontsize=12, fontweight='bold', color='white')
    plt.xticks(rotation=45, fontsize=10, color='white')a
    plt.yticks(fontsize=10, color='white')
    plt.grid(True, linestyle='--', color='gray', alpha=0.5)
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.show()

else:
    print(f"Erro na API: {response.status_code}")
    
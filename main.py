import pandas as pd
import mysql.connector

# Convertir le fichier Excel en CSV (si nécessaire)
excel_file_path = '1-DEBIT GENERAL CGLE26.csv'
csv_file_path = 'data.csv'
excel_data = pd.read_excel(excel_file_path, skiprows=3)
excel_data.to_csv(csv_file_path, index=False)

# Lire le fichier CSV
csv_data = pd.read_csv(csv_file_path)
print (csv_data)
# Établir une connexion à la base de données MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="User",
    password="1214",
    database="mydb"
)


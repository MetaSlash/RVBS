import csv

def generate_sql_from_csv(csv_file_path, table_name, encoding='utf-8'):
    try:
        with open(csv_file_path, mode='r', newline='', encoding=encoding) as csvfile:
            csvreader = csv.reader(csvfile)
            headers = next(csvreader)  # Lire les en-têtes

            # Générer la partie VALUES de la commande SQL
            values = []
            for row in csvreader:
                # Convertir chaque valeur en une chaîne SQL appropriée
                sql_values = ', '.join([f'"{value}"' if not value.replace('.', '', 1).isdigit() else value for value in row])
                values.append(f"({sql_values})")

            # Combiner toutes les valeurs en une seule chaîne
            values_str = ",\n           ".join(values)

            # Générer la commande SQL complète
            sql_command = f"INSERT INTO {table_name}\n           ({', '.join(headers)})\n    VALUES\n           {values_str};"

            return sql_command
    except UnicodeDecodeError:
        print(f"Erreur de décodage avec l'encodage {encoding}. Essayez un autre encodage.")
        return None

# Exemple d'utilisation
csv_file_path = 'sql_querry/1-DEBIT GENERAL CGLE26.csv'  # Chemin vers votre fichier CSV
table_name = 'rvbs'

# Essayer d'abord avec UTF-8
sql_command = generate_sql_from_csv(csv_file_path, table_name, encoding='utf-8')
if sql_command is None:
    # Si UTF-8 échoue, essayer avec ISO-8859-1
    sql_command = generate_sql_from_csv(csv_file_path, table_name, encoding='iso-8859-1')

if sql_command:
    print(sql_command)

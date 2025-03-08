import mysql.connector

def debit_prep(connection_cred, item_wanted, quantity):
    # Établir une connexion à la base de données MySQL
    mydb = mysql.connector.connect(
        host = connection_cred["host"],
        user = connection_cred["user"],
        password = connection_cred["password"],
        database = connection_cred["database"]
    )

    cursor = mydb.cursor()
    request = "SELECT stock FROM rvbs WHERE id = %s"
    cursor.execute(request, (item_wanted,))
    data = cursor.fetchone()
    
    if data == None:
        return "None"
    else:
        data = data[0]

    return data - quantity

def display(data):
    if data == "None":
        return "Stock inconue ou non renseigné"
    elif data > 0:
        return f"il restera {data} unitée(s)"
    else: 
        return f"il manquera {- data} unitée(s)"

connection_cred = {
    "host":     "192.168.0.22",
    "user":     "User",
    "password": "1214",
    "database": "mydb"
}

item_wanted = int(input("enter the id of the item you want. "))
quantity = int(input("enter the quantity of the item you want. "))

print(display(debit_prep(connection_cred, item_wanted, quantity)))

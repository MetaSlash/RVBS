import mysql.connector 

def stock_rest_calc_unit(mydb, id, quantity):
    """
    Calculate the remaining stock of a specified item after a requested quantity is deducted.

    Establishes a connection to a MySQL database using provided credentials, retrieves
    the current stock level of an item identified by `id`, and returns the 
    difference between the current stock and `quantity`. If the item is not found, 
    returns "None".

    Args:
        connection_cred (dict): A dictionary containing database connection credentials 
                                with keys 'host', 'user', 'password', and 'database'.
        id (int): The ID of the item for which the stock needs to be checked.
        quantity (int): The quantity of the item requested.

    Returns:
        int or str: The remaining stock quantity after deduction, or "None" if the item
                    is not found in the database.
    """

    # Établir une connexion à la base de données
    # Exécuter une requête SQL pour récupérer le stock actuel de l'article
    cursor = mydb.cursor()
    request = "SELECT stock FROM rvbs WHERE id = %s"
    cursor.execute(request, (id,))
    data = cursor.fetchone()

    # Si l'article n'est pas trouvé, renvoyer None
    if data == None or data[0] == None:
        return "None"
    else:
        # Renvoyer la différence entre le stock actuel et la quantité demandée
        data = data[0]
        return data - quantity


def display(data, id):
    """
    Converts the result of stock_rest_calc into a human-readable string.

    Args:
        data (int or str): The result of stock_rest_calc. If "None", returns
            "no stock found". If the number is positive, returns a string
            with the number of units left. If the number is negative, returns
            a string with the number of units missing.

    Returns:
        str: A human-readable string describing the stock level.
    """
    if data == "None":
        result = "[=] Stock inconue ou non renseigné"   
    elif data >= 0:
        # If the number of units left is positive, 
        # return a string indicating the number of units left.
        result = f"[+] Il restera {data} unitée(s) de l'objet {id}"
    elif data < 0: 
        # If the number of units left is negative, 
        # return a string indicating the number of units missing.
        result = f"[-] Il manquera {- data} unitée(s) de l'objet {id}"
    
    return result

# faire le calcule de stock pour tous les item demandé
def stock_rest_calc(connection_cred ,list_of_items):
    """
    Calculates the remaining stock for multiple items after deducting requested quantities.

    Establishes a connection to a MySQL database using provided credentials, iterates over
    a list of item IDs and quantities, and retrieves the current stock levels for each item.
    It then calculates the remaining stock after the requested quantity is deducted and
    returns human-readable messages indicating the stock status for each item.

    Args:
        connection_cred (dict): A dictionary containing database connection credentials 
                                with keys 'host', 'user', 'password', and 'database'.
        list_of_items (dict): A dictionary containing lists of item IDs under the key 'id' 
                              and corresponding requested quantities under the key 'quantity'.

    Returns:
        list: A list of strings, each describing the stock status of an item, indicating 
              whether there are sufficient units left or if some units are missing.
    """
    
    message = ""
    results = []
    mydb = mysql.connector.connect(
        host = connection_cred["host"],
        user = connection_cred["user"],
        password = connection_cred["password"],
        database = connection_cred["database"]
    )

    number_of_items = len(list_of_items["id"])

    for index in range(number_of_items):
        # Get the current item ID and quantity
        item_id = list_of_items["id"][index]
        item_quantity = list_of_items["quantity"][index]
        
        # Calculate the remaining stock for this item
        raw_results = stock_rest_calc_unit(mydb, item_id, item_quantity)
        
        # Append the result to the list
        results.append(raw_results)
        message += display(raw_results, item_id) + "\n"


    exit = {"human readable" : message,
            "machine readable" : results}

    return exit

    

########## Human ##########

if __name__ == "__main__":
    
    list_of_items = {
    "id" :      [124, 2, 3, 4, 5],
    "quantity" :[8, 5, 1, 10, 2]
    }

    connection_cred = {
    "host":     "192.168.0.22",
    "user":     "User",
    "password": "1214",
    "database": "mydb"
    }

    print(stock_rest_calc(connection_cred, list_of_items)["human readable"])
    
import psycopg2

def execute_sql_dump(host, port, database, username, password, dump_file):
    # Connexion à la base de données
    conn = psycopg2.connect(
        database=database,
        user=username,
        password=password
    )

    # Création d'un curseur pour exécuter les commandes SQL
    cursor = conn.cursor()

    try:
        # Ouverture du fichier de dump SQL
        with open(dump_file, 'r') as f:
            # Lecture du contenu du fichier
            sql_statements = f.read()

            # Exécution des commandes SQL
            cursor.execute(sql_statements)

        # Validation des modifications dans la base de données
        conn.commit()
        print("Le dump SQL a été exécuté avec succès.")

    except (Exception, psycopg2.DatabaseError) as error:
        # En cas d'erreur, annulation des modifications
        conn.rollback()
        print("Une erreur s'est produite lors de l'exécution du dump SQL :", error)

    finally:
        # Fermeture du curseur et de la connexion à la base de données
        cursor.close()
        conn.close()

# Exemple d'utilisation du script
if __name__ == '__main__':
    host = 'localhost'
    port = '5432'
    database = 'OMAJ_PRODUCTS'
    username = 'postgres'
    password = 'root'
    dump_file = './dump.sql'

    execute_sql_dump(host, port, database, username, password, dump_file)

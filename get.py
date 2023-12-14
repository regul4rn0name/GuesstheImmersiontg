import mysql.connector
from match_ids_module import match_ids
import matchdecode
fetched_id = []

def main():
    try:
        fetched_id.clear()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="matches",
           
        )

        mycursor = mydb.cursor()
        sql = "SELECT match_id FROM `Andrey`"

        mycursor.execute(sql)
        fetched_match_ids = mycursor.fetchall()

        # Extract match_ids from the fetched data and append them to the existing array
        match_ids.extend([match_id[0] for match_id in fetched_match_ids])
        fetched_id.extend([match_id[0] for match_id in fetched_match_ids])

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        mycursor.close()
        mydb.close()
if __name__ == '__main__':
     main()



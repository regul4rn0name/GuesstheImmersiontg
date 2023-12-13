import mysql.connector
from match_ids_module import match_ids  # Assuming match_ids is a list of values
from get import fetched_id


def main():
    try:
        print("Match IDs to be processed:")
        print(match_ids)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="matches",
            
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO `Andrey` (match_id) VALUES (%s)"

        # Assuming match_ids is a list of values
        # If match_ids is a list of tuples, use executemany

        for match_id in match_ids:
            if match_id != fetched_id :
                mycursor.execute(sql, (match_id,))

        mydb.commit()
        print("Records inserted successfully")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        mycursor.close()
        mydb.close()


if __name__ == "__main__":
    main()

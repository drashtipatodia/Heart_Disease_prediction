import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="app_user",   # better than root
        password="paa",
        database="churn_db",
        port=3306
    )

def save_prediction(data, pred):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        query = """
        INSERT INTO heart_predictions 
        (age, sex, cp, trestbps, chol, prediction)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            data["age"],
            data["sex"],
            data["cp"],
            data["trestbps"],
            data["chol"],
            pred
        )

        cursor.execute(query, values)
        conn.commit()

    except Exception as e:
        print("DB Error:", e)

    finally:
        cursor.close()
        conn.close()
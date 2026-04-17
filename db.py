import mysql.connector
import streamlit as st
# MYSQL CONNECTION
# -------------------------
def connect_db():
    return mysql.connector.connect(
        host=st.secrets["MYSQLHOST"],
        user=st.secrets["MYSQLUSER"],
        password=st.secrets["MYSQLPASSWORD"],
        database=st.secrets["MYSQLDATABASE"],
        port=int(st.secrets["MYSQLPORT"])
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

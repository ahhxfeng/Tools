#coding=utf-8

import mysql.connector

def do_sql(sql:str):
    """
    execute the sql 
    """
    
    conn = mysql.connector.connect(user="weave", password="weavewater", database="explorer0808", host="192.168.1.132", port=3306, auth_plugin='mysql_native_password')
    cursor = conn.cursor()
    cursor.execute(sql)
    values = cursor.fetchall()

    cursor.close()
    conn.close()

    return values
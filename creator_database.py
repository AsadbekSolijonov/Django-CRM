import logging
import mysql.connector

logging.basicConfig(format='%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s %(message)s]',
                    level=logging.INFO)

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
)

cursor = dataBase.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS dcrm_database;')

logging.info('Databse is created!')

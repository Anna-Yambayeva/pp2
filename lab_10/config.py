from configparser import ConfigParser

def load_config(filename='database.ini', section='postgresql'):
    return {
        'host': 'localhost',
        'database': 'snake',
        'user': 'postgres',
        'password': 'Fyyf1012',
        'port': '5432'
    }
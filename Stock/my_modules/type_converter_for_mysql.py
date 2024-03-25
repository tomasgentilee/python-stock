import datetime

def convert(data):
    
    if type(data) == bool:
        return "BOOLEAN"
    if type(data) == int:
        return "INTEGER"
    if type(data) == float:
        return "FLOAT"
    if type(data) == str:
        return "VARCHAR(50)"
    if type(data) == datetime.datetime:
        return "TIMESTAMP DEFAULT NULL"
    
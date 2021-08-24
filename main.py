import json
import requests


def call_table():
    r = requests.get('https://api.airtable.com/v0/apprs1kK3yiSRCQeX/MainTable?api_key=keyu4O4iQfg69w0iQ')
    data = r.json()["records"]
    l = [(el["fields"]["title"], el["fields"]["ID"]) for el in data]
    return [el[0] for el in sorted(l, key=lambda x: x[1])]


def say_hello_handler(event, context):
    if 'globalCursor' not in globals():
        global globalCursor
        globalCursor = 0
    table = call_table()
    table = table[globalCursor:] + table[:globalCursor]
    result = f"{table[0]}\n{table[1]}\n{table[2]}"
    globalCursor += 1
    if globalCursor == len(table):
        globalCursor = 0

    return {
        "statusCode": 200,
        "body": result,
    }


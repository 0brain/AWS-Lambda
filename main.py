import json
import requests


def say_hello_handler(event, context):
    r = requests.get('https://api.airtable.com/v0/apprs1kK3yiSRCQeX/MainTable?api_key=keyu4O4iQfg69w0iQ')
    data = r.json()["records"]
    l = [(el["fields"]["title"], el["fields"]["ID"]) for el in data]
    res = [el[0] for el in sorted(l, key=lambda x: x[1])]
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World')
    }, "<br>", res

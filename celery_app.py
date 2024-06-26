from celery import Celery
import requests
import json

# Assuming Redis is running in a Docker container and you're using docker-compose
app = Celery('tasks', broker='redis://redis:6379/0')


@app.task
def fetch_jsonplaceholder_data():
    urls = [
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
    ]
    data = {}
    for url in urls:
        response = requests.get(url)
        key = url.split('/')[-1]
        data[key] = response.json()

    with open('data.json', 'w') as f:
        json.dump(data, f)

    return "Data saved successfully!"

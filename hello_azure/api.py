

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .openai_kay import api_key
import requests

openai_secret_key = api_key

@api_view(['GET','POST'])
def chatgpt(request):
    if request.method == 'GET':
        message = request.GET['msg']
        print(message)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {openai_secret_key}'
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": message}],
            "temperature": 0.7
        }
        response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
        response_data = response.json()
        text = response_data["choices"][0]
        return Response({'text': text})
    
    message = request.POST['msg']
    print(message)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {openai_secret_key}'
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": message}],
        "temperature": 0.7
    }
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
    response_data = response.json()
    text = response_data["choices"][0]
    return Response({'text': text})

  
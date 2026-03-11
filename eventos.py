import requests
from requests import HTTPError


def user(username):

    try:
        url = requests.get(f"https://api.github.com/users/{username}/events")
        url.raise_for_status()
    except HTTPError as HTTPerr:
        print(f'HTTP erro: {HTTPerr}')
    except Exception as err:
        print("ERRO{err}")
    else:
        r = url.json()
        return r
        

def get_events(r):   
    
    lista_eventos = []
    for evento in r:

        usuario = evento['actor']['login']
        repositorio = evento['repo']['name']

        if evento['type'] == 'PushEvent':
            lista_eventos.append(f'Usuario {usuario} criou repositorio {repositorio}')
    print(lista_eventos)
       
    

get_events(user('vitoria174'))
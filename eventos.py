import requests
from requests import HTTPError
from rich import print

class Usuario:

    def __init__(self, username):
        self.username = username

    def validacao(self):
        try: 
            url = requests.get(f"https://api.github.com/users/{self.username}/events") #faz uma requisao de usuario da api do github
            url.raise_for_status() #verifica de o response gera um erro de 400 ao 500
            return url.json() #retorna o json da requisicao (url)
        
        except requests.exceptions.HTTPError as erro:
            print(f"[red]Usuario não encontrado [/red] {erro}")
            return None
        
        except Exception as erro:
            print(f"Erro: {erro}")
            return None
        
    def CommitEvent(self):
        cont = 0
        eventos = self.validacao()
        if not eventos:
             print("Usuario não encontrado")
             return
        
        for evento in eventos:
            if evento['type'] == "PushEvent":
                cont +=1
        print(f"Commit {cont} enviados.")

    def CreateEvent(self):
        ContEvent = 0
        event_create = self.validacao()
        
        for create in event_create:
            if create['type'] == 'CreateEvent':
                ContEvent += 1

        print(f"Foi criado {ContEvent} repositorio.")
    
    def DeleteEvent(self):
        DelEvent = 0
        delete = self.validacao()

        for delete in delete:
            if delete['type'] == 'DeleteEvent':
                DelEvent += 1
        print(f'{DelEvent} repositorio deletado.')
        
    def ForkEvent(self):
        Cont_Fork = 0
        fork_event = self.validacao()

        for fork in fork_event:
            if fork['type'] == 'ForkEvent':
                Cont_Fork += 1
        print(f'{Cont_Fork} fork no repositorio')
    
    def WatchEvent(self):
        Cont_Watch = 0
        watch_event = self.validacao()

        for watch in watch_event:
            if watch['type'] == 'WatchEvent':
                Cont_Watch += 1
        print(f"{Cont_Watch} :star: repositorio")


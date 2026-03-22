from rich.panel import Panel
from rich import print
from eventos import Usuario



def eventos(user):
        menu ="""
    [blue]
        1 - Commits
        2 - Create Events
        3 - Delete Events
        4 - Fork Events
        5 - Watch Event
    [/blue]
"""

        print(Panel(menu, title= "Conteudo", width=100))
        opcao= int(input("OPÇÃO: "))

        if opcao == 1:
            user.CommitEvent()
        
        elif opcao == 2:
             user.CreateEvent()

        elif opcao == 3:
            user.DeleteEvent()

        elif opcao == 4:
             user.ForkEvent()

def main():
    [blue]username= input("User Github: ")[/blue]
    user = Usuario(username)

    if user.validacao():
        eventos(user)

if __name__=="__main__":
    main()

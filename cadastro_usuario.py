import pyrebase


firebaseConfig = {'apiKey': "AIzaSyABR_FTVuyaguHtOtUk5lGG9pzz_STYHGw",
    'authDomain': "cadastro-usuario-login.firebaseapp.com",
    'projectId': "cadastro-usuario-login",
    'storageBucket': "cadastro-usuario-login.appspot.com",
    'messagingSenderId': "580682689328",
    'appId': "1:580682689328:web:2aa6be3825b87a93f7b6f5",
    'measurementId': "G-1LYMDQJYSZ",
    'databaseURL': ""}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

#tela inicial (menu)
def menu():
    menu = """
    ========== MENU ==========
    [1] CADASTRO DE USUÁRIO
    [2] LOGIN E SENHA
    [3] SAIR
    
    """
    return input(menu)

#opção 1 - cadastro de usuário
def cadastro_usuario():
    print("Cadastrando...teste")
    email = input("Informe seu e-mail: ")
    senha = input("Digite uma senha: ")
    try:
        user = auth.create_user_with_email_and_password(email, senha)
        print("Usuário cadastrado com sucesso!!")
        ask = input("Deseja Entrar em sua conta agora? [S / N]")
        if ask == 'S' or "s":
            login()
        
        else: 
            print("Nos veremos em breve!... Retornando para o 'MENU'.")
            menu()
    
    except:
        print("E-mail já cadastrado!!")    
#opção 2 - login usuário
def login():
    print("Logando...")
    email = input("Digite seu nome de Usuário:\n")
    senha = input("Digite sua senha: ")
    try:
        login = auth.sign_in_with_email_and_password(email, senha)
        print("Olá novamente!!")
    except:
        print("E-mail inválido...Tente novamente.")    
    
def main():
    
    while True:
        opcao = menu()
    
        if opcao == "1":
            cadastro_usuario()
        
        
        elif opcao == "2":
            login()
            
        elif opcao == "3":
            break
        
        else:
            print("Operação Inválida, por favor digite o número indicado no MENU")
    
main()


import pyrebase
import dotenv
import os
import stdiomask

dotenv.load_dotenv(dotenv.find_dotenv())

firebaseConfig = {'apiKey': os.getenv("apiKey"),
    'authDomain': os.getenv("authDomain"),
    'projectId': os.getenv("projectId"),
    'storageBucket': os.getenv("storageBucket"),
    'messagingSenderId': os.getenv("messagingSenderId"),
    'appId': os.getenv("appId"),
    'measurementId': os.getenv("measurementId"),
    'databaseURL': os.getenv("databaseURL") }
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
    print("Cadastrando...")
    email= input("Informe seu e-mail: ")
    senha = stdiomask.getpass(prompt = "Digite uma senha: ", mask='*')
    try:
        user = auth.create_user_with_email_and_password(email, senha)
        print("Usuário cadastrado com sucesso!!")
        ask = input("Deseja Entrar em sua conta agora? [S / N]")
        if ask == 'S' or ask == 's':
            login()
        
        else: 
            print("Nos veremos em breve!... Retornando para o 'MENU'.")
    
    except:
        print("E-mail já cadastrado!!...Cadastre um novo E-mail")    
#opção 2 - login usuário
def login():
    print("Logando...")
    email = input("Digite seu E-mail:\n")
    senha = stdiomask.getpass(prompt = "Digite uma senha: ", mask='*')
    try:
        login = auth.sign_in_with_email_and_password(email, senha)
        print("Olá, Seja bem-vindo!!")
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


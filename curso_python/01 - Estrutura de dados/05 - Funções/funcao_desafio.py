nome = input("Escreva seu nome aqui: ")
email = input("Escreva seu e-mail aqui: ")

def exibirmensagem(nome, email):
    print(f"Seja bem-vindo {nome}!, seu e-mail {email} já foi cadastrado no nosso sistema")

exibirmensagem(nome=nome, email=email)
texto = input("Informe um texto:")
VOGAIS = "AEIOU"

#exemplo utlizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")

else:
    print()
    print("Executa no final do laço")


#exemplo utlizando a função built in range
for numero in range(0, 51, 5):
    print(numero, end=" ")
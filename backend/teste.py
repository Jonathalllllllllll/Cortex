
from util import dobro;

print(dobro(5))

idade=75
if idade>=18:
    print("maior de idade")
else:
    print("menor de idade")

nome="Ajax"
print(f"Olá, {nome}! Você tem {idade} anos.")

linguagens=["PHP", "JS", "TS"]
usuario={"nome": "Joacir", "idade":20}

print(linguagens[2])
print(usuario["nome"])

maiusculas=[lang.upper() for lang in linguagens]
print(maiusculas)



def soma (a: int, b: int) -> int:
    return a+b
def saudacao(nome:str, idade: int=18) ->str:
    return f"{nome} tem {idade} anos"

print(soma(2,3))
print(saudacao("Joacir", 20))
print(saudacao("Ana")) #usa o default

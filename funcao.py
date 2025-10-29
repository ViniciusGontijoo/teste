def SomarNumeros(a,b):
    return a + b

resultado = SomarNumeros(4,2)
print(resultado)

def saudacao(nome="Visitante"):
    print(f"Olá, {nome} seja bem-vindo!")

saudacao()
saudacao("Vinícius")

for i in range(1,10):
    if i == 7 or i == 6:
        break
    print(i)

print("Deu bom d+++")
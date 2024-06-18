nCartao = input("Digite o numero do cartão\n")
deveDobrar = False
soma = 0

while (len(nCartao) != 16):
    nCartao = input("Atenção! Digite o numero do cartão com 16 digitos\n")

for digito in nCartao[::-1]:
    digito = int(digito)
    if(deveDobrar):
        digito *=2
        if(digito > 9): digito -= 9
    
    soma+=digito
    deveDobrar = not deveDobrar

if (soma % 10) == 0:
    print("Valido")
else:
    print("invalido")
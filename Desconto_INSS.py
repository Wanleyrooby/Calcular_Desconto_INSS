# EXERCÍCIO:

# Crie um script para calcular o desconto do INSS, de acordo com o salário informado
# pelo usuário, conforme a tabela de desconto abaixo:

# Salário                                      Desconto
# -------------------------------------------------------------
# Até R$ 1693,72                                  8%
# De R$ 1693,73 a R$ 2822,90                      9%
# De R$ 2822,91 a R$ 5645,80                     11%
# Acima de R$ 5645,80                O desconto é de R$ 621,04.


print("\n* * * MOSTRA O DESCONTO DO INSS! * * *\n")
def Calc_INSS():

    INSS = None
    salario = float(input("Qual o seu salario: "))

    if salario <= 1693.72:
        INSS = float(salario * 8 / 100)

    elif salario >= 1693.73 and salario <= 2822.90:
        INSS = float(salario * 9 / 100)

    elif salario >= 2822.91 and salario <= 5645.80:
        INSS = float(salario * 11 / 100)

    else:
        INSS = 621.04

    print("O desconto do INSS será de: \n", "%.2f"% INSS)

def Calc_Outro():
    resposta = input("Quer continuar ? (sim or não): ")
    resposta = resposta.upper()

    if resposta == "SIM":
        return True
    else:
        return False

Calc_INSS()

while Calc_Outro():
    Calc_INSS()

print("Obrigado!!!")
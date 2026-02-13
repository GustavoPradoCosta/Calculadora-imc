print ("===Calculadora de IMC===")

peso = float(input("Digite aqui seu peso em (kg): ").replace (",","."))
altura = float(input("Digite aqui sua altura em (m): ").replace (",","."))

imc = peso / (altura ** 2)

if imc < 18.5:
   Classificacao = "abaixo do peso"
elif 18.5 <= imc < 25:
    Classificacao = "peso normal"
elif 25 <= imc < 30:
    Classificacao = "acima do peso, risco à saúde"
elif 30 <= imc < 35:
    Classificacao = "obesidade nível I, risco à saúde"
elif 35 <= imc < 40:
    Classificacao = "obesidade nível II, risco à saúde"
else:
    Classificacao = "obesidade nível III, risco grave à saúde"

print (f"Classificação: {Classificacao}")

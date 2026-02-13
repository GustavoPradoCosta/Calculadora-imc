print ("==Calculadora de IMC==")

peso = float(input("Digite aqui seu peso em (kg): ").replace (",","."))
altura = float(input("Digite aqui sua altura em (m): ").replace (",","."))

imc = peso / (altura ** 2)

if imc < 18.5:
    print ("Classificação: abaixo do peso")
elif 18.5 <= imc < 25:
    print ("Classificação: peso normal")
elif 25 <= imc < 30:
    print ("Classificação: sobrepeso")
elif 30 <= imc < 35:
    print ("Classificação: obesidade grau I")
elif 35 <= imc < 40:
    print ("Classificação: obesidade grau II")
elif imc >= 40:
    print ("Classificação: obesidade grau III, risco grave de saúde")
else:
    print ("Insira apenas dados válidos")

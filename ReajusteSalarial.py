salario_atual = float(input("Digite o salario atual do colaborador: R$ "))

if salario_atual <= 280.00:
    percentual_aumento = 20
elif salario_atual <= 700.00:
    percentual_aumento = 15
elif salario_atual <= 1500.00:
    percentual_aumento = 10
else:
    percentual_aumento = 5

valor_aumento = salario_atual * percentual_aumento / 100
novo_salario = salario_atual + valor_aumento

inflacao = 3.8
aumento_real = valor_aumento - (salario_atual * inflacao / 100)

def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")

print(f"Salário antes do reajuste: {formatar_moeda(salario_atual)}")
print(f"Percentual de aumento aplicado: {percentual_aumento}%")
print(f"Valor do aumento: {formatar_moeda(valor_aumento)}")
print(f"Novo salário, após o aumento: {formatar_moeda(novo_salario)}")
print(f"Valor do aumento real, descontado a inflação: {formatar_moeda(aumento_real)}")
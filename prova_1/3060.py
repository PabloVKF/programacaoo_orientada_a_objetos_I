# Tento usar o ingles para me ajudar, pois acredito ser bastante importante para o nosso ramo.
# Também estou me acostumando a usar o type hints. Pois acredito ajudar na legibilidade e manutenibilidade do código.
purchase_value: int = int(input())
installments: int = int(input())

# Pego o valor da parcela base e a sobra, caso não sejá totalmente divisivel
installments_value_base: int = purchase_value // installments
rest_of_puechase: int = purchase_value % installments

for installment in range(installments):
    # Caso tenha sobrado algum valor não divisivel pelo numero de parcelas, ele sera distribuido aqui
    if rest_of_puechase > 0:
        installment_value = installments_value_base + 1
        rest_of_puechase -= 1
    else:
        installment_value = installments_value_base
    print(installment_value)

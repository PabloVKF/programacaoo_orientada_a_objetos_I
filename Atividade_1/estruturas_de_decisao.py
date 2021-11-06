def teste_de_selecao_1():
    entry = str(input()).split()

    A = int(entry[0])
    B = int(entry[1])
    C = int(entry[2])
    D = int(entry[3])

    condicao_1 = B > C
    condicao_2 = D > A
    condicao_3 = (C + D) > (A + B)
    condicao_4 = (A > 0) and (B > 0) and (C > 0) and (D > 0)
    condicao_5 = (A % 2) == 0

    if condicao_1 and condicao_2 and condicao_3 and condicao_4 and condicao_5:
        print("Valores aceitos")
    else:
        print("Valores nao aceitos")


def intervalo():
    value: float = float(input())

    if 0 <= value <= 25:
        print("Intervalo [0,25]")
    elif 25 < value <= 50:
        print("Intervalo (25,50]")
    elif 50 < value <= 75:
        print("Intervalo (50,75]")
    elif 75 < value <= 100:
        print("Intervalo (75,100]")
    else:
        print("Fora de intervalo")


def lanche():
    request = str(input()).split()
    food_code: str = str(request[0])
    amount_of_food: int = int(request[1])
    food_prices: dict = {
        '1': 4.00,
        '2': 4.50,
        '3': 5.00,
        '4': 2.00,
        '5': 1.50
    }

    food_price: float = food_prices[food_code]
    request_price: float = food_price * amount_of_food

    print(f"Total: R$ {request_price:.2f}")


def media_3():
    notas = str(input()).split()
    nota_1 = float(notas[0])
    nota_2 = float(notas[1])
    nota_3 = float(notas[2])
    nota_4 = float(notas[3])
    weight_nota_1: int = 2
    weight_nota_2: int = 3
    weight_nota_3: int = 4
    weight_nota_4: int = 1

    numerador: float = (nota_1 * weight_nota_1) + (nota_2 * weight_nota_2) + (nota_3 * weight_nota_3) + (nota_4 * weight_nota_4)
    denominador: int = weight_nota_1 + weight_nota_2 + weight_nota_3 + weight_nota_4
    average: float = numerador / denominador
    print(f"Media: {average:.1f}\n")

    min_to_aprovate: float = 7.0
    min_to_exam: float = 5.0
    if average >= min_to_aprovate:
        print("Aluno aprovado.")
    elif average < min_to_exam:
        print("Aluno reprovado.")
    elif min_to_exam <= average < min_to_aprovate:
        print("Aluno em exame.")
        nota_exam: float = float(input())
        print(f"Nota do exame: {nota_exam:.1f}")

        new_average: float = (average + nota_exam) / 2

        min_to_new_aprovate: float = 5.0
        if new_average >= min_to_new_aprovate:
            print("Aluno aprovado.")
        elif new_average < min_to_new_aprovate:
            print("Aluno reprovado.")

        print(f"Media final: {new_average:.1f}")




if __name__ == "__main__":
    media_3()

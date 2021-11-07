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
    print(f"Media: {average:.1f}")

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


def triangulo():
    entry = str(input()).split()
    A = float(entry[0])
    B = float(entry[1])
    C = float(entry[2])

    condition_1 = abs(B - C) < A < (B + C)
    condition_2 = abs(A - C) < B < (A + C)
    condition_3 = abs(A - B) < C < (A + B)

    if condition_1 and condition_2 and condition_3:
        perimetro = A + B + C
        print(f"Perimetro = {perimetro:.1f}")
    else:
        area = ((A + B) / 2) * C
        print(f"Area = {area:.1f}")


def multiplos():
    numbers = input().split()
    number_1 = int(numbers[0])
    number_2 = int(numbers[1])

    if (number_2 % number_1 == 0) or (number_1 % number_2 == 0):
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")


def animal():
    entry_1 = input()
    entry_2 = input()
    entry_3 = input()

    animals = {
        'vertebrado': {
            'ave': {
                'carnivoro': 'aguia',
                'onivoro': 'pomba'
            },
            'mamifero': {
                'onivoro': 'homem',
                'herbivoro': 'vaca'
            }
        },
        'invertebrado': {
            'inseto': {
                'hematofago': 'pulga',
                'herbivoro': 'lagarta'
            },
            'anelideo': {
                'hematofago': 'sanguessuga',
                'onivoro': 'minhoca'
            }
        }
    }

    result = animals[entry_1][entry_2][entry_3]
    print(result)


def qual_triangulo():
    # Considderando A e B como catetos e C como hipotenusa

    entry = str(input()).split()
    entry = [int(x) for x in entry]
    entry.sort()
    A, B, C = entry

    condition = abs(A - B) < C < (A + B)

    if condition:
        if A == B and B == C:
            triangle_type = "Valido-Equilatero"
        elif A == B or B == C:
            triangle_type = "Valido-Isoceles"
        else:
            triangle_type = "Valido-Escaleno"
        print(triangle_type)

        pitagoras_theorem = (A ** 2) + (B ** 2) == (C ** 2)
        if pitagoras_theorem:
            triangle_shape = "S"
        else:
            triangle_shape = "N"
        print(f"Retangulo: {triangle_shape}")
    else:
        print("Invalido")


def avioes_de_papel():
    pass


if __name__ == "__main__":
    avioes_de_papel()

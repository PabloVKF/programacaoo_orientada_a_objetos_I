from random import randrange


def notas_e_moedas():
    ramining_value: float = float(input())
    bill_types: list = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
    coins_types: list = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

    print("NOTAS:")
    for bill in bill_types:
        number_of_bill: int = int(ramining_value // bill)
        ramining_value %= bill
        print(f"{number_of_bill} nota(s) de R$ {bill:.2f}")

    print("MOEDAS:")
    for coin in coins_types:
        number_of_bill: int = int(ramining_value // coin)
        ramining_value %= coin
        print(f"{number_of_bill} moeda(s) de R$ {coin:.2f}")


def numeros_pares():
    for number in range(1, 101):
        is_even: bool = (number % 2) == 0
        if is_even:
            print(number)


def numeros_impares():
    max_number: int = int(input())

    for number in range(1, max_number + 1):
        is_odd: bool = (number % 2) != 0
        if is_odd:
            print(number)


def quadrado_de_pares():
    max_number: int = int(input())

    for number in range(1, max_number + 1):
        is_even: bool = (number % 2) == 0
        if is_even:
            print(f"{number}^2 = {number ** 2}")


def par_ou_impar():
    number_of_entrys: int = int(input())
    entrys_list: list = []

    for number in range(number_of_entrys):
        entry: int = int(input())
        entrys_list.append(entry)

    for entry in entrys_list:
        if entry == 0:
            print("NULL")
        else:
            int_type: str = ""
            if entry > 0:
                int_type: str = "POSITIVE"
            elif entry < 0:
                int_type: str = "NEGATIVE"

            if (entry % 2) == 0:
                print(f"EVEN {int_type}")
            elif (entry % 2) != 0:
                print(f"ODD {int_type}")


def resto_2():
    denominator: int = int(input())

    for number in range(1, 10001):
        left_two: bool = (number % denominator) == 2
        if left_two:
            print(number)


def tabuada():
    main_number: int = int(input())

    for number in range(1, 11):
        result: int = number * main_number
        print(f"{number} x {main_number} = {result}")


def maior_e_posicao():
    max_number: int = 0
    position_max_number: int = 0

    for position in range(100):
        number: int = int(input())
        if number > max_number:
            max_number = number
            position_max_number = position + 1

    print(max_number)
    print(position_max_number)


def dama():
    while True:
        entry = input().split()
        x1 = int(entry[0])
        y1 = int(entry[1])
        x2 = int(entry[2])
        y2 = int(entry[3])

        is_x1_equal_x2: bool = x1 == x2
        is_y1_equal_y2: bool = y1 == y2
        is_in_diagon: bool = abs(x2-x1) == abs(y2-y1)
        out_of_the_board: bool = (x1 < 1) or (y1 < 1) or (x2 < 1) or (y2 < 1) or (x1 > 8) or (y1 > 8) or (x2 > 8) or (y2 > 8)

        if out_of_the_board:
            break
        elif is_x1_equal_x2 and is_y1_equal_y2:
            print(0)
        elif is_x1_equal_x2 or is_y1_equal_y2 or is_in_diagon:
            print(1)
        else:
            print(2)


def soma_de_impares_consecutivos_ii():
    number_of_entrys: int = int(input())
    answers: list = []

    for z in range(number_of_entrys):
        entry: list = input().split()
        entry.sort()
        x: int = int(entry[0])
        y: int = int(entry[1])
        sum_of_odds: int = 0

        for number in range(x+1, y):
            number_is_odd: bool = (number % 2) != 0

            if number_is_odd:
                sum_of_odds += number

        answers.append(sum_of_odds)

    for answer in answers:
        print(answer)


def senha_fixa():
    correct_password: str = "2002"
    not_correct_password: bool = True

    while not_correct_password:
        password_attempt: str = input()

        if password_attempt == correct_password:
            print("Acesso Permitido")
            not_correct_password = False
        else:
            print("Senha Invalida")


def tipo_do_combustivel():
    not_end: bool = True
    products: dict = {
        "1": {"name_produtc": "Álcool", "points": 0},
        "2": {"name_produtc": "Gasolina", "points": 0},
        "3": {"name_produtc": "Diesel", "points": 0},
        "4": {"name_produtc": "Fim", "points": 0}
    }

    while not_end:
        favorite_product_code: str = input()
        out_of_range: bool = int(favorite_product_code) < 1 or int(favorite_product_code) > 4

        if out_of_range:
            continue
        elif products[favorite_product_code]["name_produtc"] == "Fim":
            alcool_points: int = products["1"]["points"]
            gasolina_points: int = products["2"]["points"]
            diesel_pints: int = products["3"]["points"]

            print("MUITO OBRIGADO\n"
                  f"Alcool: {alcool_points}\n"
                  f"Gasolina: {gasolina_points}\n"
                  f"Diesel: {diesel_pints}")
            not_end = False
        else:
            products[favorite_product_code]["points"] += 1


def primo_rapido():
    number_of_entrys: int = int(input())

    for z in range(number_of_entrys):
        number_entry: int = int(input())
        text_to_print: str = "Prime"

        for number in range(2, number_entry):
            is_divisible: bool = number_entry % number == 0
            if is_divisible:
                text_to_print = "Not Prime"
                break

        print(text_to_print)


def feynman():
    not_end: bool = True

    while not_end:
        square_dimension: int = int(input())
        total_squares: int = 0

        if square_dimension == 0:
            break
        else:
            for number in range(1, square_dimension + 1):
                total_squares += number ** 2
            print(total_squares)


def zerinho_ou_um():
    winner: dict = {
        0: "A",
        1: "B",
        2: "C"
    }

    while True:
        try:
            answers: list = input().split()

            for participant, answer in enumerate(answers):
                number_of_apparitions: int = answers.count(answer)

                if number_of_apparitions == len(answers):
                    print(answers)
                    print(len(answers))
                    print("*")
                    break
                elif number_of_apparitions == 1:
                    print(winner[participant])
                    break
                else:
                    continue
        except EOFError:
            break

from datetime import date
def natal_de_pedrinho():
    while True:
        try:
            christmas_date: date = date(2016, 12, 25)
            entry: list = input().split()
            month: int = int(entry[0])
            day: int = int(entry[1])
            entry_day: date = date(2016, month, day)

            if christmas_date < entry_day:
                delta_days = entry_day - christmas_date
                delta_days = -int(delta_days.days)
            else:
                delta_days = christmas_date - entry_day
                delta_days = int(delta_days.days)

            if delta_days == 0:
                print("E natal!")
            elif delta_days == 1:
                print("E vespera de natal!")
            elif delta_days > 1:
                print(f"Faltam {delta_days} dias para o natal!")
            elif delta_days < 0:
                print("Ja passou!")
        except EOFError:
            break


def bits_trocados():
    counter: int = 1
    while True:
        ramining_value: int = int(input())
        if ramining_value == 0:
            break
        bill_types: list = [50.00, 10.00, 5.00, 1.00]
        count_bill_types: list = []

        for bill in bill_types:
            number_of_bill: int = int(ramining_value // bill)
            ramining_value %= bill
            count_bill_types.append(number_of_bill)

        print(f"Teste {counter}\n"
              f"{count_bill_types[0]} {count_bill_types[1]} {count_bill_types[2]} {count_bill_types[3]}\n")
        counter += 1


def dobradura():
    while True:
        folds: int = int(input())
        if folds == -1:
            break
        else:
            q1 = 1
            q2 = 1
            q3 = 1
            q4 = 1

            for fold in range(folds):
                if (q1 + q2) < (q3 + q4):
                    q1 += q4
                    q2 += q3
                else:
                    q4 += q1
                    q3 += q2

                if (q1 + q4) < (q2 + q3):
                    q1 += q2
                    q4 += q3
                else:
                    q2 += q1
                    q3 += q4

            print(q1 + q2 + q3 + q4)


def cofrinhos_da_vo_vitoria():
    counter: int = 1
    while True:
        number_of_entrys: int = int(input())
        if number_of_entrys == 0:
            break

        difference: int = 0
        print(f"Teste {counter}")
        for number in range(number_of_entrys):
            coins_J, coins_Z = map(int, input().split())
            difference += coins_J - coins_Z
            print(difference)

        print()
        counter += 1


def garcom():
    number_of_deliveries: int = int(input())
    broken_glasses: int = 0
    for number in range(number_of_deliveries):
        cans, glasses = map(int, input().split())

        if glasses < cans:
            broken_glasses += glasses

    print(broken_glasses)


def tustin_e_seu_dado_novo():
    number_of_entrys: int = int(input())
    for number in range(number_of_entrys):
        face_1: int = int(input())
        face_2, face_3, face_4, face_5 = map(int, input().split())
        face_6: int = int(input())

        sum_of_faces_with_yuor_back_is_seven: bool = ((face_1 + face_6) == 7) and \
                                                     ((face_2 + face_4) == 7) and \
                                                     ((face_3 + face_5) == 7)

        all_faces_are_different_from_zero: bool = (face_1 > 0) and (face_2 > 0) and (face_3 > 0) and \
                                                  (face_4 > 0) and (face_5 > 0) and (face_6 > 0)

        if sum_of_faces_with_yuor_back_is_seven and all_faces_are_different_from_zero:
            print("SIM")
        else:
            print("NAO")


if __name__ == "__main__":
    tustin_e_seu_dado_novo()

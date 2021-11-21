from datetime import date


def quadrante():
    while True:
        x, y = map(int, input().split())

        if x == 0 or y == 0:
            break
        elif x > 0 and y > 0:
            print("primeiro")
        elif x < 0 and y > 0:
            print("segundo")
        elif x < 0 and y < 0:
            print("terceiro")
        elif x > 0 and y < 0:
            print("quarto")


def qual_o_mais_rapido():
    otavio_time, bruno_time, ian_time = map(float, input().split())

    if otavio_time < bruno_time and otavio_time < ian_time:
        print("Otavio")
    elif bruno_time < otavio_time and bruno_time < ian_time:
        print("Bruno")
    elif ian_time < otavio_time and ian_time < bruno_time:
        print("Ian")
    else:
        print("Empate")


def macaco_prego():
    counter_of_tests: int = 1
    while True:
        number_of_regions: int = int(input())

        if number_of_regions == 0:
            break
        else:
            x1, y1, u1, v1 = [-10000, 10000, 10000, -10000]
            has_intersection = True
            for region in range(number_of_regions):
                x2, y2, u2, v2 = map(int, input().split())

                letf_corner_is_in_the_region: bool = x1 <= x2 <= u1 and v1 <= y2 <= y1
                if letf_corner_is_in_the_region:
                    x1 = x2
                    y1 = y2

                right_corner_is_in_the_region: bool = x1 <= u2 <= u1 and v1 <= v2 <= y1
                if right_corner_is_in_the_region:
                    u1 = u2
                    v1 = v2

                if (not letf_corner_is_in_the_region) and (not right_corner_is_in_the_region):
                    has_intersection = False
                    break

            if has_intersection:
                print(f"Teste {counter_of_tests}\n"
                      f"{x1} {y1} {u1} {v1}\n")
            else:
                print(f"Teste {counter_of_tests}\n"
                      f"nenhum\n")

            counter_of_tests += 1


def bafo():
    counter_of_tests: int = 1
    while True:
        number_of_rounds: int = int(float(input()))

        if number_of_rounds == 0:
            break
        else:
            aldo_points: int = 0
            beto_points: int = 0
            for number in range(number_of_rounds):
                entry = input().split()
                aldo_points += int(entry[0])
                beto_points += int(entry[1])

            if aldo_points > beto_points:
                print(f"Teste {counter_of_tests}\n"
                      f"Aldo\n")
            elif beto_points > aldo_points:
                print(f"Teste {counter_of_tests}\n"
                      f"Beto\n")

            counter_of_tests += 1


def diferenca_entre_datas():
    entry_1 = input().split()
    date_1 = date(2021, int(entry_1[1]), int(entry_1[0]))
    entry_2 = input().split()
    date_2 = date(2021, int(entry_2[1]), int(entry_2[0]))

    delta_days = date_1 - date_2
    print(abs(delta_days.days))


def elevador():
    entry_1: list = input().split()
    number_of_readings: int = int(entry_1[0])
    elevator_capacity: int = int(entry_1[1])
    elevator: int = 0
    over_capacity: bool = False

    for number in range(number_of_readings):
        entry_2: list = input().split()
        people_who_left: int = int(entry_2[0])
        people_who_joined: int = int(entry_2[1])
        elevator += people_who_joined - people_who_left

        if elevator > elevator_capacity:
            over_capacity = True
            break

    if over_capacity:
        print("S")
    else:
        print("N")


def escada_rolante():
    number_of_people: int = int(input())
    last_time_on: int = 0
    time_on: int = 0

    for number in range(number_of_people):
        time_sensor: int = int(input())

        if time_sensor >= last_time_on:
            time_on += 10
        else:
            time_on += (time_sensor + 10) - last_time_on

        last_time_on = time_sensor + 10

    print(time_on)


def album_de_fotos():
    entry_1 = input().split()
    paper_dimensions: list = [int(entry_1[0]), int(entry_1[1])]
    entry_2 = input().split()
    photo_1_dimensions: list = [int(entry_2[0]), int(entry_2[1])]
    entry_3 = input().split()
    photo_2_dimensions: list = [int(entry_3[0]), int(entry_3[1])]
    squares = []

    if photo_1_dimensions[0] <= paper_dimensions[0] and photo_1_dimensions[1] <= paper_dimensions[1]:
        squares.append([
            (paper_dimensions[0] - photo_1_dimensions[0]),
            paper_dimensions[1]
        ])
        squares.append([
            paper_dimensions[0],
            (paper_dimensions[1] - photo_1_dimensions[1])
        ])

    if photo_1_dimensions[1] <= paper_dimensions[0] and photo_1_dimensions[0] <= paper_dimensions[1]:
        squares.append([
            (paper_dimensions[0] - photo_1_dimensions[1]),
            paper_dimensions[1]
        ])
        squares.append([
            paper_dimensions[0],
            (paper_dimensions[1] - photo_1_dimensions[0])
        ])

    photos_fit: bool = False
    for square in squares:
        fit_horizontal = photo_2_dimensions[0] <= square[0] and photo_2_dimensions[1] <= square[1]
        fit_vertically = photo_2_dimensions[1] <= square[0] and photo_2_dimensions[0] <= square[1]
        if fit_horizontal or fit_vertically:
            photos_fit = True
            break

    if photos_fit:
        print("S")
    else:
        print("N")


def chocolate():
    width_square: int = int(input())
    pieces: int = 1

    while True:
        if width_square >= 2:
            pieces *= 4
            width_square /= 2
        else:
            break

    print(pieces)




if __name__ == "__main__":
    chocolate()

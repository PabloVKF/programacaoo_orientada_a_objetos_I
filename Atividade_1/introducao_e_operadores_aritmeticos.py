import math
import datetime


def media_1():
    A = 5.0
    B = 7.1
    peso_A = 3.5
    peso_B = 7.5
    denominador = peso_A + peso_B

    media = ((A * peso_A) + (B * peso_B)) / denominador

    print("MEDIA = {:.5f}".format(media))


def media_2():
    A = float(input())
    B = float(input())
    C = float(input())
    peso_A = 2
    peso_B = 3
    peso_C = 5
    denominador = peso_A + peso_B + peso_C

    media = ((A * peso_A) + (B * peso_B) + (C * peso_C)) / denominador

    print(f"MEDIA = {media:.1f}")


def diferenca():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    
    result = (A * B) - (C * D)
    
    print(f"DIFERENCA = {result}")


def salario():
    employee_number = int(input())
    worked_hours = int(input())
    hourly_value = float(input())
    
    salary = worked_hours * hourly_value
    
    print(f"NUMBER = {employee_number}\n"
          f"SALARY = U$ {salary:.2f}")


def salario_com_bonus():
    seller_name = str(input())
    fixed_salary = float(input())
    total_sales = float(input())
    
    commission = total_sales * 0.15
    total_salary = fixed_salary + commission
    
    print(f"TOTAL = R$ {total_salary:.2f}")


def area():
    entry = str(input()).split()

    A = float(entry[0])
    B = float(entry[1])
    C = float(entry[2])
    pi = 3.14159

    triangle_area = (A * C) / 2
    circle_area = pi * (C ** 2)
    trapeze_area = ((A + B) / 2) * C
    square_area = B * B
    rectangle_area = A * B

    print(f"TRIANGULO: {triangle_area:.3f}\n"
          f"CIRCULO: {circle_area:.3f}\n"
          f"TRAPEZIO: {trapeze_area:.3f}\n"
          f"QUADRADO: {square_area:.3f}\n"
          f"RETANGULO: {rectangle_area:.3f}")


def consumo():
    total_km = int(input())
    total_fuel = float(input())

    consumption = total_km / total_fuel

    print(f"{consumption:.3f} km/l")


def distancia_entre_doi_pontos():
    point_1 = str(input()).split()
    point_2 = str(input()).split()
    x1 = float(point_1[0])
    y1 = float(point_1[1])
    x2 = float(point_2[0])
    y2 = float(point_2[1])

    distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

    print(f"{distance:.4f}")


def gasto_de_combustivel():
    time = int(input())
    avarege_of_km_per_hour = int(input())
    km_per_liter: int = 12

    km_traveled: int = time * avarege_of_km_per_hour
    liters_needed: float = km_traveled / km_per_liter

    print(f"{liters_needed:.3f}")


def conversao_de_tempo():
    total_seconds: int = int(input())
    hours_in_seconds: int = 3600
    minute_in_seconds: int = 60

    hours: int = total_seconds // hours_in_seconds
    seconds_remainning: int = total_seconds % hours_in_seconds
    minutes: int = seconds_remainning // minute_in_seconds
    seconds_remainning %= minute_in_seconds

    print(f"{hours}:{minutes}:{seconds_remainning}")


def idade_em_dias():
    total_days: int = int(input())
    days_in_year: int = 365
    days_in_month: int = 30

    years: int = total_days // days_in_year
    days_remainning: int = total_days % days_in_year
    months: int = days_remainning // days_in_month
    days_remainning %= days_in_month

    print(f"{years} ano(s)\n"
          f"{months} mes(es)\n"
          f"{days_remainning} dia(s)\n")


def poligonos_regulares_simples():
    entry = str(input()).split()
    number_of_sizes: int = int(entry[0])
    length_of_sizes: int = int(entry[1])

    perimeter: int = number_of_sizes * length_of_sizes

    print(f"{perimeter}")


def pneu():
    desired_pressure: int = int(input())
    current_pressure: int = int(input())

    difference: int = desired_pressure - current_pressure

    print(f"{difference}")


def transporte_de_conteineres():
    container_dimensions = str(input()).split()
    ship_dimensions = str(input()).split()

    container_width = int(container_dimensions[0])
    container_length = int(container_dimensions[1])
    container_height = int(container_dimensions[2])
    ship_width = int(ship_dimensions[0])
    ship_length = int(ship_dimensions[1])
    ship_height = int(ship_dimensions[2])

    containers_per_width: int = ship_width // container_width
    containers_per_length: int = ship_length // container_length
    containers_per_height: int = ship_height // container_height
    ship_capacity: int = containers_per_width * containers_per_length * containers_per_height

    print(f"{ship_capacity}")


def bucca_na_inernet():
    third_link_entries: int = int(input())
    coefficient_third_to_second_link: float = 2.0
    coefficient_second_to_first_link: float = 2.0

    entries_on_second_link: float = third_link_entries * coefficient_third_to_second_link
    entries_on_first_link: float = entries_on_second_link * coefficient_second_to_first_link

    print(f"{entries_on_first_link:.0f}")


if __name__ == "__main__":
    bucca_na_inernet()

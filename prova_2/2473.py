flav_numbers: list = input().split()
drawn_numbers: list = input().split()
matchs: int = 0
table: dict = {
    0: "azar",
    1: "azar",
    2: "azar",
    3: "terno",
    4: "quadra",
    5: "quina",
    6: "sena"
}
# itera sobre os numeros do Flavio verificando se estao na lista de numeros soteados.
for numbers in flav_numbers:
    if numbers in drawn_numbers:
        matchs += 1

print(table[matchs])

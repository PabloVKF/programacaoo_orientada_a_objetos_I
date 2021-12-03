# Tanto nesse quanto em outros exercicio vou input().split() e distribuir as variaveis uma a uma.
# Pois mesmo gostando de usar o map(), notei que ele aumenta muito o tempo de processamento.
# Tento usar o ingles para me ajudar, pois acredito ser bastante importante para o nosso ramo.
# Também estou me acostumando a usar o type hints. Pois acredito ajudar na legibilidade e manutenibilidade do código.
entry: list = input().split()
N: int = int(entry[0])
M: int = int(entry[1])

# Optei por desenvolver essa função pois o processo para cada numero seria o mesmo
def clouser_prime_number(x: int) -> int:
    # O primeiro for chama o outro for entregando de X até 1
    for number in range(x, 0, -1):
        is_prime: bool = True
        # Já nesse sugundo for é onde ocorre a vwerificação se cada numero do for anterio é primeo
        for subnumber in range(2, number):
            # Caso não sejá primo, essa informação é passada pra variavel e para o segundo for
            if (number % subnumber) == 0:
                is_prime = False
                break

        # Caso se ache um numero primo é retornado
        if is_prime:
            return number


p1 = clouser_prime_number(N)
p2 = clouser_prime_number(M)

print(p1 * p2)

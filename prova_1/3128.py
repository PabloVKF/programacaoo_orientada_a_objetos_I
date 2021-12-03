# Tento usar o ingles para me ajudar, pois acredito ser bastante importante para o nosso ramo.
# Também estou me acostumando a usar o type hints. Pois acredito ajudar na legibilidade e manutenibilidade do código.
client_age_1: int = int(input())
client_age_2: int = int(input())
free_access: bool = True

# Verifica se tem algumcliente com idade inferior a 6
very_young: bool = client_age_1 < 6 or client_age_2 < 6

# Verifica se o cliente mais novo tem a idade inferior a 14 e se o cliente mais velho é um adulto (>18anos) o
# acompanhando
unaccompanied_underage: bool = min(client_age_1, client_age_2) < 14 and max(client_age_1, client_age_2) < 18

# Caso alguma das infrações tenha ocorrido, o acesso é negado
if very_young or unaccompanied_underage:
    free_access = False

if free_access:
    print("YES")
else:
    print("NO")

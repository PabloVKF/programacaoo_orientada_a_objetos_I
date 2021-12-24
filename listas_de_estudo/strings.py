def revisao_do_contrato():
    while True:
        problematic_number, contract_price = input().split()
        end_test: bool = (int(problematic_number) == 0) and (int(contract_price) == 0)
        if end_test:
            break

        wrong_price: list = [letter for letter in contract_price if letter != problematic_number]
        if wrong_price:
            final_value: int = int("".join(wrong_price))
        else:
            final_value: int = 0
        print(final_value)


def flores_florecem_da_franca():
    while True:
        entry: list = input().split()
        end_test: bool = entry[0] == "*"
        if end_test:
            break

        poem: list = list(map(lambda x: x.lower(), entry))
        first_letter = poem[0][0]
        is_tautogram: bool = True

        for word in poem:
            starts_correctly: bool = word.startswith(first_letter)
            if not starts_correctly:
                is_tautogram = False
                break

        if is_tautogram:
            print("Y")
        else:
            print("N")


def led():
    number_of_entrys: int = int(input())
    leds_per_number: dict = {
        "0": 6,
        "1": 2,
        "2": 5,
        "3": 5,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 3,
        "8": 7,
        "9": 6
    }

    for i in range(number_of_entrys):
        value: str = input()
        required_leds: int = 0

        for letter in value:
            leds: int = leds_per_number[letter]
            required_leds += leds

        print(f"{required_leds} leds")


def wertyu():
    decoder: dict = {
        "1": "`",
        "2": "1",
        "3": "2",
        "4": "3",
        "5": "4",
        "6": "5",
        "7": "6",
        "8": "7",
        "9": "8",
        "0": "9",
        "-": "0",
        "=": "-",
        "W": "Q",
        "E": "W",
        "R": "E",
        "T": "R",
        "Y": "T",
        "U": "Y",
        "I": "U",
        "O": "I",
        "P": "O",
        "[": "P",
        "]": "[",
        "\\": "]",
        "S": "A",
        "D": "S",
        "F": "D",
        "G": "F",
        "H": "G",
        "J": "H",
        "K": "J",
        "L": "K",
        ";": "L",
        "'": ";",
        "X": "Z",
        "C": "X",
        "V": "C",
        "B": "V",
        "N": "B",
        "M": "N",
        ",": "M",
        ".": ",",
        "/": ".",
        " ": " "
    }
    while True:
        try:
            coded_phrase: list = list(input())
            uncoded_phrase: str = ''

            for character in coded_phrase:
                decoded: str = decoder[character]
                uncoded_phrase += decoded

            print(uncoded_phrase)
        except EOFError:
            break


def combinador():
    number_of_tests: int = int(input())
    for number in range(number_of_tests):
        word_result = ''
        first_word, second_word = input().split()

        for index in range(max(len(first_word), len(second_word))):
            if index < len(first_word):
                word_result += first_word[index]
            if index < len(second_word):
                word_result += second_word[index]

        print(word_result)


def botas_perdidas():
    while True:
        try:
            number_of_entrys: int = int(input())
            left_boots: list = []
            right_boots: list = []
            total_boots: int = 0

            for number in range(number_of_entrys):
                boot, side = input().split()
                if side == "E":
                    try:
                        right_boots.remove(boot)
                        total_boots += 1
                    except ValueError:
                        left_boots.append(boot)
                else:
                    try:
                        left_boots.remove(boot)
                        total_boots += 1
                    except ValueError:
                        right_boots.append(boot)

            print(total_boots)
        except EOFError:
            break


def relogio_binario():
    while True:
        try:
            hours, minutes = map(int, input().split(":"))

            hour_divider: list = [8, 4, 2, 1]
            hour_result: list = []
            rest: int = hours
            for divider in hour_divider:
                if rest >= divider:
                    hour_result.append("o")
                    rest = rest % divider
                else:
                    hour_result.append(" ")

            min_divider: list = [32, 16, 8, 4, 2, 1]
            min_result: list = []
            rest: int = minutes
            for divider in min_divider:
                if rest >= divider:
                    min_result.append("o")
                    rest = rest % divider
                else:
                    min_result.append(" ")

            print(f" ____________________________________________")
            print(f"|                                            |")
            print(f"|    ____________________________________    |_")
            print(f"|   |                                    |   |_)")
            print(f"|   |   8         4         2         1  |   |")
            print(f"|   |                                    |   |")
            print(f"|   |   {hour_result[0]}         {hour_result[1]}         {hour_result[2]}         {hour_result[3]}  |   |")
            print(f"|   |                                    |   |")
            print(f"|   |                                    |   |")
            print(f"|   |   {min_result[0]}     {min_result[1]}     {min_result[2]}     {min_result[3]}     {min_result[4]}     {min_result[5]}  |   |")
            print(f"|   |                                    |   |")
            print(f"|   |   32    16    8     4     2     1  |   |_")
            print(f"|   |____________________________________|   |_)")
            print(f"|                                            |")
            print(f"|____________________________________________|")
            print()

        except EOFError:
            break


def deli_deli():
    irregular_words_number, total_words = map(int, input().split())
    word_ends_with: list = ["o", "s", "ch", "sh", "x"]
    vowels: list = ["a", "e", "i", "o", "u"]
    irregular_words: list = []
    plu_irregular_words: list = []

    for number in range(irregular_words_number):
        irregular, plural = input().split()
        irregular_words.append(irregular)
        plu_irregular_words.append(plural)

    for number in range(total_words):
        word: str = input()
        if word in irregular_words:
            index: int = irregular_words.index(word)
            word = plu_irregular_words[index]
            print(word)
        elif (word[-1] == "y") and (word[-2].lower() not in vowels):
            word = word[:-1] + "ies"
            print(word)
        elif word[-1] in word_ends_with:
            word += "es"
            print(word)
        elif word[-2:] in word_ends_with:
            word += "es"
            print(word)
        else:
            word += "s"
            print(word)


def perdido_em_marte():
    unnecessary_entry: str = input()
    hex_letters: list = input().split()

    for hexadecimal in hex_letters:
        bytes_letter: bytes = bytes.fromhex(hexadecimal)
        ascii_letter: str = bytes_letter.decode("ASCII")
        print(ascii_letter, end='')

    print()


def nome_no_formulario():
    texte: str = input()
    limit: int = 80

    if len(texte) > limit:
        print("NO")
    else:
        print("YES")


def banco_imobiliario():
    money, number_of_transations = map(int, input().split())
    players: dict = {
        "D": money,
        "E": money,
        "F": money
    }

    for number in range(number_of_transations):
        transations = input().split()
        type_tran: str = transations[0]
        player: str = transations[1]

        if type_tran == "C":
            value: int = int(transations[2])
            players[player] -= value
        elif type_tran == "V":
            value: int = int(transations[2])
            players[player] += value
        elif type_tran == "A":
            player_2: str = transations[2]
            value: int = int(transations[3])
            players[player] += value
            players[player_2] -= value

    print(f"{players['D']} {players['E']} {players['F']}")


def lingua_do_P():
    coded_sentence: str = input()
    decoded_sentence: str = ""

    contador: int = 0
    while contador < len(coded_sentence):
        letter = coded_sentence[contador]
        if letter == "p":
            decoded_sentence += coded_sentence[contador + 1]
            contador += 2
        else:
            decoded_sentence += coded_sentence[contador]
            contador += 1

    print(decoded_sentence)


def letras():
    letter: str = input()
    text: list = input().split()
    number_of_words: int = len(text)
    occurrences: int = 0

    for word in text:
        if letter in word:
            occurrences += 1

    percentage_of_occurrrence: float = (occurrences / number_of_words) * 100
    print(f"{percentage_of_occurrrence:.1f}")


def nova_senha_ra():
    number_of_passwords: int = int(input())
    logic: list = [
        ("GQaku", "0"),
        ("ISblv", "1"),
        ("EOYcmw", "2"),
        ("FPZdnx", "3"),
        ("JTeoy", "4"),
        ("DNXfpz", "5"),
        ("AKUgq", "6"),
        ("CMWhr", "7"),
        ("BLVis", "8"),
        ("HRjt", "9")
    ]

    for number in range(number_of_passwords):
        old_password: str = input()
        new_password: str = ''

        for letter in old_password:

            for letter_set, number in logic:
                if letter in letter_set:
                    new_password += number
                    break

            if len(new_password) == 12:
                break
        print(new_password)


def evitando_chuva():
    number_of_days: int = int(input())
    umbrella_home: int = 0
    umbrella_work: int = 0
    home_stock: int = 0
    work_stock: int = 0

    for number in range(number_of_days):
        home, work = input().split()
        if home == "chuva":
            if home_stock:
                home_stock -= 1
                work_stock += 1
            else:
                umbrella_home += 1
                work_stock += 1
        if work == "chuva":
            if work_stock:
                work_stock -= 1
                home_stock += 1
            else:
                umbrella_work += 1
                home_stock += 1

    print(umbrella_home, umbrella_work)


def lexico():
    word_1: str = input()
    word_2: str = input()
    ordered_words: list = sorted([word_1, word_2])

    for word in ordered_words:
        print(word)


def criptotexto():
    number_of_tests: int = int(input())

    for number in range(number_of_tests):
        encrypted_word: list = list(input())
        encrypted_word.reverse()
        decrypted_word: str = ""

        for letter in encrypted_word:
            if letter.islower():
                decrypted_word += letter

        print(decrypted_word)


def frase_binaria():
    while True:
        try:
            number_of_tests: int = int(input())
            word: str = ""

            for number in range(number_of_tests):
                decimal: int = int(input(), base=2)
                ascii_letter: str = chr(decimal)
                word += ascii_letter

            print(word)
        except EOFError:
            break


if __name__ == "__main__":
    frase_binaria()

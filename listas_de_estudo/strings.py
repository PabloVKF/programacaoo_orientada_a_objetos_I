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


if __name__ == "__main__":
    botas_perdidas()

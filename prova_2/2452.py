length, drops_number = map(int, input().split())
drop_positions: list = list(map(int, input().split()))
necessary_days: int = 0

# Crio um array de Zeros e uns representando a amostra
sample: list = []
for number in range(1, length + 1):
    if number in drop_positions:
        sample.append(1)
    else:
        sample.append(0)

# Simulo o passar dos dias até que a amostra se complete (só tenha 1)
have_white_space: bool = 0 != sample.count(0)
while have_white_space:
    current_sample = sample.copy()
    for index, result in enumerate(current_sample):
        if result:
            if index > 0:
                previous_index = index - 1
                sample[previous_index] = 1

            if index < len(sample) - 1:
                next_index = index + 1
                sample[next_index] = 1

    necessary_days += 1
    have_white_space: bool = 0 != sample.count(0)

print(necessary_days)


import math

# all in uF
CAP_VALUES = [
    1000,
    680,
    470,
    330,
    220,
    100,
    47,
    33,
    22,
    10,
    4.7,
    3.3,
    2.2,
    1,
    0.1,
    0.22,
    0.47,
    0.02,
    0.001,
    0.0001,
    0.00001,
]

# limits to prevent printing ridiculous component values
UF_LIMIT_LOW = 0.001
UF_LIMIT_HIGH = 300

PF_LIMIT_LOW = 10
PF_LIMIT_HIGH = 1000

calculate_r = lambda c, f: 1 / (2 * math.pi * (c * 10 ** -6) * f)
uF_to_pF = lambda c: c * (10 ** 6)


def print_component_table(*, freq):
    print(f"cutoff frequency set at: {freq} Hz")
    template = "{0:8}\t{1:8}\t{2:8}\t{3:8}"

    print("-" * 60)
    print(template.format("c (uF)", "c (pF)", "r(k ohms)", "r(ohms)"))
    print("-" * 60)

    for c in CAP_VALUES:
        r = calculate_r(c, freq)
        c_in_pF = uF_to_pF(c)

        # apply limits
        if c_in_pF > PF_LIMIT_HIGH or c_in_pF < PF_LIMIT_LOW:
            c_in_pF = "-"
        else:
            c_in_pF = round(c_in_pF, 4)

        if c > UF_LIMIT_HIGH or c < UF_LIMIT_LOW:
            c = "-"

        # TODO: choose an R thats reasonable from a component list that gets us around 10% tolerance
        print(template.format(c, c_in_pF, round(r / 1000, 4), round(r, 0)))


def run():
    multiplier = 1
    cutoff_freq = input("freq> ")
    try:
        if cutoff_freq[-1] == "k":
            multiplier = 1000
            cutoff_freq = cutoff_freq[:-1]

        cutoff_freq = int(cutoff_freq) * multiplier
    except ValueError:
        print("invalid freq, try again.")
        run()

    print_component_table(freq=cutoff_freq)


if __name__ == "__main__":
    run()

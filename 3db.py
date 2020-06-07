import math

# all in uF
CAP_VALUES = [
    220,
    4.7,
    2.2,
    1,
    0.02,
    0.001,
    0.0001,
    0.00001
]

PF_LIMIT = 200

calculate_r = lambda c, f: 1/(2*math.pi*(c*10**-6)*f)
uF_to_pF = lambda c: c*(10**6)

def print_component_table(*, freq):
    print(f"cutoff frequency set at: {freq} Hz")
    template = "{0:8}\t{1:8}\t{2:8}\t{3:8}"

    print('-'*60)
    print(template.format("c (uF)","c (pF)", "r(k ohms)","r(ohms)"))
    print('-'*60)

    for c in CAP_VALUES:
        r = calculate_r(c, freq)

        c_in_pF = uF_to_pF(c)
        if c_in_pF > PF_LIMIT:
            c_in_pF = '-'
        else:
            c_in_pF = round(c_in_pF, 4)
            
        print(template.format(c, c_in_pF, round(r/1000, 4), round(r, 0)))




def run():
    multiplier = 1
    cutoff_freq = input('freq> ')
    try:
        if cutoff_freq[-1] == 'k':
            multiplier = 1000
            cutoff_freq = cutoff_freq[:-1]

        cutoff_freq = int(cutoff_freq) * multiplier
    except ValueError:
        print("invalid freq, try again.")
        run()
    
    print_component_table(freq=cutoff_freq)


if __name__ == '__main__': run()
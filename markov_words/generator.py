import random

from .data import data

def main():
    return ''.join((chr(c + 97) for c in generate()))

def generate():
    text = decompose(init_markov())[1:]
    while True:
        # print(''.join((chr(c + 97) for c in text)))
        sig, r = row(text[-2], text[-1])
        if sig > 0:
            next = markov(r, sig)
            if next < 26:
                text.append(next)
            else:
                return text
        else:
            return text

def init_markov():
    offset = compose(26, 0, 0)
    return markov(data[offset:], rows[-1]) + offset

def markov(dat, sig):
    i = -1
    s = 0
    target = random.randint(1, sig)
    # print(target, sig, dat)
    while s < target:
        i += 1
        s += dat[i]
    return i

def compose(i, j, k):
    return (27 * i + j) * 26 + k

def decompose(num):
    i, rem = divmod(num, 27 * 26)
    j, k = divmod(rem, 26)
    return [i, j, k]

def row(i, j):
    index = 26 * i + j
    sig = rows[index]
    index *= 27
    return sig, data[index:index + 27]

rows = [0] * (26 * 26 + 1)

for i, d in enumerate(data):
    r = i / 27
    if r >= len(rows):
        # layer 1, not really a row
        rows[-1] += d
    else:
        # actual row
        rows[r] += d

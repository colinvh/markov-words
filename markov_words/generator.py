import random

def generate():
    return MarkovGenerator().generate()

class MarkovGenerator(object):
    def __init__(self, data=None, random=random):
        if data is None:
            from .data import data
        self.data = data
        self.random = random

    def generate(self):
        text = decompose(self.init_markov())[1:]
        while True:
            # print(''.join((chr(c + 97) for c in text)))
            r = row(self.data, text[-2], text[-1])
            next = self.markov(r)
            if next < 26:
                text.append(next)
            else:
                return ''.join((chr(c + 97) for c in text))

    def init_markov(self):
        offset = compose(26, 0, 0)
        return self.markov(self.data[offset:]) + offset

    def markov(self, dat):
        i = -1
        s = 0
        target = self.random.randint(1, sum(dat))
        while s < target:
            i += 1
            s += dat[i]
        return i

def compose(i, j, k):
    return (26 * i + j) * 27 + k

def decompose(num):
    i, rem = divmod(num, 27 * 26)
    j, k = divmod(rem, 27)
    return [i, j, k]

def row(data, i, j):
    index = 26 * i + j
    index *= 27
    return data[index:index + 27]

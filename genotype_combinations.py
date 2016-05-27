TETHA = 0.3
class Allele:
    def __init__(self, locus = "W", length = -1, freq = 1):
        self.locus = locus
        self.length = length
        self.freq = freq

    def is_equal(self, right):
        return self.locus == right.locus and self.length == right.length and self.freq == right.freq

class Genotypes:
    def __init__(self, distinct_alleles):
        self.alleles = distinct_alleles
        self.allele_comb = self.generate_allele_pairs()
        self.freqs = self.generate_freqs()

    def generate_freqs(self):
        tmp = []
        for i in range(0, len(self.alleles)):
            for j in range(i, len(self.alleles)):
                if (i == j):
                    tmp.append(self.calc_hom(self.alleles[i]))
                else:
                    tmp.append(self.calc_het(self.alleles[i], self.alleles[j]))
        return tmp

    def generate_allele_pairs(self):
        tmp = []
        for i in range(0, len(self.alleles)):
            for j in range(i, len(self.alleles)):
                tmp.append((self.alleles[i], self.alleles[j]))
        return tmp

    def calc_hom(self, a):
        return a.freq * a.freq + a.freq * TETHA * (1 - a.freq)

    def calc_het(self, a, b):
        return 2 * a.freq * b.freq

class Person:
    def __init__(self, a = Allele(), b = Allele()):
        self.a = a
        self.b = b
        self.freq = self.generate_freq()
        self.hom = True
        self.het = False
        if self.a.is_equal(self.b):
            self.hom = True
            self.het = False
        else:
            self.hom = False
            self.het = True

    def generate_freq(self):
        tmp = 0
        if self.a.is_equal(self.b):
            tmp = self.calc_hom(self.a)
        else:
            tmp = self.calc_het(self.a, self.b)
        return tmp

    def calc_hom(self, a):
        return a.freq * a.freq + a.freq * TETHA * (1 - a.freq)

    def calc_het(self, a, b):
        return 2 * a.freq * b.freq

    def is_equal(self, right):
        return self.a.is_equal(right.a) and self.b.is_equal(right.b) and self.freq == right.freq and self.hom == right.hom and self.het == right.het

    def is_less_than(self, right):
        if self.a.is_equal(right.a):
            return self.b.length < right.b.length
        else:
            return self.a.length < right.a.length;

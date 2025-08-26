class DonThuc:
    def __init__(self, he_so=0, so_mu=0):
        self.he_so = he_so
        self.so_mu = so_mu

    def dao_ham(self):
        return DonThuc(self.he_so * self.so_mu, self.so_mu - 1)

    def __str__(self):
        if self.he_so == 0:
            return ''
        s = ''
        abs_hs = abs(self.he_so)
        if self.so_mu != 0:
            if abs_hs == 1:
                s += 'x'
            else:
                s += f'{abs_hs}x'
            if self.so_mu > 1:
                s += f'^{self.so_mu}'
        else:
            s += f'{abs_hs}'
        return s

class DaThuc:
    def __init__(self, bac=0, gia_tri=None):
        self.bac = bac
        self.gia_tri = gia_tri if gia_tri is not None else [DonThuc() for _ in range(101)]

    @staticmethod
    def nhap():
        bac = int(input())
        gia_tri = [DonThuc() for _ in range(101)]
        for i in range(bac, -1, -1):
            he_so = int(input())
            gia_tri[i] = DonThuc(he_so, i)
        return DaThuc(bac, gia_tri)

    def dao_ham_cap_mot(self):
        res = DaThuc(self.bac - 1)
        for i in range(res.bac, -1, -1):
            res.gia_tri[i] = self.gia_tri[i+1].dao_ham()
        return res

    def dao_ham_cap_hai(self):
        return self.dao_ham_cap_mot().dao_ham_cap_mot()

    def check(self):
        return sum(self.gia_tri[i].he_so for i in range(self.bac, -1, -1))

    def __str__(self):
        s = ''
        check = False
        for i in range(self.bac, -1, -1):
            he_so = self.gia_tri[i].he_so
            if he_so == 0:
                continue
            if check and he_so > 0:
                s += '+'
            if he_so < 0:
                s += '-'
            s += str(self.gia_tri[i])
            check = True
        return s if s else '0'

def main():
    a = DaThuc.nhap()
    print(a)
    b = a.dao_ham_cap_mot()
    c = a.dao_ham_cap_hai()
    print(b if b.check() != 0 else 0)
    print(c if c.check() != 0 else 0)

if __name__ == "__main__":
    main()

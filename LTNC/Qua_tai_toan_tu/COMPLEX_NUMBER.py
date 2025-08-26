import sys, math

class SoPhuc:
    __slots__ = ("thuc", "ao")
    def __init__(self, thuc=0, ao=0):
        self.thuc = thuc
        self.ao = ao

    def modun(self):
        return math.sqrt(self.thuc * self.thuc + self.ao * self.ao)

    def __add__(self, other):
        return SoPhuc(self.thuc + other.thuc, self.ao + other.ao)

    def __sub__(self, other):
        return SoPhuc(self.thuc - other.thuc, self.ao - other.ao)

    def __str__(self):
        s = "{"
        if self.thuc != 0:
            s += str(self.thuc)
        if self.ao != 0:
            if self.ao > 0 and self.thuc != 0:
                s += "+"
            if self.ao < 0:
                s += "-"
            if abs(self.ao) != 1:
                s += str(abs(self.ao))
            s += "i"
        s += "}"
        return s

class DaySoPhuc:
    def __init__(self):
        self.values = []

    def tinhTong(self):
        if not self.values:
            return SoPhuc()
        res = self.values[0]
        for sp in self.values[1:]:
            res = res + sp
        return res

    def tinhHieu(self):
        if not self.values:
            return SoPhuc()
        res = self.values[0]
        for sp in self.values[1:]:
            res = res - sp
        return res

    def tinhModun(self):
        return [f"{v.modun():.2f}" for v in self.values]

def read_input():
    tokens = sys.stdin.read().strip().split()
    arr = DaySoPhuc()
    for i in range(0, len(tokens), 2):
        if i + 1 < len(tokens):
            thuc = int(tokens[i])
            ao = int(tokens[i + 1])
            arr.values.append(SoPhuc(thuc, ao))
    return arr

def main():
    ds = read_input()
    # Dòng 1: các số phức (mỗi cái kèm khoảng trắng, kể cả cuối dòng)
    print("".join(str(sp) + " " for sp in ds.values))
    # Dòng 2: các mô-đun (2 chữ số thập phân, khoảng trắng cuối)
    print("".join(m + " " for m in ds.tinhModun()))
    # Dòng 3: tổng (không thêm newline sau cùng để sát với C++ hành vi)
    sys.stdout.write(str(ds.tinhTong()))

if __name__ == "__main__":
    main()
'''
Số “tương lai” là số có các ước (không kể 1 và chính nó) là các số nguyên tố. VD: số 10 có ước là 2 và 5 là các số nguyên tố nên 10 là số “tương lai”.
Cho dãy số nguyên a1, a2, ..., an. Hãy cho biết trong dãy trên có bao nhiêu số tương lai.
Input:
Dòng thứ nhất chứa số nguyên dương n.
Dòng thứ hai chứa n số nguyên a1, a2, ..., an.
Output:
Một số nguyên dương là số lượng các số tương lai.
Ví dụ:
Input
9
9 7 10 6 17 4 19 21 13
Output
5

'''
n = int(input().strip())
arr = list(map(int, input().split()))

def is_future(x):
    if x < 4:  # 1,2,3 không tính
        return False
    factors = []
    tmp = x
    d = 2
    while d * d <= tmp:
        if tmp % d == 0:
            exp = 0
            while tmp % d == 0:
                tmp //= d
                exp += 1
            factors.append((d, exp))
            if len(factors) > 2: 
                return False
            if exp >= 3:  
                return False
        d += 1 if d == 2 else 2
        if len(factors) > 2:
            return False
    if tmp > 1:
        factors.append((tmp, 1))

    if len(factors) == 1 and factors[0][1] == 2:
        return True
    if len(factors) == 2 and factors[0][1] == 1 and factors[1][1] == 1:
        return True
    return False

print(sum(1 for x in arr[:n] if is_future(x)))

'''
Viết chương trình xuất ra n số tự nhiên đầu tiên (n>0) thỏa điều kiện: Các số này chia hết cho các số từ 1 đến 10. Kết quả cho ra là các số cách nhau 1 khoảng trắng. VD:
Input: 3
Output:  2520 5040 7560

'''
n = int(input().strip())
lcm_1_10 = 2520  # BCNN các số 1..10
result = [str(lcm_1_10 * i) for i in range(1, n + 1)]
print(" ".join(result))
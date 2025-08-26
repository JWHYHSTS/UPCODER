'''
Mảng Ngày Tháng Năm 
 
xây dựng cấu trúc mảng 1 chiều DATEARRAY lưu trữ những phần tử thuộc cấu trúc ngày ,tháng ,năm

Viết quá tải toán tử nhập ( >> ) , xuất ( << ) (xuất theo đúng định dạng DD/MM/YYYY)
Viết quá tải toán tử so sánh bằng ( == ) so sánh 2 mảng có tất cả các ngày có thứ trong tuần tương ứng trùng nhau (VD: ta có mảng 1 là a[2] = {02/05/2016, 05/05/2016} và mảng 2 là b[2] = {16/05/2016, 19/05/2016} sẽ bằng nhau vì a[0] và b[0] đều là thứ 2, a[1] và b[1] đều là thứ 5)
viết quá tải so sánh nhỏ hơn ( < ) kiểm tra tất cả số ngày của mảng 1 nhỏ hơn mảng 2 VD: ta có mảng 1 là a[2] = {02/05/2016, 05/05/2016} và mảng 2 là b[2] = {16/05/2016, 19/05/2016} sẽ trả về "TRUE" vì tất cả phần tử ngày của mảng a nhỏ hơn mảng b )
viết quá tải toán tử cộng ( + ) để gộp 2 mảng thành 1 mảng 
viết quá tải toán tử trừ ( - ) để tạo thành 1 mảng là số ngày giữa 2 ngày tương ứng của từng mảng với c[i] là số ngày giữa ngày a[i] và ngày b[i] với mọi i < số phần tử của 2 mảng ) 
viết hàm xác định mảng có thứ tự giảm dần (trả về -1 ) hay tăng dần (trả về 1) hay không có thứ tự  (trả về 0) theo ngày, tháng, năm 
viết hàm sắp xếp mảng theo thứ tự giảm dần theo ngày, tháng, năm  
viết hàm sắp xếp mảng theo thứ tự tăng dần theo ngày, tháng, năm  

gợi ý : cách tính thứ của ngày trong năm :
nếu tháng của ngày đó nhỏ hơn 3 thì biến đổi tháng = tháng + 12 , năm  = năm - 1 ,nếu tháng của ngày đó lớn hơn 2 thì giữ nguyên ,sau đó thế vào CT : 
n = (ngày+2*tháng+(3*(tháng+1)) / 5 + năm + (năm / 4)) % 7 
với n = 0 là Chủ Nhật, n = 1 là thứ 2 , n = 3 là thứ 3,.....

lưu ý : 
Chủ Nhật - xuất ra "Sunday"
Thứ 2 - xuất ra "Monday"
Thứ 3 - xuất ra "Tuesday"
Thứ 4 - xuất ra "Wednesday"
Thứ 5 - xuất ra "Thursday"
Thứ 6 - xuất ra "Friday"
Thứ 7 - xuất ra "Saturday"

Dữ liệu vào từ file "DATE.inp": 
dòng 1: n là số phần tử của mảng 1, n dòng tiếp theo là n ngày của mảng 1, mỗi phần tử có dạng DD MM YYYY
dòng tiếp theo sau n + 1 dòng : m là số phần tử của mảng 2, m dòng tiếp theo là m ngày của mảng 2, mỗi phần tử có dạng DD MM YYYY
dòng cuối cùng : chuỗi h là chỉ dẫn sắp xếp mảng của 2 mảng sau khi gộp thành 1 mảng 

Dữ liệu xuất ra file "DATE.out":
dòng 1:K là số ngày thuộc năm nhuận của mảng 1, K dòng tiếp theo mỗi dòng gồm ngày thuộc năm nhuận ,thuộc thứ mấy trong tuần ,ngày thứ mấy trong năm và ngày tiếp theo tương ứng của ngày đó , mỗi phần tử cách nhau 1 khoảng trắng ,nếu mảng không có ngày thuộc năm nhuận thì in ra 0
dòng 2:L là số ngày thuộc năm nhuận của mảng 2, L dòng tiếp theo mỗi dòng gồm ngày thuộc năm nhuận ,thứ mấy trong tuần ,ngày thứ mấy trong năm và ngày tiếp theo của ngày đó , mỗi phần tử cách nhau 1 khoảng trắng ,nếu mảng không có ngày thuộc năm nhuận thì in ra 0
dòng 3: Nếu 2 mảng có tất cả các ngày trùng thứ trong tuần thì in ra "TRUE", ngược lại in ra "FALSE" 
dòng 4: Nếu mảng 1 có số ngày thuộc năm nhuận ít hơn mảng 2 thì in ra "1 < 2" , Nếu mảng 1 có số ngày thuộc năm nhuận bằng mảng 2 thì in ra "1 = 2" ,Nếu mảng 1 có số ngày thuộc năm nhuận nhiều hơn mảng 2 thì in ra "1 > 2"
dòng 5: Xác định thứ tự sắp xếp ngày trong mảng 1 ,nếu Tăng dần in ra "TANG" ,nếu giảm dần thì in ra "GIAM" ,nếu mảng không có thứ tự thì in ra "KHONG CO THU TU"
dòng 6: Xác định thứ tự sắp xếp ngày trong mảng 2 ,nếu Tăng dần in ra "TANG" ,nếu giảm dần thì in ra "GIAM" ,nếu mảng không có thứ tự thì in ra "KHONG CO THU TU"
dòng 7: xuất ra mảng chứa số ngày tương ứng giữa 2 phần tử của mảng 1 và 2 với c[i] là số ngày giữa ngày a[i] và b[i] , mỗi phần tử cách nhau 1 khoảng trắng  
dòng 8 : số phần tử khi gộp 2 mảng thành 1 mảng ,m+ n dòng tiếp theo xuất mảng ,nếu h là "TANG" thì xuất mảng theo thứ tự tăng dần theo ngày, tháng, năm, nếu h là "GIAM" thì xuất mảng theo thứ tự giảm dần theo ngày, tháng, năm

input: 
2
04 05 2015
12 04 2016
2
15 06 2015
14 02 2012
GIAM

output: 
1
12/04/2016 Tuesday 103 13/04/2016
1
14/02/2012 Tuesday 45 15/02/2012
TRUE
1 = 2
TANG
GIAM
42 1519 
4
12/04/2016
15/06/2015
04/05/2015
14/02/2012

'''
from datetime import datetime, timedelta

# Map thứ trong tuần
WEEKDAY_MAP = [
    "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
]

def is_leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def day_of_year(d, m, y):
    days_in_month = [31, 29 if is_leap(y) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(days_in_month[:m-1]) + d

def next_day(d, m, y):
    try:
        dt = datetime(y, m, d) + timedelta(days=1)
        return dt.day, dt.month, dt.year
    except:
        return d, m, y

def weekday(d, m, y):
    # Zeller's Congruence (adjusted for Monday=1, Sunday=0)
    if m < 3:
        m += 12
        y -= 1
    n = (d + 2 * m + (3 * (m + 1)) // 5 + y + y // 4) % 7
    return n

class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y

    @classmethod
    def from_string(cls, s):
        d, m, y = map(int, s.strip().split())
        return cls(d, m, y)

    def __str__(self):
        return f"{self.d:02d}/{self.m:02d}/{self.y:04d}"

    def __lt__(self, other):
        return (self.y, self.m, self.d) < (other.y, other.m, other.d)

    def __eq__(self, other):
        return (self.d, self.m, self.y) == (other.d, other.m, other.y)

    def is_leap(self):
        return is_leap(self.y)

    def day_of_year(self):
        return day_of_year(self.d, self.m, self.y)

    def next_day(self):
        d, m, y = next_day(self.d, self.m, self.y)
        return Date(d, m, y)

    def weekday(self):
        return weekday(self.d, self.m, self.y)

    def days_between(self, other):
        dt1 = datetime(self.y, self.m, self.d)
        dt2 = datetime(other.y, other.m, other.d)
        return abs((dt1 - dt2).days)

class DATEARRAY:
    def __init__(self, arr=None):
        self.arr = arr if arr else []

    def __len__(self):
        return len(self.arr)

    def __getitem__(self, idx):
        return self.arr[idx]

    def __setitem__(self, idx, value):
        self.arr[idx] = value

    def __str__(self):
        return "\n".join(str(date) for date in self.arr)

    def __add__(self, other):
        return DATEARRAY(self.arr + other.arr)

    def __sub__(self, other):
        n = min(len(self), len(other))
        return [self.arr[i].days_between(other.arr[i]) for i in range(n)]

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for a, b in zip(self.arr, other.arr):
            if a.weekday() != b.weekday():
                return False
        return True

    def __lt__(self, other):
        n = min(len(self), len(other))
        for i in range(n):
            if not (self.arr[i] < other.arr[i]):
                return False
        return True

    def leap_dates(self):
        return [date for date in self.arr if date.is_leap()]

    def sort(self, reverse=False):
        self.arr.sort(reverse=reverse)

    def order(self):
        if len(self.arr) < 2:
            return 0
        inc = all(self.arr[i] < self.arr[i+1] for i in range(len(self.arr)-1))
        dec = all(self.arr[i] > self.arr[i+1] for i in range(len(self.arr)-1))
        if inc:
            return 1
        elif dec:
            return -1
        else:
            return 0

def read_input(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    idx = 0
    n = int(lines[idx]); idx += 1
    arr1 = DATEARRAY([Date.from_string(lines[idx + i]) for i in range(n)])
    idx += n
    m = int(lines[idx]); idx += 1
    arr2 = DATEARRAY([Date.from_string(lines[idx + i]) for i in range(m)])
    idx += m
    h = lines[idx]
    return arr1, arr2, h

def write_output(filename, arr1, arr2, leap1, leap2, eq, cmp_leap, order1, order2, days_diff, merged, h):
    with open(filename, "w") as f:
        # Leap year dates for arr1
        if leap1:
            f.write(f"{len(leap1)}\n")
            for date in leap1:
                wd = WEEKDAY_MAP[date.weekday()]
                doy = date.day_of_year()
                nextd = date.next_day()
                f.write(f"{date} {wd} {doy} {nextd}\n")
        else:
            f.write("0\n")
        # Leap year dates for arr2
        if leap2:
            f.write(f"{len(leap2)}\n")
            for date in leap2:
                wd = WEEKDAY_MAP[date.weekday()]
                doy = date.day_of_year()
                nextd = date.next_day()
                f.write(f"{date} {wd} {doy} {nextd}\n")
        else:
            f.write("0\n")
        # Compare weekdays
        f.write("TRUE\n" if eq else "FALSE\n")
        # Compare leap year counts
        if len(leap1) < len(leap2):
            f.write("1 < 2\n")
        elif len(leap1) == len(leap2):
            f.write("1 = 2\n")
        else:
            f.write("1 > 2\n")
        # Order of arr1
        f.write("TANG\n" if order1 == 1 else "GIAM\n" if order1 == -1 else "KHONG CO THU TU\n")
        # Order of arr2
        f.write("TANG\n" if order2 == 1 else "GIAM\n" if order2 == -1 else "KHONG CO THU TU\n")
        # Days difference
        f.write(" ".join(str(x) for x in days_diff) + " \n")
        # Merged array
        f.write(f"{len(merged)}\n")
        for date in merged.arr:
            f.write(f"{date}\n")

def main():
    arr1, arr2, h = read_input("DATE.inp")
    leap1 = arr1.leap_dates()
    leap2 = arr2.leap_dates()
    eq = arr1 == arr2
    # Compare leap year counts
    cmp_leap = (len(leap1), len(leap2))
    # Order
    order1 = arr1.order()
    order2 = arr2.order()
    # Days difference
    days_diff = arr1 - arr2
    # Merge and sort
    merged = arr1 + arr2
    if h == "TANG":
        merged.sort(reverse=False)
    elif h == "GIAM":
        merged.sort(reverse=True)
    write_output("DATE.out", arr1, arr2, leap1, leap2, eq, cmp_leap, order1, order2, days_diff, merged, h)

if __name__ == "__main__":
    main()
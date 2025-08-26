'''
Ngày Tháng Năm 

Xây dựng cấu trúc để biểu diễn ngày ,tháng, năm (kiểu số nguyên và phải hợp lệ) 

Viết quá tải toán tử nhập ( >> ) ,xuất ( << ) (có kiểm tra tính hợp lệ hiện thị ra màn hình dạng MM/DD/YYYY) 
Viết hàm kiểm tra năm nhuận khi biết ngày tháng năm (ngày 15/01/2016 thuộc năm nhuận )
viết hàm tìm ngày thứ mấy trong năm khi biết ngày tháng năm (VD: ngày 15/01/2016 là ngày thứ 15 trong năm 2016)
viết hàm xác định thứ trong tuần khi biết ngày tháng năm (16/05/2016 là thứ 2 )
viết hàm tìm ngày kế tiếp khi biết ngày tháng năm (VD: 15/05/2016 ngày kế tiếp là 16/05/2016)
viết quá tải toán tử so sánh bằng ( == )  để so sánh 2 ngày trùng nhau (VD: 17/05/2011 == 17/05/2011 )
viết hàm kiểm tra xem 2 ngày có trùng thứ trong tuần không (VD : 16/05/2016 trùng thứ với 09/05/2016 vì cùng là thứ 2)
viết quá tải so sánh nhỏ hơn ( < ) để so sánh ngày nào nhỏ hơn (VD: 15/05/2013 < 02/07/2013)
viết quá tải so sánh trừ ( - ) để tính số ngày giữa 2 ngày (VD: 15/05/2015 đến ngày 20/05/2015 cách nhau 5 ngày ) 
gợi ý : cách tính thứ của ngày trong năm :
nếu tháng của ngày đó nhỏ hơn 3 thì biến đổi tháng = tháng + 12 , năm  = năm - 1 ,nếu tháng của ngày đó lớn hơn 2 thì giữ nguyên ,sau đó thế vào CT : 
n = (ngày+2*tháng+(3*(tháng+1)) / 5 + năm + (năm / 4)) % 7 
với n = 0 là Chủ Nhật, n = 1 là thứ 2 , n = 3 là thứ 3,.....

dữ liệu nhập: 
dòng 1: ngày thứ 1, có dạng DD MM YYYY
dòng 2: ngày thứ 2, có dạng DD MM YYYY

dữ liệu xuất: 
dòng 1: xuất ra ngày 1 ,thuộc  thứ mấy trong trong tuần, ngày thứ mấy trong năm, ngày kế tiếp,  nếu ngày 1 là năm nhuân in ra "TRUE", ngược lại in ra "FALSE", 
dòng 2: xuất ra ngày 2 ,thuộc  thứ mấy trong trong tuần, ngày thứ mấy trong năm, ngày kế tiếp, nếu ngày 2 là năm nhuân in ra "TRUE", ngược lại in ra "FALSE",
dòng 3: nếu ngày 1 và 2 có thứ trong tuần trùng nhau thì in ra "TRUE" ,ngược lại in ra "FALSE"
dòng 4: nếu ngày 1 nhỏ hơn ngày 2 thì in ra "1 < 2", nếu ngày 1 trùng ngày 2 in ra "1 = 2", nếu ngày 1 lớn hơn ngày 2 in ra "1 > 2"
dòng 5: số ngày giữa ngày 1 và ngày 2
lưu ý : 
Chủ Nhật - xuất ra "Sunday"
Thứ 2 - xuất ra "Monday"
Thứ 3 - xuất ra "Tuesday"
Thứ 4 - xuất ra "Wednesday"
Thứ 5 - xuất ra "Thursday"
Thứ 6 - xuất ra "Friday"
Thứ 7 - xuất ra "Saturday"

Ví dụ:

Input	
17 05 2016
05 05 2015
Output
17/05/2016 Tuesday 138 18/05/2016 TRUE
05/05/2015 Tuesday 125 06/05/2015 FALSE
TRUE
1 > 2
378

'''

from datetime import datetime, timedelta

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
        self.valid = self.is_valid()

    @classmethod
    def from_string(cls, s):
        d, m, y = map(int, s.strip().split())
        return cls(d, m, y)

    def is_valid(self):
        try:
            datetime(self.y, self.m, self.d)
            return True
        except:
            return False

    def __str__(self):
        return f"{self.d:02d}/{self.m:02d}/{self.y:04d}"

    def is_leap(self):
        return is_leap(self.y)

    def day_of_year(self):
        return day_of_year(self.d, self.m, self.y)

    def next_day(self):
        d, m, y = next_day(self.d, self.m, self.y)
        return Date(d, m, y)

    def weekday(self):
        return weekday(self.d, self.m, self.y)

    def __eq__(self, other):
        return (self.d, self.m, self.y) == (other.d, other.m, other.y)

    def __lt__(self, other):
        return (self.y, self.m, self.d) < (other.y, other.m, other.d)

    def __sub__(self, other):
        dt1 = datetime(self.y, self.m, self.d)
        dt2 = datetime(other.y, other.m, other.d)
        return abs((dt1 - dt2).days)

    def same_weekday(self, other):
        return self.weekday() == other.weekday()

def main():
    # Nhập dữ liệu
    s1 = input().strip()
    s2 = input().strip()
    date1 = Date.from_string(s1)
    date2 = Date.from_string(s2)

    # Dòng 1
    wd1 = WEEKDAY_MAP[date1.weekday()]
    doy1 = date1.day_of_year()
    next1 = date1.next_day()
    leap1 = "TRUE" if date1.is_leap() else "FALSE"
    print(f"{date1} {wd1} {doy1} {next1} {leap1}")

    # Dòng 2
    wd2 = WEEKDAY_MAP[date2.weekday()]
    doy2 = date2.day_of_year()
    next2 = date2.next_day()
    leap2 = "TRUE" if date2.is_leap() else "FALSE"
    print(f"{date2} {wd2} {doy2} {next2} {leap2}")

    # Dòng 3
    print("TRUE" if date1.same_weekday(date2) else "FALSE")

    # Dòng 4
    if date1 < date2:
        print("1 < 2")
    elif date1 == date2:
        print("1 = 2")
    else:
        print("1 > 2")

    # Dòng 5
    print(date1 - date2)

if __name__ == "__main__":
    main()
'''
SMG Gateway là một thiết bị để quản lý hàng loạt SIM điện thoại. Mỗi thiết bị có thể chứa N slot để gắn SIM. Mỗi slot như vậy sẽ có các thông tin như: mã số (kiểu chuỗi, tối đa 10 kí tự), số điện thoại của SIM (kiểu chuỗi, tối đa 11 kí tự i), nhà mạng cung cấp (kiểu chuỗi, tối đa 20 kí tự).

Hãy xây dựng chương trình để quản lý SMG Gateway với các chức năng sau:

Hàm nhập thông tin cho N slot
Hàm xuất thông tin cho N slot
Hàm nhập vào số điện thoại (tối đa 11 chữ số), sau đó tìm và in ra thông tin của các slot có cùng nhà mạng cung cấp với số điện thoại nhập vào (dựa theo đầu số là 3 kí tự đầu của số điện thoại)


Input:

- Dòng đầu tiên là số nguyên N cho biết số lượng slot

- N dòng tiếp theo, mỗi dòng là thông tin của từng slot, bao gồm: mã số, số điện thoại, nhà mạng. Mỗi thông tin cách nhau 1 khoảng trắng

- Dòng cuối cùng chứa số điện thoại để tìm slot có cùng nhà mạng

Output:

- Lần lượt in ra thông tin của các slot tìm được, mỗi slot là một dòng có các thông tin: mã số, số điện thoại, nhà mạng cung cấp. Mỗi thông tin cách nhau 1 dấu hai chấm “:”

 

Ví dụ:

Input:

3
S01 0903334455 Mobi
S02 0981234567 Viettel
S03 0919999999 Vinaphone
0907773177

Output:
S01:0903334455:Mobi

'''

prefix_to_network = {
    '090': 'Mobi',
    '093': 'Mobi',
    '089': 'Mobi',
    '070': 'Mobi',
    '079': 'Mobi',
    '077': 'Mobi',
    '076': 'Mobi',
    '078': 'Mobi',
    '091': 'Vinaphone',
    '094': 'Vinaphone',
    '088': 'Vinaphone',
    '083': 'Vinaphone',
    '084': 'Vinaphone',
    '085': 'Vinaphone',
    '081': 'Vinaphone',
    '082': 'Vinaphone',
    '098': 'Viettel',
    '097': 'Viettel',
    '096': 'Viettel',
    '086': 'Viettel',
    '032': 'Viettel',
    '033': 'Viettel',
    '034': 'Viettel',
    '035': 'Viettel',
    '036': 'Viettel',
    '037': 'Viettel',
    '038': 'Viettel',
    '039': 'Viettel',
}

def get_network(phone):
    prefix = phone[:3]
    return prefix_to_network.get(prefix, '')

def main():
    N = int(input())
    slots = []
    for _ in range(N):
        parts = input().strip().split()
        slots.append({
            'id': parts[0],
            'phone': parts[1],
            'network': parts[2]
        })
    search_phone = input().strip()
    search_network = get_network(search_phone)
    for slot in slots:
        if slot['network'] == search_network:
            print(f"{slot['id']}:{slot['phone']}:{slot['network']}")

if __name__ == "__main__":
    main()
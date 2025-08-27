<?php
//echo "Dòng 1<br>", "NHÀ BAO VIỆC HỌC PHP TUỔI<br>", "Dòng 2<br>";
/* Quy tắc đặt biến
$x = 5;
$y = 10;
$z = $x + $y;
$d = $z + $x + $y;
echo $z. "<br>";
echo $d;    
*/


// Quy tắc đặt hằng số
// define('Ga123', 3);
//  echo Ga123;
// const GunnyMobileTBNapVip = "VIP 20";
//  echo GunnyMobileTBNapVip;    


// Kiểu dữ liệu int
// $x = 1;
// $y = 3.7;
// $z = true;
// $d = "1";
// $a = 1;
// $mang = ['PHP', 'Java', 'JavaScript'];

// var_dump($x);
// echo "<br>";
// var_dump($y);
// echo "<br>";
// var_dump(GunnyMobileTBNapVip);
// echo "<br>";
// var_dump($z);
// echo "<br>";
// var_dump($mang);
// echo "<br>";

// echo $mang[0]. "<br>";
// echo $mang[1]. "<br>";
// echo $mang[2]. "<br>";

// echo '<pre>';
// print_r($mang);
// echo '</pre>';

// echo "<br>";
// var_dump($x <> $d);

// echo "<br>";
// echo ++$a. "<br>";
// $b = $a++;
// echo $b. "<br>";
// echo $a;
// echo "<br>";


// $s = 2005;
// if(2025 - $s == 20){
//     echo "Đủ 20 tuổi";
// }
// elseif(2025 - $s > 20){
//     echo "Trên 20 tuổi";
// }
// else {
//     echo "Chưa đủ 20 tuổi";
// }


// $day = 4;
// switch($day){
//     case 2:
//         echo "Thứ 2";
//         break;
//     case 3:
//         echo "Thứ 3";
//         break;
//     case 4:
//         echo "Thứ 4";
//         break;
//     case 5:
//         echo "Thứ 5";
//         break;
//     case 6:
//         echo "Thứ 6";
//         break;
//     case 7:
//         echo "Thứ 7";
//         break;
//     case 8:
//         echo "Thứ 8";
//         break;
//     default:
//         echo "ERROR";
// }


// VÒNG LẶP FOR
/*
- VL for
- VL while
- VL do-while
- VL foreach
*/
//// VÒNG LẶP FOR  -- Biết trước số lần lặp
// VD: minh họa for Tìm số nguyên tố nếu có in ra ko thì in ra -1 
// Cách 1: Sử dụng trực tiếp ko dùng hàm
// for($i = 2; $i <= 100; $i++){
//     $snt = true;
//     for($j = 2; $j <= sqrt($i); $j++){
//         if($i % $j == 0){
//             $snt = false;
//             break;
//         }
//     }
//     if($snt){
//         echo $i. " ";
//         $found = true;
//     }
// }
// if(!$found){
//     echo -1;
// }
// Cách 2: Sử dụng hàm
// function SNT($n){
//     if($n < 2) return false;
//     for($i = 2; $i <= sqrt($n); $i++){
//         if($n % $i == 0){
//             return false;
//         }
//     }
//     return true;
// }
// $found = false;
// for($i = 2; $i <= 10; $i++){
//     if(SNT($i)){
//         echo $i. " ";
//         $found = true;
//     }
// }
// if(!$found){
//     echo -1;
// }


/// VÒNG LẶP WHILE  - Chưa biết trước số lần lặp 
// while(condition){
//     code
//}

// $x = 1;
// while($x <= 10){
//     echo "$x <br>";
//     $x++;
// }

/// VÒNG LẶP DO-WHILE -  Lặp ít nhất 1 lần 
// do {
//     code
// } while(condition);

// $x = 1;
// do {
//     echo "$x <br>";
//     $x++;
// } while($x < 5);


/// VÒNG LẶP FOREACH // Dùng để duyệt các mảng và các đối tượng 
// foreach($mang as $value){
//     echo "$value <br>";
// }

// $mang = [1,2,3,4,5,6,7,8,9,10];
// foreach($mang as $value){
//     echo "$value <br>";
// }


// Hàm có giá trị trả về
// function tinhtong($a, $b){
//     return $a + $b;
// }
// echo tinhtong(5, 10);

// Tham trị: mặc định giá trị ban đầu của tham số truyền vào
// Tham chiếu: truyền tham số bằng cách tham chiếu (giá trị mặc định sẽ thay đổi trong quá trình xử lý hàm)
// function tinhtongthamchieu(&$a, &$b){
//     $a += 10;
//     $b += 20;
//     return $a + $b;
// }
// echo tinhtongthamchieu($x, $y);

// HÀM ẨN DANH
// $test = function($x){
//     return $x;
// }; // Chú ý thêm dấu ; ở cuối
// echo $test(5);


// BIẾN TOÀN CỤC, BIẾN CỤC BỘ
// Biến toàn cục: Được định nghĩa bên ngoài hàm, có thể truy cập từ bất kỳ đâu trong mã nguồn
// Biến cục bộ: Được định nghĩa bên trong hàm, chỉ có thể truy cập trong phạm vi của hàm đó
// Biến Static: Giữ giá trị giữa các lần gọi hàm
// $x = 5; // Biến toàn cục
// function test(){
    //$y = 10; // Biến cục bộ
    // echo $x; // Lỗi vì $x không được định nghĩa trong phạm vi này
    // echo $y;
    // Nếu muốn sử dụng biến toàn cục trong hàm, cần khai báo từ khóa global
    // global $x;  
//     static $z = 1; // Sử dụng biến static
//     $z++;
//     echo $z;
// }
// test();
// //echo "<br>";
// //echo $x;
// echo "<br>";
// test();
// echo "<br>";
// test();


// HÀM ISSET VÀ HÀM EMPTY

// Hàm isset dùng để kiểm tra 1 biến có tồn tại hay ko, Kết quả trả về true hoặc false
// $test = 0;
// if(isset($test)){
//     echo "Biến test có tồn tại";
// }
// else{
//     echo "Biến test ko tồn tại";
// }

// Hàm empty dùng để kiểm tra 1 biến có rỗng hay ko, Kết quả trả về true hoặc false
// $test = null; // Nếu đặt = 0 thì cũng sẽ rỗng
// if(empty($test)){
//     echo "Biến test rỗng";
// }
// else{
//     echo "Biến test không rỗng";
// }


// CÂU LỆNH INCLUDE , REQUIRE, INCLUDE_ONCE, REQUIRE_ONCE: Nhúng file
// - include: bao gồm file và tiếp tục thực thi nếu file không tồn tại (Nhúng được nhiều lần) (Nếu gặp lỗi --> tiếp tục chạy chương trình)
// - require: bao gồm file và dừng thực thi nếu file không tồn tại (Không nhúng được nhiều lần) (Nếu gặp lỗi --> dừng chương trình)
// - include_once: bao gồm file chỉ 1 lần (Nếu đã bao gồm file đó rồi thì sẽ không bao gồm lại nữa) (Nếu gặp lỗi --> tiếp tục chạy chương trình)
// - require_once: bao gồm file chỉ 1 lần và dừng thực thi nếu file không tồn tại (Không nhúng được nhiều lần) (Nếu gặp lỗi --> dừng chương trình)


// // MẢNG (ARRAY)
// // - Mảng chỉ mục: bắt đầu từ 0
// $x = [1,2,3,4,5];
// // 1 : key : 0 -> value: 1
// //echo $x[4];
// // foreach($x as $item){ 
// //     echo $item;
// //     echo "<br>";
// // }
// foreach($x as $key => $value){ // Key là vị trí của phần tử trong mảng
//     echo $key; // Nếu echo $value thì in ra các giá trị trong mảng
//     echo "<br>";
// }

// - Mảng kết hợp : key sẽ là chuỗi
// $pvs = [
//     'FCes' => 'Solozy, Ymdu, SirT, Zest',
//     'Agal' => 'Himass, Taikon, Haisaki, Destroy',
//     'Te' => 'Clories, Tanvu, Delwyn, DuckHieu',
// ];
// echo "<pre>";
// print_r($pvs);
// echo "</pre>";

// echo $pvs['Agal'];

// foreach ($pvs as $key => $value){
//     echo $key;
//     echo "<br>";
// }


// - Mảng đa chiều: Mảng chứa các mảng khác (mảng con bên trong mảng cha)
// $pvs = [
//     'FCes' => ['Solozy', 'Ymdu', 'SirT', 'Zest'],
//     'Agal' => ['Himass', 'Taikon', 'Haisaki', 'Destroy'],
//     'Te' => ['Clories', 'Tanvu', 'Delwyn', 'DuckHieu'],
// ];
// // var_dump($pvs);
// // echo $pvs['FCes'][2];

// foreach($pvs as $key => $value){
//     echo "Đội $key gồm: ";
//     foreach($value as $item){
//         echo $item. ", ";
//     }
//     echo "<br>";
// }

// CÁC HÀM XỬ LÝ MẢNG // 

// 1. count(): Đếm số phần tử trong mảng    
// $pvs = ['FCes', 'Agal', 'Te', 'Fl'];
// echo count($pvs);

// 2. in_array($values, $array): Kiểm tra xem giá trị có tồn tại trong mảng hay không
// $pvs = ['FCes', 'Agal', 'Te', 'Fl'];
// echo in_array('FCes', $pvs); // Trả về 1 nghĩa là true còn ko có hiển thị gì nghĩa là false

// 3. array_keys($array): Trả về tất cả các key của mảng dưới dạng mảng
// $pvs = ['FCes', 'Agal', 'Te', 'Fl'];
// // echo array_keys($pvs); // Chỉ in ra Array 
// $key = array_keys($pvs);
// foreach ($key as $item){
//     echo $item;
//     echo "<br>";
// } // In ra 0 1 2 3 

// 4. array_values($array): Trả về tất cả các giá trị của mảng dưới dạng mảng
// $pvs = ['FCes', 'Agal', 'Te', 'Fl'];
// echo array_values($pvs); // Chỉ in ra Array
// $value = array_values($pvs);
// foreach ($value as $item) {
//     echo $item;
//     echo "<br>";
// } // In ra FCes Agal Te Fl

// 5. array_combine($keys, $values): Tạo mảng kết hợp từ 2 mảng
// $keys = ['FCes', 'Agal', 'Te', 'Fl'];
// $values = ['Solozy', 'Himass', 'Clories', 'DuckHieu'];
// $result = array_combine($keys, $values);
// echo "<pre>";
// print_r($result);
// echo "</pre>";

// 6. sort($array): Sắp xếp mảng theo thứ tự tăng dần
// $mang = [0,10,5,3,2,11,24];
// sort($mang);
// foreach ($mang as $item) {
//     echo $item;
//     echo "<br>";
// } // In ra 0 2 3 5 10 11 24

// 7. rsort($array): Sắp xếp mảng theo thứ tự giảm dần
// $mang = [0,10,5,3,2,11,24];
// rsort($mang);
// foreach ($mang as $item) {
//     echo $item;
//     echo "<br>";
// } // In ra 24 11 10 5 3 2 0

// 8. array_push($array, $value): Thêm phần tử vào cuối mảng
// $mang = [1,2,3];
// array_push($mang, 4);
// foreach($mang as $item){
//     echo $item;
//     echo "<br>";
// } // In ra 1 2 3 4

// 9. array_pop($array): Xóa phần tử cuối mảng
// $mang = [1,2,3,4];
// array_pop($mang);
// foreach($mang as $item){
//     echo $item;
//     echo "<br>";
// } // In ra 1 2 3

// 10. array_unshift($array, $value): Thêm phần tử vào đầu mảng
// $mang = [1,2,3];
// array_unshift($mang, 0);
// foreach($mang as $item){
//     echo $item;
//     echo "<br>";
// } // In ra 0 1 2 3

// 11. array_shift($array): Xóa phần tử đầu mảng
// $mang = [1,2,3,4];
// array_shift($mang);
// foreach($mang as $item){
//     echo $item;
//     echo "<br>";
// } // In ra 2 3 4
// echo "<pre>"; 
// print_r($mang);
// echo "</pre>"; // Dùng echo "<pre></pre>" để in mảng dễ nhìn hơn

// 12. array_filter($array, $callback): Lọc mảng theo điều kiện
// $mang = [1,2,3,4,5];
// $result = array_filter($mang, function($item){ // function($item) dùng để định nghĩa một hàm ẩn danh
//     return $item % 2 == 0; // Điều kiện lọc ra các số chẵn
// });
// foreach($result as $item){
//     echo $item;
//     echo "<br>";
// } // In ra 2 4
// echo "<pre>";
// print_r($result);
// echo "</pre>";

// 13. array_unique($array): Lọc bỏ các giá trị trùng lặp trong mảng
// $mang = [1,2,2,3,4,4,5];
// $result = array_unique($mang);
// foreach($result as $item){
//     echo $item;
//     echo "<br>";
// } // In ra 1 2 3 4 5
// echo "<pre>";
// print_r($result);
// echo "</pre>"; 

// 14. array_merge($array1, $array2): Kết hợp hai mảng
// $mang1 = [1,2,3];
// $mang2 = [4,5,6];
// $result = array_merge($mang1, $mang2);
// foreach($result as $item){
//     echo $item;
//     echo "<br>";
// } // In ra 1 2 3 4 5 6
// echo "<pre>";
// print_r($result);
// echo "</pre>";

// 15. explode($delimiter, $string): Tách chuỗi thành mảng
// $mang = "Hello World PHP";
// $result = explode(" ", $mang); // Điều kiện để tách chuỗi tại dấu cách. Còn nếu muốn tách tại dấu phẩy thì dùng explode(",", $mang);
// foreach($result as $item){
//     echo $item;
//     echo "<br>";
// } // In ra Hello World PHP (mỗi từ 1 dòng)s
// echo "<pre>";
// print_r($result);
// echo "</pre>";

// 16. implode($delimiter, $array): Tạo chuỗi từ mảng
// $mang = ['Hello', 'World', 'PHP'];
// $result = implode(" ", $mang); // Điều kiện để nối các phần tử mảng thành chuỗi, cách nhau bởi dấu cách
// echo $result; // In ra Hello World PHP


// HÀM XỬ LÝ CHUỖI //

// Nối chuỗi
// $a = "Nhà bao";
// $b = "việc!!!";
// $c = $a . " " . $b;
// echo $c;

// 1. strlen($string): trả về độ dài của chuỗi
// $str = "Hello World PHP";
// echo strlen($str); // In ra là 15

// 2. str_word_count($string): Đếm số từ trong chuỗi
// $str = "Hello PVS";
// echo str_word_count($str); // In ra là 2

// 3. strrev($string): Đảo ngược chuỗi
// $str = "12345";
// echo strrev($str); // In ra là 54321

// 4. strpos($string, $search): Tìm vị trí của chuỗi con trong chuỗi
// $str = "Hello World";
// echo strpos($str, "World"); // In ra là 6

// 5. str_replace($search, $replace, $subject): Thay thế chuỗi con trong chuỗi
// $str = "Hello World";
// echo str_replace("World", "PVS", $str); // In ra là Hello PVS

// 6. substr($string, $start, $length): Trích xuất một phần của chuỗi
// $str = "Hello My Friend";
// echo substr($str, 6, 2); // In ra là My

// 7. strtolower($string): Chuyển chuỗi thành chữ thường
// $str = "HELLO WORLD";
// echo strtolower($str); // In ra là hello world

// 8. strtoupper($string): Chuyển chuỗi thành chữ hoa
// $str = "hello world";
// echo strtoupper($str); // In ra là HELLO WORLD

// 9. ucfirst($string): Chuyển chữ cái đầu tiên thành chữ hoa
// $str = "hello world";
// echo ucfirst($str); // In ra là Hello world

// 10. ucwords($string): Chuyển chữ cái đầu tiên của mỗi từ thành chữ hoa
// $str = "hello world z";
// echo ucwords($str); // In ra là Hello World Z

// 11. trim($string): Xóa khoảng trắng ở đầu và cuối chuỗi
// $str = "   Hello World   ";
// echo trim($str); // In ra là Hello World

// 12. rtrim($string): Xóa khoảng trắng ở cuối chuỗi
// $str = "   Hello World   ";
// echo rtrim($str); // In ra là "   Hello World"

// 13. ltrim($string): Xóa khoảng trắng ở đầu chuỗi
// $str = "   Hello World   ";
// echo ltrim($str); // In ra là "Hello World   "

// 14. explode($delimiter, $string): Tách chuỗi thành mảng
// $str = "Hello World PHP";
// $result = explode(" ", $str);
// foreach($result as $item){
//     echo $item;
//     echo "<br>";
// } // In ra Hello World PHP (mỗi từ 1 dòng)
// echo "<pre>";
// print_r($result);
// echo "</pre>";

// 15. implode($delimiter, $array): Tạo chuỗi từ mảng
// $arr = ['Hello', 'World', 'PHP'];
// $result = implode(" ", $arr);
// echo $result; // In ra Hello World PHP

// 16. strcmp($string1, $string2): So sánh hai chuỗi
// $str1 = "Hello";
// $str2 = "Hello";
// echo strcmp($str1, $str2); // In ra 0 (bằng nhau) // Nếu khác chuỗi thì in ra -1

// 17. strcasecmp($string1, $string2): So sánh hai chuỗi (không phân biệt chữ hoa chữ thường)
// $str1 = "Hello";
// $str2 = "hello";
// echo strcasecmp($str1, $str2); // In ra 0 (bằng nhau) // Nếu khác chuỗi thì in ra -1

// 18. str_contains($haystack, $needle): Kiểm tra xem chuỗi có chứa chuỗi con hay không
// $str = "Hello World";
// echo str_contains($str, "World"); // In ra 1 (true) // Nếu không chứa thì in ra 0 (false)'

// 19. str_pad($string, $length, $pad_string, $pad_type): Thêm ký tự vào chuỗi để đạt độ dài mong muốn
// $str = "Hello";
// echo str_pad($str, 10, "-=", STR_PAD_BOTH); // In ra -=Hello-=- (đệm chuỗi)

// 20. strip_tabs($string): Xóa tất cả các tab trong chuỗi HTML
// function strip_tabs($string) {
//     return str_replace("\t", "", $string);
// }
// $str = '<strong><i>Tom & Jerry</i></strong>';
// echo strip_tabs($str); // Chặn ko cho mở chỉnh sửa trên web (In ra Tom & Jerry)

// 21. htmlspecialchars($string): Chuyển ký tự HTML thành mã 
// $str = '<strong><i>Tom & Jerry</i></strong>';
// echo htmlspecialchars($str); // In ra Tom &amp; Jerry
// $str = '<script>alert("XSS Attack")</script>';
// echo $str; // Báo động XSS Attack


// CÁC HÀM MÃ HÓA //
// 1. md5($string): Tính toán mã băm MD5 của chuỗi
// $str = "Hello World";
// echo md5($str); // In ra mã băm MD5

// 2. sha1($string): Tính toán mã băm SHA-1 của chuỗi
// $str = "Hello World";
// echo sha1($str); // In ra mã băm SHA-1

// 3. base64_encode($string): Mã hóa chuỗi thành Base64
// $str = "Hello World";
// echo base64_encode($str); // In ra SGVsbG8gV29ybGQ=

// 4. base64_decode($string): Giải mã chuỗi Base64
// $str = "SGVsbG8gV29ybGQ=";
// echo base64_decode($str); // In ra Hello World


// PHƯƠNG THỨC GET //
// VD:
// $ten = $_GET['ten'];
// $tuoi = $_GET['tuoi'];
// if (!empty($ten) && !empty($tuoi)) {
//     echo "Tên: " . htmlspecialchars($ten) . "<br>";
//     echo "Tuổi: " . htmlspecialchars($tuoi);
// } else {
//     echo "Vui lòng nhập đầy đủ thông tin.";
// }

// <form method = "GET" action="./result.php">
//     <input type = "text" name = "ten" placeholder = "Nhập tên...">
//     <input type = "text" name = "password" placeholder = "Nhập mật khẩu...">
//     <button type = "submit">Gửi</button>
// </form>

// PHƯƠNG THỨC POST //
/*
- là phương thức gửi dữ liệu an toàn hơn GET vì dữ liệu không hiển thị trên URL
- $ _POST
- Ưa điểm của POST: cho phép gửi dữ liệu lớn hơn và phức tạp hơn (như file upload)
- Nhược điểm: Không thể kiểm tra nhanh bằng URL
*/

// VD:

// <form method = "POST" action="./result.php">
//     <input type = "text" name = "ten" placeholder = "Nhập tên...">
//     <input type = "text" name = "password" placeholder = "Nhập mật khẩu...">
//     <button type = "submit">Gửi</button>
// </form>
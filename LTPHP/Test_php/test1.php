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


// ĐỆ QUY TRONG PHP //
// function giaiThua($n){
//     if($n == 0 || $n == 1){
//         return 1;
//     }
//     return $n * giaiThua($n - 1);
// }
// echo giaiThua(5); // In ra 120


// BIẾN SIÊU TOÀN CỤC - $_REQUEST //
// Dùng để lấy tất cả các biến $_GET, $_POST, $_COOKIE


// XỬ LÝ VALIDATE TRONG PHP //
/*
- Xử lý dữ liệu từ form
- Ngăn chặn tấn công XSS, SQL Injection
- Đảm bảo dữ liệu đúng định dạng trước khi lưu vào CSDL
=> Người dùng nhập dữ liệu vào form, dữ liệu sẽ được gửi lên server và xử lý bằng PHP
*/
// VD:

// <form method="POST" action="./result.php">
//     <input type="text" name="ten" placeholder="Nhập tên..."><br>
//     <input type="text" name="email" placeholder="Nhập email..."><br>
//     <input type="text" name="password" placeholder="Nhập mật khẩu..."><br>
//     <button type="submit">Gửi</button>
// </form>


// DATETIME TRONG PHP //

// //- Lấy thời gian hiện tại
// echo date("Y-m-d H:i:s"); // In ra thời gian hiện tại
// echo "<br>";
// //- Chuyển đổi chuỗi thành đối tượng DateTime
// $date = DateTime::createFromFormat("Y-m-d", "2023-03-15");
// echo $date->format("d/m/Y"); // In ra 15/03/2023
// echo "<br>";
// //- Thao tác với thời gian
// $date = new DateTime();
// $date->modify("+1 day");
// echo $date->format("Y-m-d"); // In ra ngày mai
// echo "<br>";
// //date_default_timezone_set("UTC"); // : Thiết lập múi giờ mặc định
// date_default_timezone_set("Asia/Ho_Chi_Minh"); // UTC, GMT+7, Việt Nam
// echo date("Y-m-d H:i:s"); // In ra thời gian hiện tại theo múi giờ đã thiết lập
// echo "<br>";
// // time(): Trả về thời gian Unix timestamp
// echo time(); // In ra thời gian hiện tại tính bằng giây từ 1/1/1970


// UPLOAD FILE TRONG PHP //
// input type = "file"
// $_FILE
// Upload file thì method bắt buộc phải là POST
// enctype="multipart/form-data"

// <form method="POST" action="./result.php" enctype="multipart/form-data">
//     <input type="file" name="file_upload">
//     <button type="submit">Upload</button>
// </form>


// COOKIE TRONG PHP //
// - Cookie là một tập tin nhỏ được lưu trữ trên máy tính của người dùng bởi trình duyệt web
// - Cookie được sử dụng để lưu trữ thông tin người dùng và trạng thái phiên làm việc
// - Cookie có thể có thời gian sống (expiration time) và có thể được thiết lập để tự động xóa sau một khoảng thời gian nhất định
// - Để sử dụng cookie trong PHP, ta sử dụng hàm setcookie(name, value, expire, path, domain, secure, httponly)
// name : tên cookie
// value: giá trị cookie
// expire: thời gian sống của cookie
// path: đường dẫn mà cookie có hiệu lực
// domain: miền mà cookie có hiệu lực
// secure: chỉ gửi cookie qua HTTPS
// httponly: chỉ cho phép truy cập cookie qua HTTP(S), không cho phép truy cập qua JavaScript
// - get cookie
// - xóa cookie
// setcookie('John', '2000', time() + 3600, "/"); // Tạo cookie tên John có giá trị 2000, thời gian sống 1 giờ, có hiệu lực trên toàn bộ trang web


// SESSION TRONG PHP //
/*
- Session là một cơ chế lưu trữ dữ liệu tạm thời trên server
- Dữ liệu session được lưu trữ trên server và được xác định bằng một mã định danh (session ID) duy nhất
- Session thường được sử dụng để lưu trữ thông tin người dùng trong quá trình truy cập web
- Để sử dụng session trong PHP, ta sử dụng các hàm session_start(), $_SESSION, session_destroy()
*/
// session_start(); // Bắt đầu phiên làm việc
// $_SESSION['username'] = 'JohnD'; // Tạo xong Session có tên username có giá trị JohnD

// if(isset($_SESSION['username'])){
//     echo $_SESSION['username']; // In ra giá trị của Session
// }


// CÁC LỖI ERROR TRONG PHP //
/*
- Notice: Thông báo lỗi nhẹ, thường xảy ra khi sử dụng biến chưa được khởi tạo
- Warning: Cảnh báo lỗi, xảy ra khi có vấn đề nhưng kịch bản vẫn tiếp tục thực thi
- Fatal error: Lỗi nghiêm trọng, xảy ra khi PHP không thể tiếp tục thực thi kịch bản
- Parse error: Lỗi cú pháp, xảy ra khi có lỗi trong mã nguồn
- Exception error: Lỗi ngoại lệ, xảy ra khi có lỗi trong quá trình thực thi (Lỗi được ném ra trong khối try-catch)
*/

// echo 'hello'; // Nếu ko có dấu ; ở cuối dòng thì sẽ báo lỗi Parse error 
// john(); // Chưa được định nghĩa nên sẽ báo lỗi Fatal error

// try{
//     $age = -20;
//     if($age < 18){
//         throw new Exception("Tuổi ko hợp lệ");
//     }
//     echo "Tuổi hợp lệ";
// }catch(Exception $e){
//     echo "Lỗi: " . $e->getMessage();
// }


// TỔNG QUAN VỀ MYSQL VÀ NGÔN NGỮ TRUY VẤN
// Client (người dùng) -> request (yêu cầu) -> Server (máy chủ) -> CSDL (lấy dữ liệu) -> response (phản hồi) -> Client (người dùng)
// Ngôn ngữ truy vấn: SQL (Structured Query Language)   
// phpmyadmin: công cụ quản lý cơ sở dữ liệu MySQL qua giao diện web


// CREATE DATABASE, CREATE TABLE 
/*
- Kiểu dữ liệu dùng trong SQL:
    + INT: số nguyên
    + VARCHAR: chuỗi ký tự có độ dài biến đổi
    + TEXT: chuỗi ký tự có độ dài lớn
    + DATE: ngày tháng
    + DATETIME: ngày giờ
    + TIMESTAMP: dấu thời gian
    + FLOAT, DOUBLE: số thực
    + BOOLEAN: giá trị đúng/sai

- Thao tác với TABLE trong SQL:
    + CREATE TABLE: tạo bảng
    + ALTER TABLE: sửa bảng
    + DROP TABLE: xóa bảng
    + RENAME TABLE: đổi tên bảng
    + TRUNCATE TABLE: xóa tất cả dữ liệu trong bảng nhưng giữ cấu trúc bảng
    + INSERT INTO: chèn dữ liệu
    + SELECT: truy vấn dữ liệu
    + UPDATE: cập nhật dữ liệu
    + DELETE: xóa dữ liệu
    + WHERE: điều kiện lọc dữ liệu
    + JOIN: kết hợp dữ liệu từ nhiều bảng
    + ORDER BY: sắp xếp dữ liệu
    + GROUP BY: nhóm dữ liệu
    + HAVING: điều kiện lọc nhóm dữ liệu
    + LIMIT: giới hạn số lượng bản ghi trả về
    + OFFSET: bỏ qua một số bản ghi
    + UNION: kết hợp kết quả từ nhiều truy vấn
    + INDEX: tạo chỉ mục để tăng tốc truy vấn
    + FOREIGN KEY: khóa ngoại để liên kết giữa các bảng
    + PRIMARY KEY: khóa chính để xác định duy nhất một bản ghi trong bảng
- Thao tác với DATABASE trong SQL:
    + CREATE DATABASE: tạo cơ sở dữ liệu
    + ALTER DATABASE: sửa cơ sở dữ liệu
    + DROP DATABASE: xóa cơ sở dữ liệu
    + RENAME DATABASE: đổi tên cơ sở dữ liệu
- Khóa chính (Primary Key):
    + Là một cột hoặc tập hợp các cột trong bảng dùng để xác định duy nhất mỗi bản ghi
    + Không được phép có giá trị NULL và phải có giá trị duy nhất
    + Mỗi bảng chỉ được phép có một khóa chính
    + Tăng hiệu suất truy vấn và đảm bảo tính toàn vẹn dữ liệu
- Khóa ngoại (Foreign Key):
    + Là một cột hoặc tập hợp các cột trong bảng dùng để liên kết với khóa chính của bảng khác
    + Giúp duy trì tính toàn vẹn dữ liệu giữa các bảng
    + Cho phép thiết lập các ràng buộc như CASCADE, SET NULL, NO ACTION khi xóa hoặc cập nhật dữ liệu
- Mối quan hê:
    + Một-một (One-to-One): Mỗi bản ghi trong bảng A tương ứng với một bản ghi duy nhất trong bảng B
    + Một-nhiều (One-to-Many): Mỗi bản ghi trong bảng A có thể liên kết với nhiều bản ghi trong bảng B
    + Nhiều-nhiều (Many-to-Many): Mỗi bản ghi trong bảng A có thể liên kết với nhiều bản ghi trong bảng B và ngược lại, thường được thực hiện thông qua bảng trung gian
*/

/* 
//////INSERT - UPDATE - DELETE/////////
- INSERT INTO: chèn dữ liệu
- UPDATE: cập nhật dữ liệu
- DELETE: xóa dữ liệu
- WHERE: điều kiện lọc dữ liệu
- JOIN: kết hợp dữ liệu từ nhiều bảng
*/

/* 
//// TRUY VẤN - SẮP XẾP - LIMIT DỮ LIỆU ////
- SELECT * FROM <table_name>: truy vấn tất cả các cột
- SELECT column1, column2 FROM <table_name>: truy vấn các cột cụ thể

- ORDER BY column1 ASC|DESC: sắp xếp dữ liệu theo cột (ASC: tăng dần, DESC: giảm dần) // Nếu ko ghi ASC hay DESC thì mặc định là ASC
- LIMIT number OFFSET number: giới hạn số lượng bản ghi trả về và bỏ qua một số bản ghi
- WHERE condition: điều kiện lọc dữ liệu

//// INNER JOIN VÀ LEFT JOIN TRONG SQL ////
- INNER JOIN: kết hợp dữ liệu từ hai bảng và chỉ trả về các bản ghi có giá trị khớp trong cả hai bảng
- LEFT JOIN: kết hợp dữ liệu từ hai bảng và trả về tất cả các bản ghi từ bảng bên trái, ngay cả khi không có bản ghi khớp trong bảng bên phải

*/
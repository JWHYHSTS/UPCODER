<?php
date_default_timezone_set('Asia/Ho_Chi_Minh');
// echo date('d/m/Y H:i:s'); --> Dùng để in ngày giờ hiện tại
session_start(); // Tạo phiên làm việc cho người dùng
ob_start(); // Bật bộ đệm đầu ra (tránh lỗi header, setcookie, session_start)

require_once 'config.php';
// require_once './modules/auth/login.php'; --> Ví dụ require file
require_once 'includes/connect.php'; // Nạp file kết nối database
require_once 'includes/database.php'; // Nạp file thao tác database
require_once 'includes/session.php'; // Nạp file thao tác session

// Nạp thư viện gửi email
require_once './includes/mailer/Exception.php';
require_once './includes/mailer/PHPMailer.php';
require_once './includes/mailer/SMTP.php';

require_once 'includes/functions.php'; // Nạp file hàm chung
// sendMail('haidangblck15@gmail.com', 'Test email', 'Đây là nội dung email'); // Gửi email test
// $rel = validateEmail('haidangblck15gmail.com'); --> Ví dụ validate email
// var_dump($rel); // In ra kết quả validate email
// $rel = validateInt('-5'); // Ví dụ validate int
// var_dump($rel); // In ra kết quả validate int
// $rel = isPhone('023456789'); // Ví dụ validate phone
// if($rel) {
//     echo 'SDT hợp lệ'; // In ra nếu đúng định dạng
// } else {
//     echo 'SDT không hợp lệ'; // In ra nếu sai định dạng
// }

// Hàm mã hóa và so sánh mật khẩu (password_hash, password_verify)
// $pass = 123456;
// $rel = password_hash($pass, PASSWORD_DEFAULT); // Mã hóa mật khẩu
// echo $rel. '<br>'; // In ra mật khẩu đã mã hóa

// $pass_user_input = '123456'; // Mật khẩu người dùng nhập vào
// $rel_2 = password_verify($pass_user_input, $rel); // So sánh mật khẩu người dùng nhập vào với mật khẩu đã mã hóa
// if($rel_2) {
//     echo 'Mật khẩu đúng'; // In ra nếu đúng mật khẩu
// } else {
//     echo 'Mật khẩu sai'; // In ra nếu sai mật khẩu
// }



// Sử dụng Session
// setSession('hai', 'Khóa học'); // Tạo session
// $a = getSession('hai'); // Lấy session
// echo $a; // In ra session
// echo '<pre>';
// print_r($_SESSION); // In ra tất cả session
// echo '</pre>';
// removeSession('hai'); // Xóa session
// setSessionFlash('msg', 'Đăng nhập thành công!'); // Tạo session flash
// $rel = getSessionFlash('msg'); // Lấy session flash
// echo $rel; // In ra session flash


// $data = [
//         'name' => 'Lập trình trên Windows',
//         'slug' => 'lap-trinh-windows',
//     ];


// $rel = getONE("SELECT * FROM course"); // Ví dụ lấy tất cả dữ liệu từ bảng users
// echo '<pre>';
// print_r($rel); // In ra mảng dữ liệu
// echo '</pre>';
// die();

// insert('course_category', $data); // Ví dụ chèn dữ liệu vào bảng users

// $condition = "id = 4";
// update('course_category', $data, $condition); // Ví dụ cập nhật dữ liệu bảng users với điều kiện id = 1

// $condition = 'id = 1';
// delete('users', $condition); // Ví dụ xóa dữ liệu bảng users với điều kiện id = 1

// $rel = getRows("SELECT * FROM course"); // Ví dụ đếm số dòng trả về từ bảng course
// echo $rel; // In ra số dòng

//insert('course_category', $data); // Ví dụ chèn dữ liệu vào bảng course_category
//$rel = lastID(); // Ví dụ lấy ID mới nhất
//echo $rel; // In ra số dòng

// echo _MODULES . 'và' . _ACTION; --> Dùng để kiểm tra hằng số và in ra: _MODULES = dashboard và _ACTION = index
$module = _MODULES; // Dùng để lấy giá trị modules mặc định
$action = _ACTION; // Dùng để lấy giá trị action mặc định

if(!empty($_GET['module'])) {
    $module = $_GET['module']; // Lấy giá trị modules từ URL
}

if(!empty($_GET['action'])) {
    $action = $_GET['action']; // Lấy giá trị action từ URL
}

$path = 'modules/' . $module . '/' . $action . '.php'; // Tạo đường dẫn file
// echo $path . '<br>'; // Dùng để kiểm tra đường dẫn file

// Nếu nhập là localhost/manager_course/ --> Hiện trang tổng quan
// Nếu nhập là localhost/manager_course/?modules=auth&action=login --> Báo lỗi 404 vì file không tồn tại
// Nếu nhập là localhost/manager_course/?module=students --> Hiện trang quản lý học viên
// Nếu nhập là localhost/manager_course/?module=students&action=login --> Hiện trang login

if(!empty($path)){
    if(file_exists($path)){
        // echo 'Kết nối thành công! <br>'; // Dùng để kiểm tra file có tồn tại
        require_once $path; // Nạp file nếu tồn tại file --> Nếu file tồn tại thì sẽ hiện thì nội dung file ra là $module = dashboard và $action = index
    } else{
        // echo 'Lỗi xin vui lòng thử lại sau!'; // Báo lỗi nếu file không tồn tại
        require_once 'modules/errors/404.php'; // Nạp file lỗi 404
    }
}else{
    // echo 'Truy cập lỗi';
    require_once 'modules/errors/500.php'; // Nạp file lỗi 500
}
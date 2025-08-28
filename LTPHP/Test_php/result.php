<?php

// if(!empty($_GET)){
//     echo '<pre>';
//     print_r($_GET);
//     echo '</pre>';
// }

// if(!empty($_POST)){
//     echo '<pre>';
//     print_r($_POST);
//     echo '</pre>';
// }

// $fullname = "";
// $email = "";
// $password = "";
// $error_fullname = "";
// $error_email = "";
// $error_password = "";

// if($_SERVER['REQUEST_METHOD'] == "POST"){
//     if(empty($fullname)){
//         $error_fullname = "Vui lòng nhập tên.";
//     }else{
//         $fullname = htmlspecialchars(trim($_POST['fullname']));
//     }
//     if(empty($email)){
//         $error_email = "Vui lòng nhập email.";
//     }else{
//         if(!filter_var($email, FILTER_VALIDATE_EMAIL)){
//             $error_email = "Email không hợp lệ.";
//         }else{
//             $email = htmlspecialchars(trim($_POST['email']));
//         }
//     }
//     if(empty($password)){
//         $error_password = "Vui lòng nhập mật khẩu.";
//     }else{
//         $password = htmlspecialchars(trim($_POST['password']));
//     }

//     // In ra lỗi nếu có
//     if($error_fullname == ""){
//         echo 'Dữ liệu hợp lệ: ' . $fullname. '<br>';
//     }else{
//         echo $error_fullname;
//     }

//     if($error_email == ""){
//         echo 'Dữ liệu hợp lệ: ' . $email. '<br>';
//     }else{
//         echo $error_email;
//     }

//     if($error_password == ""){
//         echo 'Dữ liệu hợp lệ: ' . $password. '<br>';
//     }else{
//         echo $error_password;
//     }
// }


// Xử lý Upload 

// echo '<pre>';
// print_r($_FILES);
// echo '</pre>';

// if($_SERVER['REQUEST_METHOD'] == "POST"){
//     $file = $_FILES['file_upload'];
//     $filename = uniqid() . '_' . $file['name'];
//     $fileTmp = $file['tmp_name'];
//     $fileError = $file['error'];

//     if($fileError == 0){
//         $target = "./uploads/"; // Địa chỉ lưu ảnh upload
//         // Di chuyển file lưu ảnh upload vào thư mục uploads
//         if(move_uploaded_file($fileTmp, $target . $filename)){
//             echo 'Upload thành công. <a href="' . $target . $filename . '" target="_blank">Xem file</a>';
//         }else{
//             echo 'Upload thất bại.';
//         }
//         // move_uploaded_file($fileTmp, $target . $filename);
//     }else{
//         echo 'Có lỗi xảy ra khi upload file.';
//     }
// }



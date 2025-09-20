<?php
if(!defined('_HD')) {
    die('Bạn không có quyền truy cập!');
}

try {
    $option = array (
        PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES utf8", // Thiết lập mã hóa ký tự UTF-8, hỗ trợ tiếng Việt
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION // Thiết lập chế độ báo lỗi, đẩy lỗi ra ngoại lệ
    );
    $dsn = _DRIVER . ':host=' . _HOST . ";dbname=" . _DB; 
    $conn = new PDO($dsn, _USER, _PASS, $option);
    
}catch (Exception $ex) {
    echo "Lỗi kết nối: " . $ex->getMessage();
}
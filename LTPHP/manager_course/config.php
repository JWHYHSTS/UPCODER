<?php
const _HD = true; // Định nghĩa hằng số để chống truy cập trực tiếp
// echo _HD; // In ra hằng số để kiểm tra: 1 -> true, 0 hoặc ko hiện gì -> false

const _MODULES = 'dashboard';
const _ACTION = 'index';

// Khai báo database
const _HOST = 'localhost';
const _DB = 'manager_haidang';
const _USER = 'root';
const _PASS = '';
const _DRIVER = 'mysql'; // mysql, pgsql, sqlite, sqlsrv

// Debug error
const _DEBUG = true; // Bật chế độ debug

// Thiết lập host
define ('_HOST_URL', 'http://'. $_SERVER['HTTP_HOST']. '/manager_course/'); // Đường dẫn gốc của website
define ('_HOST_URL_TEMPLATES', _HOST_URL . 'templates/'); // Đường dẫn gốc của thư mục templates

// echo _HOST_URL_TEMPLATES; // In ra hằng số để kiểm tra
// Thiết lập path
define('_PATH_URL', __DIR__. '/'); // Đường dẫn tuyệt đối của website
define('_PATH_URL_TEMPLATES', _PATH_URL . 'templates/'); // Đường dẫn tuyệt đối của thư mục templates


// echo _HOST_URL . '<br>'; // In ra là http://localhost/manager_course/
// echo _HOST_URL_TEMPLATES . '<br>'; // In ra là http://localhost/manager_course/templates/
// echo _PATH_URL . '<br>'; // In ra là C:\xampp\htdocs\manager_course/
// echo _PATH_URL_TEMPLATES . '<br>'; // In ra là C:\xampp\htdocs\manager_course\templates/

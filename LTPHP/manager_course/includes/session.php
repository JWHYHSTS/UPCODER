<?php
if(!defined('_HD')) {
    die('Bạn không có quyền truy cập!');
}

// Set session
function setSession($key, $value) {
    if(!empty(session_id())) {
        $_SESSION[$key] = $value;
        return true;
    }
    return false;
}

// Lấy dữ liệu session
function getSession($key='') {
    if(empty($key)) {
        return $_SESSION;
    }else{
        if(isset($_SESSION[$key])) {
            return $_SESSION[$key];
        }
    }
    return false;
}

// Xóa session
function removeSession($key='') {
    if(empty($key)) {
        session_destroy();
        return true;
    }else{
        if(isset($_SESSION[$key])) {
            unset($_SESSION[$key]);
            return true;
        }
    }
    return false;
}

// Tạo session flash
function setSessionFlash($key, $value) {
    $key = $key . 'Flash';
    $rel = setSession($key, $value);
    return $rel;
}

// Lấy session flash
function getSessionFlash($key) {
    $key = $key . 'Flash';
    $rel = getSession($key);
    if($rel) {
        removeSession($key);
        return $rel;
    }
    return false;
}


<?php
if(!defined('_HD')) {
    die('Bạn không có quyền truy cập!');
}

// Truy vấn tất cả dữ liệu
function getAll($sql){
    global $conn; // Sử dụng biến toàn cục $conn từ file config.php
    $stmt = $conn->prepare($sql); // Chuẩn bị câu lệnh SQL
    $stmt->execute(); // Thực thi câu lệnh SQL
    $result = $stmt->fetchAll(PDO::FETCH_ASSOC); 
    return $result; // Trả về mảng kết quả
}

// Đếm số dòng trả về
function getRows($sql){
    global $conn; // Sử dụng biến toàn cục $conn từ file config.php
    
    $stmt = $conn->prepare($sql); // Chuẩn bị câu lệnh SQL
    $stmt->execute(); // Thực thi câu lệnh SQL
    $count = $stmt->rowCount(); // Đếm số dòng trả về
    return $count; // Trả về số dòng
}


// Truy vấn một bản ghi
function getOne($sql){
    global $conn; // Sử dụng biến toàn cục $conn từ file config.php
    
    $stmt = $conn->prepare($sql); // Chuẩn bị câu lệnh SQL
    $stmt->execute(); // Thực thi câu lệnh SQL
    $result = $stmt->fetch(PDO::FETCH_ASSOC); 
    return $result; // Trả về mảng kết quả
}

// Insert dữ liệu
function insert($table, $data){
    /*
    $data = [
        'name' => 'Phat',
        'email' => 'phat@example.com',
        'phone' => '023456789'
    ]; --> Ví dụ mảng dữ liệu truyền vào hàm insert
    */
    global $conn; // Sử dụng biến toàn cục $conn từ file config.php
    $keys = array_keys($data); // Lấy tất cả key của mảng $data
    $cot = implode(', ', $keys); // Chuyển mảng thành chuỗi, ngăn cách bởi dấu phẩy
    $place = ':' . implode (', :', $keys); // Tạo chuỗi placeholder: :name, :email, :phone

    $sql = "INSERT INTO $table($cot) VALUES ($place)"; // :name --> placeholder
    // echo $sql; // Dùng để kiểm tra câu lệnh SQL
    
    $stmt = $conn->prepare($sql); // Chuẩn bị câu lệnh SQL (tránh SQL injection) // $stmt nghĩa là statement dùng để thực thi câu lệnh SQL

    $rel = $stmt->execute($data); // Thực thi câu lệnh SQL

    return $rel;
}

// Update dữ liệu
function update($table, $data, $condition = ''){
    global $conn; // Sử dụng biến toàn cục $conn từ file config.php
    $update = '';

    foreach($data as $key => $value){
        $update .= "$key=:$key,"; // name = :name, email = :email, phone = :phone,
    }
    $update = trim($update, ','); // Loại bỏ dấu phẩy cuối cùng
    
    // $sql = "UPDATE class SET name = :name WHERE id = :id";
    
    if(!empty ($condition)){
        $sql = "UPDATE $table SET $update WHERE $condition";
    }else{
        $sql = "UPDATE $table SET $update";
    }
    // Chuẩn bị câu lệnh SQL
    $tmp = $conn->prepare($sql); // $tmp nghĩa là template dùng để thực thi câu lệnh SQL
    // Thực thi câu lệnh SQL
    $rel = $tmp->execute($data); 
    return $rel;
}


// Xóa dữ liệu
function delete($table, $condition = ''){
    global $conn; // Sử dụng biến toàn cục $conn từ file config.php
    if(!empty($condition)){
        $sql = "DELETE FROM $table WHERE $condition";
    } else{
        $sql = "DELETE FROM $table";
    }
    $stmt = $conn->prepare($sql); // Chuẩn bị câu lệnh SQL
    $rel = $stmt->execute(); // Thực thi câu lệnh SQL
    return $rel;
}


// Hàm lấy ID dữ liệu mới insert
function lastID(){
    global $conn; // Sử dụng biến toàn cục $conn từ file config.php
    return $conn->lastInsertId(); // Trả về ID mới nhất
} 
<?php
if(!defined('_HD')) {
    die('Bạn không có quyền truy cập!');
}

$data = [
    'title' => 'Đăng ký tài khoản'
];
layout('header-auth', $data); // Nạp file header

// Khởi tạo mặc định để tránh Warning khi không phải POST
$msg = '';
$msg_type = '';
$errorArr = [];
$oldData = [];

if(isPOST()){
  $filter = filterData();
  $errors = [];

  // Validate fullname
  if(empty(trim($filter['fullname']))){
    $errors['fullname']['required'] = 'Họ và tên không được để trống';
  }else{
    if(strlen(trim($filter['fullname'])) < 5){
      $errors['fullname']['length'] = 'Họ và tên phải có ít nhất 5 ký tự';
    }
  }
  // Validate email
  if(empty(trim($filter['email']))){
    $errors['email']['required'] = 'Email không được để trống';
  }else{
    if(!validateEmail(trim($filter['email']))){
      $errors['email']['isEmail'] = 'Email không đúng định dạng';
    }else{
      $email = $filter['email'];
      $checkEmail = getRows("SELECT * FROM users WHERE email = '$email'");
      if($checkEmail > 0){
        $errors['email']['exits'] = 'Email đã tồn tại';
      }
    }
  }
  // Validate phone
  if(empty(trim($filter['phone']))){
    $errors['phone']['required'] = 'Số điện thoại không được để trống';
  }else{
    if(!isPhone(trim($filter['phone']))){
      $errors['phone']['isPhone'] = 'Số điện thoại không đúng định dạng'; 
    }else{
      $phone = $filter['phone'];
      $checkPhone = getRows("SELECT * FROM users WHERE phone = '$phone'");
      if($checkPhone > 0){
        $errors['phone']['exits'] = 'Số điện thoại đã tồn tại';
      }
    }
  }

  // Validate password
  if(empty(trim($filter['password'] ?? ''))){
    $errors['password']['required'] = 'Mật khẩu không được để trống';
  }else{
    if(strlen(trim($filter['password'] ?? '')) < 6){
      $errors['password']['length'] = 'Mật khẩu phải có ít nhất 6 ký tự';
    }
  }
  // Validate confirm_pass
  if(empty(trim($filter['confirm_pass'] ?? ''))){
    $errors['confirm_pass']['required'] = 'Nhập lại mật khẩu không được để trống';
  }else{
    if(trim($filter['confirm_pass'] ?? '') !== trim($filter['password'] ?? '')){
      $errors['confirm_pass']['match'] = 'Nhập lại mật khẩu không khớp';
    }
  }


  if(empty($errors)){
    // table: users
    $activeToken = sha1(uniqid().time());
    $data = [
      'fullname' => trim($filter['fullname']),
      'email' => trim($filter['email']),
      'phone' => trim($filter['phone']),
      'password' => password_hash(trim($filter['password']), PASSWORD_DEFAULT),
      'address' => trim($filter['address'] ?? ''),
      'active_token' => $activeToken,
      'group_id' => 1, // Mặc định nhóm khách hàng
      'created_at' => date('Y-m-d H:i:s'),

    ];

    $insertStatus = insert('users', $data);
    
    if($insertStatus){
      // Các bước gửi email kích hoạt tài khoản
      $emailTo = $filter['email'];
      $subject = 'Kích hoạt tài khoản';
      $content = '<p>Chào bạn '.$filter['fullname'].'</p>';
      $content .= '<p>Bạn vui lòng click vào đường link bên dưới để kích hoạt tài khoản:</p>';
      $content .= '<p><a href="'. _HOST_URL .'/?module=auth&action=active&token='.$activeToken.'">Kích hoạt tài khoản</a></p>';
      $content .= '<p>Cảm ơn bạn đã đăng ký!</p>';

      // Gửi email kích hoạt tài khoản
      sendMail($emailTo, $subject, $content);

      setSessionFlash('msg', 'Đăng ký tài khoản thành công. Vui lòng kiểm tra email để kích hoạt tài khoản!');
      setSessionFlash('msg_type', 'success');


      $msg = 'Đăng ký tài khoản thành công.';
      $msg_type = 'success';
    }else{
      setSessionFlash('msg', 'Đăng ký tài khoản không thành công. Vui lòng thử lại!');
      setSessionFlash('msg_type', 'danger');
    }

  }else{
    setSessionFlash('msg', 'Dữ liệu không hợp lệ, vui lòng kiểm tra lại thông tin');
    setSessionFlash('msg_type', 'danger');
    // Lưu dữ liệu cũ và mảng lỗi vào session
    setSessionFlash('oldData', $filter);
    setSessionFlash('errors', $errors);
  }
  
  $msg = getSessionFlash('msg');
  $msg_type = getSessionFlash('msg_type');
  $oldData = getSessionFlash('oldData');
  $errorArr = getSessionFlash('errors');
  

}

?>


<section class="vh-100">
  <div class="container-fluid h-custom">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-md-9 col-lg-6 col-xl-5">
        <img src="<?php echo _HOST_URL_TEMPLATES; ?>/assets/image/draw2.webp"
          class="img-fluid" alt="Sample image">
      </div>
      <div class="col-md-8 col-lg-6 col-xl-4 offset-xl-1">
        <?php if(!empty($msg) && !empty($msg_type)) getMsg($msg, $msg_type) ?>
        <form method="POST" action="" enctype="multipart/form-data">
          <div class="d-flex flex-row align-items-center justify-content-center justify-content-lg-start">
            <h2 class="fw-normal mb-5 me-3">Đăng ký tài khoản</h2>
          </div>

          <!-- Email input Name, email, sdt, mật khẩu, nhập lại mật khẩu -->
          <div data-mdb-input-init class="form-outline mb-4">
            <input name="fullname" type="text" value="<?php echo oldData($oldData, 'fullname'); ?>" class="form-control form-control-lg"
              placeholder="Họ và tên" />
              <?php 
              echo formError($errorArr, 'fullname');
              ?>
          </div>
            <!-- Email input -->
          <div data-mdb-input-init class="form-outline mb-4">
            <input name="email" type="text" value="<?php echo oldData($oldData, 'email'); ?>" class="form-control form-control-lg"
              placeholder="Địa chỉ email" />
              <?php 
              echo formError($errorArr, 'email');
              ?>
          </div>
          <!-- Số điện thoại input -->
          <div data-mdb-input-init class="form-outline mb-4">
            <input name="phone" type="text" value="<?php echo oldData($oldData, 'phone'); ?>" class="form-control form-control-lg"
              placeholder="Nhập số điện thoại" />
              <?php echo formError($errorArr, 'phone'); ?>
          </div>

          <!-- Password input -->
          <div data-mdb-input-init class="form-outline mb-3">
            <input name="password" type="password" value="" id="form3Example4" class="form-control form-control-lg" placeholder="Nhập mật khẩu" />
              <?php echo formError($errorArr, 'password'); ?>
          </div>
          <!-- Nhập lại mật khẩu input -->
          <div data-mdb-input-init class="form-outline mb-4">
            <input name="confirm_pass" type="password" value="" class="form-control form-control-lg" placeholder="Nhập lại mật khẩu" />
              <?php echo formError($errorArr, 'confirm_pass'); ?>
          </div>


          <div class="text-center text-lg-start mt-4 pt-2">
            <button  type="submit" data-mdb-button-init data-mdb-ripple-init class="btn btn-primary btn-lg"
              style="padding-left: 2.5rem; padding-right: 2.5rem;">Đăng ký</button>
            <p class="small fw-bold mt-2 pt-1 mb-0">Bạn đã có tài khoản? <a href="<?php echo _HOST_URL; ?>?module=auth&action=login"
                class="link-danger">Đăng nhập ngay</a></p>
          </div>

        </form>
      </div>
    </div>
  </div>
</section>
<?php
layout('footer'); // Nạp file footer
<?php
if (!defined('_HD')) {
  die('Bạn không có quyền truy cập!');
}
$data = [
  'title' => 'Đăng nhập hệ thống'
];
layout('header-auth', $data);

/* 
- Validate dữ liệu đầu vào
- Check dữ liệu với database
- Dữ liệu khớp --> tokenlogin --> insert vào token_login(kiểm tra đăng nhập ở các trang khác)
- Kiểm tra đăng nhập
  + Gán token login lên session
  + Trong header -> Lấy token từ session về và so khớp với token trong bảng token_login
  + Nếu khớp thì điều hướng trang đích (Không khớp thì xoá session và token_login)
- Điều hướng về trang quản trị
- Đăng nhập tài khoản ở 1 nơi tại 1 thời điểm.
*/

// Khởi tạo mặc định để tránh Warning khi không phải POST
$filter = [];
$errors = [];
$msg = '';
$msg_type = '';
$oldData = [];
$errorArr = [];


if (isPOST()) {
  $filter = filterData();
  $errors = [];

  // Validate email
  if (empty(trim($filter['email'] ?? ''))) {
    $errors['email']['required'] = 'Email không được để trống';
  } else {
    if (!validateEmail(trim($filter['email']))) {
      $errors['email']['isEmail'] = 'Email không đúng định dạng';
    }
  }

  // Validate password
  if (empty(trim($filter['password'] ?? ''))) {
    $errors['password']['required'] = 'Mật khẩu không được để trống';
  } else {
    if (strlen(trim($filter['password'] ?? '')) < 6) {
      $errors['password']['length'] = 'Mật khẩu phải có ít nhất 6 ký tự';
    }
  }

  if (empty($errors)) {

    $email = trim($filter['email'] ?? '');
    $password = $filter['password'] ?? '';

    // Kiểm tra email
    $checkEmail = getOne("SELECT * FROM users WHERE email = '$email'");
    if (!empty($checkEmail)) {
      // So sánh mật khẩu nhập với hash lưu trong DB
      $checkStatus = password_verify($password, $checkEmail['password']);
      if ($checkStatus) {

        // Tài khoản chỉ login 1 nơi
        $user_id = $checkEmail['id'];
        $checkAlready = getRows("SELECT * FROM token_login WHERE user_id = $user_id");
        if ($checkAlready > 0) {
          setSessionFlash('msg', 'Tài khoản đã đăng nhập ở nơi khác, vui lòng quay lại sau!');
          setSessionFlash('msg_type', 'danger');
          redirect('?module=auth&action=login');
        } else {
          // tạo token và insert vào token_login
          $token = sha1(uniqid() . time());

          // Gán token lên session
          setSessionFlash('token_login', $token);

          $data = [
            'token' => $token,
            'user_id' => $checkEmail['id'],
            'created_at' => date('Y-m-d H:i:s')
          ];

          $insertToken = insert('token_login', $data);
          if ($insertToken) {
            // Lưu token vào cookie (hoặc session tuỳ cách auth của bạn)
            setcookie('token_login', $token, time() + 30 * 24 * 3600, '/'); // ví dụ 30 ngày
            setSessionFlash('msg', 'Đăng nhập thành công.');
            setSessionFlash('msg_type', 'success');

            // redirect tới dashboard và exit
            header('Location: ./');
            exit;
          } else {
            setSessionFlash('msg', 'Đăng nhập không thành công, vui lòng thử lại!');
            setSessionFlash('msg_type', 'danger');
            header('Location: ' . _HOST_URL . '?module=auth&action=login');
            exit;
          }
        }
      } else {
        setSessionFlash('msg', 'Email hoặc mật khẩu không đúng!');
        setSessionFlash('msg_type', 'danger');
        header('Location: ' . _HOST_URL . '?module=auth&action=login');
        exit;
      }
    } else {
      setSessionFlash('msg', 'Email không tồn tại!');
      setSessionFlash('msg_type', 'danger');
      header('Location: ' . _HOST_URL . '?module=auth&action=login');
      exit;
    }

    // Post-Redirect-Get để tránh submit lại form
    header('Location: ' . _HOST_URL . '?module=auth&action=login');
    exit;
  } else {
    setSessionFlash('msg', 'Dữ liệu không hợp lệ, vui lòng kiểm tra lại!');
    setSessionFlash('msg_type', 'danger');
    setSessionFlash('oldData', $filter);
    setSessionFlash('errors', $errors);

    header('Location: ' . _HOST_URL . '?module=auth&action=login');
    exit;
  }

  // Lấy lại flash để hiển thị
  $msg = getSessionFlash('msg');
  $msg_type = getSessionFlash('msg_type');
  $oldData = getSessionFlash('oldData');
  $errorArr = getSessionFlash('errors');
} else {
  // Khi không phải POST vẫn muốn hiển thị flash nếu có
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
        <?php if (!empty($msg) && !empty($msg_type)) getMsg($msg, $msg_type) ?>
        <form method="POST" action="">
          <div class="d-flex flex-row align-items-center justify-content-center justify-content-lg-start">
            <h2 class="fw-normal mb-5 me-3">Đăng nhập hệ thống</h2>
          </div>

          <!-- Email input -->
          <div data-mdb-input-init class="form-outline mb-4">
            <input type="email" name="email" id="form3Example3" class="form-control form-control-lg"
              placeholder="Địa chỉ email" value="<?php echo oldData($oldData, 'email'); ?>" />
            <?php echo formError($errorArr, 'email'); ?>
          </div>

          <!-- Password input -->
          <div data-mdb-input-init class="form-outline mb-3">
            <input type="password" name="password" id="form3Example4" class="form-control form-control-lg"
              placeholder="Nhập mật khẩu" />
            <?php echo formError($errorArr, 'password'); ?>
          </div>

          <div class="d-flex justify-content-between align-items-center">
            <!-- Checkbox -->
            <a href="<?php echo _HOST_URL; ?>?module=auth&action=forgot" class="text-body">Quên mật khẩu?</a>
          </div>

          <div class="text-center text-lg-start mt-4 pt-2">
            <button type="submit" data-mdb-button-init data-mdb-ripple-init class="btn btn-primary btn-lg"
              style="padding-left: 2.5rem; padding-right: 2.5rem;">Đăng nhập</button>
            <p class="small fw-bold mt-2 pt-1 mb-0">Bạn chưa có tài khoản? <a href="<?php echo _HOST_URL; ?>?module=auth&action=register"
                class="link-danger">Đăng ký</a></p>
          </div>

        </form>
      </div>
    </div>
  </div>
</section>
<?php
layout('footer'); // Nạp file footer

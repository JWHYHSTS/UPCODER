<?php
if (!defined('_HD')) {
  die('Bạn không có quyền truy cập!');
}
$data = [
  'title' => 'Quên mật khẩu'
];
layout('header-auth', $data); // Nạp file header

// Khởi tạo để tránh undefined variable khi không phải POST
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
}


if (empty($errors)) {
  // Xử lý gửi email
  if (!empty($filter['email'])) {
    $email = trim($filter['email']);
    $checkEmail = getOne("SELECT * FROM users WHERE email = '$email'");
    if (!empty($checkEmail)) {
      // Update forget_token vào bảng users
      $forgot_token = sha1(uniqid() . time());
      $data = [
        'forget_token' => $forgot_token
      ];
      $condition = 'id=' . $checkEmail['id'];
      $updateStatus = update('users', $data, $condition);
      if ($updateStatus) {
        $emailTo = $email;
        $subject = 'Yêu cầu đặt lại mật khẩu';
        // Lấy tên hiển thị: ưu tiên fullname từ DB, nếu không có thì lấy phần trước @ của email
        $displayName = $checkEmail['fullname'] ?? $checkEmail['name'] ?? explode('@', $email)[0];
        $content = '<p>Chào bạn ' . htmlspecialchars($displayName, ENT_QUOTES, 'UTF-8') . '</p>';
        $content .= '<p>Bạn vui lòng click vào đường link bên dưới để đặt lại mật khẩu:</p>';
        $content .= '<p><a href="' . _HOST_URL . '/?module=auth&action=reset&token=' . $forgot_token . '">Đặt lại mật khẩu</a></p>';
        $content .= '<p>Nếu bạn không yêu cầu đặt lại mật khẩu, vui lòng bỏ qua email này.</p>';
        $content .= '<p>Trân trọng!</p>';

        // Gửi email kích hoạt tài khoản
        sendMail($emailTo, $subject, $content);

        setSessionFlash('msg', 'Gửi yêu cầu thành công! Vui lòng kiểm tra email để đặt lại mật khẩu.');
        setSessionFlash('msg_type', 'success');
      }else{
        setSessionFlash('msg', 'Có lỗi xảy ra, vui lòng thử lại!');
        setSessionFlash('msg_type', 'danger');
      }
    }
  }
} else {
  setSessionFlash('msg', 'Vui lòng kiểm tra lại dữ liệu nhập vào');
  setSessionFlash('msg_type', 'danger');
  setSessionFlash('oldData', $filter);
  setSessionFlash('errors', $errors);
}


$msg = getSessionFlash('msg');
$msg_type = getSessionFlash('msg_type');
$oldData = getSessionFlash('oldData');
$errorArr = getSessionFlash('errors');





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
        <form method="POST" action="" enctype="multipart/form-data">
          <div class="d-flex flex-row align-items-center justify-content-center justify-content-lg-start">
            <h2 class="fw-normal mb-5 me-3">Quên mật khẩu</h2>

          </div>

          <!-- Email input -->
          <div data-mdb-input-init class="form-outline mb-4">
            <input type="email" name="email" value="<?php echo oldData($oldData, 'email'); ?>" id="form3Example3" class="form-control form-control-lg"
              placeholder="Địa chỉ email" />
            <?php
            if (!empty($errorArr['email'])) {
              echo formError($errorArr, 'email');
            }
            ?>
          </div>




          <div class="text-center text-lg-start mt-4 pt-2">
            <button type="submit" data-mdb-button-init data-mdb-ripple-init class="btn btn-primary btn-lg"
              style="padding-left: 2.5rem; padding-right: 2.5rem;">Gửi yêu cầu</button>
            <p class="small fw-bold mt-2 pt-1 mb-0">Bạn đã có tài khoản? <a href="<?php echo _HOST_URL; ?>?module=auth&action=login"
                class="link-danger">Đăng nhập ngay</a></p>
          </div>

        </form>
      </div>
    </div>
  </div>
</section>
<?php
// require_once './templates/layouts/footer.php'; // Nạp file footer
layout('footer'); // Nạp file footer
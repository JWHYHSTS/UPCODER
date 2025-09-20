<?php
if (!defined('_HD')) {
  die('Bạn không có quyền truy cập!');
}
$data = [
  'title' => 'Đặt lại mật khẩu'
];
layout('header-auth', $data); // Nạp file header
// Khai báo biến để tránh lỗi undefined variable
$msg = '';
$msg_type = '';
$errors = [];
$filter = [];


$filterGet = filterData('get');

$tokenReset = $filterGet['token'] ?? '';

if (!empty($tokenReset)) {
  // check token hợp lệ
  $checkToken = getOne("SELECT * FROM users WHERE forget_token='$tokenReset'");
  if (!empty($checkToken)) {
    if (isPOST()) {
      $filter = filterData();
      $errors = [];

      // Validate password mới
      if (empty(trim($filter['password'] ?? ''))) {
        $errors['password']['required'] = 'Mật khẩu không được để trống';
      } else {
        if (strlen(trim($filter['password'] ?? '')) < 6) {
          $errors['password']['length'] = 'Mật khẩu phải có ít nhất 6 ký tự';
        }
      }
      // Validate nhập lại password mới
      if (empty(trim($filter['confirm_pass'] ?? ''))) {
        $errors['confirm_pass']['required'] = 'Nhập lại mật khẩu không được để trống';
      } else {
        if (trim($filter['confirm_pass'] ?? '') !== trim($filter['password'] ?? '')) {
          $errors['confirm_pass']['match'] = 'Nhập lại mật khẩu không khớp';
        }
      }

      // Hiển thị thông báo flash khi có lỗi validate
      if (!empty($errors)) {
        $msg = 'Vui lòng kiểm tra lại dữ liệu nhập vào.';
        $msg_type = 'danger';
      }
    }

    if (isPOST() && empty($errors)) {
      // Xử lý đặt lại mật khẩu
      $password = password_hash(trim($filter['password']), PASSWORD_DEFAULT);
      $dataUpdate = [
        'password' => $password,
        'forget_token' => null,
        'updated_at' => date('Y-m-d H:i:s')
      ];
      $condition = 'id=' . intval($checkToken['id']);
      $updateStatus = update('users', $dataUpdate, $condition);
      if ($updateStatus) {
        // Gửi mail thông báo (lấy email từ bản ghi $checkToken)
        $emailTo = $checkToken['email'] ?? '';
        if (!empty($emailTo)) {
          $subject = 'Đặt lại mật khẩu thành công';
          $content = '<p>Chào bạn,</p>';
          $content .= '<p>Bạn đã đặt lại mật khẩu thành công.</p>';
          $content .= '<p>Nếu bạn không thực hiện hành động này, vui lòng liên hệ với chúng tôi.</p>';
          sendMail($emailTo, $subject, $content);
        }

        setSessionFlash('msg', 'Đặt lại mật khẩu thành công! Vui lòng đăng nhập.');
        setSessionFlash('msg_type', 'success');
        redirect('?module=auth&action=reset');
      } else {
        setSessionFlash('msg', 'Có lỗi xảy ra, vui lòng thử lại!');
        setSessionFlash('msg_type', 'danger');
      }
    }
  } else {
    getMsg('Liên kết không hợp lệ hoặc đã hết hạn!', 'danger');
  }
} else {
  getMsg('Liên kết không hợp lệ hoặc đã hết hạn!', 'danger');
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
        <form method="POST" action="" enctype="multipart/form-data">
          <div class="d-flex flex-row align -items-center justify-content-center justify-content-lg-start">
            <h2 class=" fw-normal mb-5 me-3">Đặt lại mật khẩu</h2>

          </div>

          <!-- Password mới input -->
          <div data-mdb-input-init class="form-outline mb-4">
            <input type="password" name="password" id="form3Example4" class="form-control form-control-lg"
              placeholder="Nhập mật khẩu mới" />
            <?php
            if (!empty($errors['password'])) {
              echo formError($errors, 'password');
            }
            ?>
          </div>

          <!-- Nhập lại mật khẩu mới input -->
          <div data-mdb-input-init class="form-outline mb-4">
            <input type="password" name="confirm_pass" id="form3Example5" class="form-control form-control-lg"
              placeholder="Nhập lại mật khẩu mới" />
            <?php
            if (!empty($errors['confirm_pass'])) {
              echo formError($errors, 'confirm_pass');
            }
            ?>
          </div>

          <div class="text-center text-lg-start mt-4 pt-2">
            <button type="submit" data-mdb-button-init data-mdb-ripple-init class="btn btn-primary btn-lg"
              style="padding-left: 2.5rem; padding-right: 2.5rem;">Gửi</button>
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
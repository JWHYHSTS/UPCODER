<?php
if(!defined('_HD')) {
    die('Bạn không có quyền truy cập!');
}
// require_once './templates/layouts/header-auth.php'; // Nạp file header
$data = [
    'title' => 'Kích hoạt tài khoản'
];
layout('header-auth', $data); // Nạp file header
?>



<section class="vh-100">
  <div class="container-fluid h-custom">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col-md-9 col-lg-6 col-xl-5">
        <img src="<?php echo _HOST_URL_TEMPLATES; ?>/assets/image/draw2.webp"
          class="img-fluid" alt="Sample image">
      </div>
      <div class="col-md-8 col-lg-6 col-xl-4 offset-xl-1">
        <form>
          <div class="d-flex flex-column align-items-center justify-content-center text-center">
            <h2 class="fw-normal mb-4">Kích hoạt tài khoản thành công</h2>
            <a href="<?php echo _HOST_URL; ?>?module=auth&action=login" class="mt-2">
              <button type="button" class="btn btn-primary btn-lg px-4">Đăng nhập ngay</button>
            </a>
          </div>
        </form>
      </div>
    </div>
  </div>
</section>
<?php
// require_once './templates/layouts/footer.php'; // Nạp file footer
layout('footer'); // Nạp file footer
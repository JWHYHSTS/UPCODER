<?php
if (!defined('_HD')) {
    die('Bạn không có quyền truy cập!');
}
?>
<!--begin::Sidebar-->
<aside class="app-sidebar bg-body-secondary shadow" data-bs-theme="dark">
    <!--begin::Sidebar Brand-->
    <div class="sidebar-brand">
        <!--begin::Brand Link-->
        <a href="./index.html" class="brand-link">
            <!--begin::Brand Image-->
            <img
                src="data:image/png;base64,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"
                alt="AdminLTE Logo"
                class="brand-image opacity-75 shadow" />
            <!--end::Brand Image-->
            <!--begin::Brand Text-->
            <span class="brand-text fw-light">LC</span>
            <!--end::Brand Text-->
        </a>
        <!--end::Brand Link-->
    </div>
    <!--end::Sidebar Brand-->
    <!--begin::Sidebar Wrapper-->
    <div class="sidebar-wrapper">
        <nav class="mt-2">
            <!--begin::Sidebar Menu-->
            <ul
                class="nav sidebar-menu flex-column"
                data-lte-toggle="treeview"
                role="navigation"
                aria-label="Main navigation"
                data-accordion="false"
                id="navigation">
                <li class="nav-item menu-open">
                    <a href="#" class="nav-link active">
                        <i class="nav-icon bi bi-speedometer"></i>
                        <p>
                            Dashboard
                        </p>
                    </a>

                </li>
                <li class="nav-item">
                    <a href="#" class="nav-link">
                        <i class="nav-icon bi bi-box-seam-fill"></i>
                        <p>
                            Khóa học
                            <i class="nav-arrow bi bi-chevron-right"></i>
                        </p>
                    </a>
                    <ul class="nav nav-treeview">
                        <li class="nav-item">
                            <a href="./widgets/small-box.html" class="nav-link">
                                <i class="nav-icon bi bi-circle"></i>
                                <p>Danh sách</p>
                            </a>
                        </li>
                        <li class="nav-item">
                            <a href="./widgets/info-box.html" class="nav-link">
                                <i class="nav-icon bi bi-circle"></i>
                                <p>Thêm khóa học mới</p>
                            </a>
                        </li>
                        <li class="nav-item">
                            <a href="./widgets/cards.html" class="nav-link">
                                <i class="nav-icon bi bi-circle"></i>
                                <p>Lĩnh vực</p>
                            </a>
                        </li>
                    </ul>
                </li>
                <li class="nav-item">
                    <a href="#" class="nav-link">
                        <i class="nav-icon bi bi-clipboard-fill"></i>
                        <p>
                            Quản lý tài khoản
                            <i class="nav-arrow bi bi-chevron-right"></i>
                        </p>
                    </a>
                    <ul class="nav nav-treeview">
                        <li class="nav-item">
                            <a href="./layout/unfixed-sidebar.html" class="nav-link">
                                <i class="nav-icon bi bi-circle"></i>
                                <p>Danh sách tài khoản</p>
                            </a>
                        </li>
                        <li class="nav-item">
                            <a href="./layout/fixed-sidebar.html" class="nav-link">
                                <i class="nav-icon bi bi-circle"></i>
                                <p>Tạo mới tài khoản</p>
                            </a>
                    </ul>
                </li>
                <li class="nav-item">
                    <a href="#" class="nav-link">
                        <i class="nav-icon bi bi-pencil-square"></i>
                        <p>
                            Học viên
                            <i class="nav-arrow bi bi-chevron-right"></i>
                        </p>
                    </a>
                    <ul class="nav nav-treeview">
                        <li class="nav-item">
                            <a href="./forms/general.html" class="nav-link">
                                <i class="nav-icon bi bi-circle"></i>
                                <p>Danh sách</p>
                            </a>
                        </li>
                    </ul>
                </li>
            </ul>
            <!--end::Sidebar Menu-->
        </nav>
    </div>
    <!--end::Sidebar Wrapper-->
</aside>
<!--end::Sidebar-->
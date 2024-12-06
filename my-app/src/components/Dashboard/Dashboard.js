import React, { useEffect, useState } from "react";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
    faUserEdit,
    faCommentDots,
    faListUl,
    faSignOutAlt,
} from "@fortawesome/free-solid-svg-icons";
import { useNavigate } from "react-router-dom";

const UserDashboard = () => {
    const [userData, setUserData] = useState({});
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const navigate = useNavigate();

    useEffect(() => {
        const fetchUserData = async () => {
            const token = localStorage.getItem("token");
            const username = localStorage.getItem("username");

            // اگر توکن یا یوزرنیم موجود نیست
            if (!token || !username) {
                setError("کاربر احراز هویت نشده است. لطفا وارد شوید.");
                navigate("/login");
                return;
            }

            try {
                const response = await axios.get(
                    `http://127.0.0.1:8000/user_management/users/fetch-by-username/?username=${username}`,
                    {
                        headers: {
                            Authorization: `Bearer ${token}`,
                        },
                    }
                );
                setUserData(response.data);
            } catch (err) {
                if (err.response) {
                    setError(`خطا: ${err.response.status} - ${err.response.data.detail || "خطای ناشناخته"}`);
                } else if (err.request) {
                    setError("پاسخی از سمت سرور دریافت نشد. لطفا اتصال اینترنت خود را بررسی کنید.");
                } else {
                    setError(`خطا در ارسال درخواست: ${err.message}`);
                }
                console.error("Fetch Error:", err);
            } finally {
                setLoading(false);
            }
        };

        fetchUserData();
    }, [navigate]);

    const handleLogout = () => {
        localStorage.removeItem("token");
        localStorage.removeItem("username");
        navigate("/login");
    };

    if (loading) return <p>در حال بارگذاری...</p>;
    if (error) return <p style={{ color: "red" }}>{error}</p>;

    return (
        <div className="container-fluid" style={{ direction: "rtl" }}>
            <div className="row min-vh-10">
                {/* ستون کناری */}
                <aside className="col-12 col-md-3 bg-dark text-white p-3">
                    <div className="text-center mb-4">
                        <img
                            src="https://via.placeholder.com/80"
                            alt="User"
                            className="rounded-circle mb-2"
                        />
                        <h5>{userData.username}</h5>
                        <p>{userData.email}</p>
                    </div>
                    <nav className="navbar navbar-expand-md navbar-dark bg-dark border-dark">
                        <button
                            className="navbar-toggler mb-1"
                            type="button"
                            data-bs-toggle="collapse"
                            data-bs-target="#sidebarMenu"
                            aria-controls="sidebarMenu"
                            aria-expanded="false"
                            aria-label="Toggle navigation"
                        >
                            <span className="navbar-toggler-icon"></span>
                        </button>
                        <div className="collapse navbar-collapse" id="sidebarMenu">
                            <ul className="nav flex-column">
                                <li className="nav-item">
                                    <a href="#" className="nav-link text-white d-flex align-items-center gap-2">
                                        <FontAwesomeIcon icon={faUserEdit} />
                                        ویرایش پروفایل
                                    </a>
                                </li>
                                <li className="nav-item">
                                    <a href="#" className="nav-link text-white d-flex align-items-center gap-2">
                                        <FontAwesomeIcon icon={faCommentDots} />
                                        ثبت نظر
                                    </a>
                                </li>
                                <li className="nav-item">
                                    <a href="#" className="nav-link text-white d-flex align-items-center gap-2">
                                        <FontAwesomeIcon icon={faListUl} />
                                        لیست نظرات
                                    </a>
                                </li>
                                <li className="nav-item">
                                    <button
                                        onClick={handleLogout}
                                        className="nav-link text-white d-flex align-items-center gap-2 bg-transparent border-0"
                                    >
                                        <FontAwesomeIcon icon={faSignOutAlt} />
                                        خروج
                                    </button>
                                </li>
                            </ul>
                        </div>
                    </nav>
                </aside>

                {/* محتوای اصلی */}
                <main className="col-12 col-md-9 bg-light p-4">
                    <h4>داشبورد کاربری</h4>
                    <div className="card mb-4 p-3">
                        <h5 className="card-title">مشخصات کاربر</h5>
                        <div className="card-body">
                            <p><strong>یوزرنیم:</strong> {userData.username}</p>
                            <p><strong>ایمیل:</strong> {userData.email}</p>
                        </div>
                    </div>
                </main>
            </div>
        </div>
    );
};

export default UserDashboard;

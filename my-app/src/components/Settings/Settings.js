import React, { useState } from "react";
import { Container, Row, Col, Tab, Form, Button, Table } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faChartBar, faUsers, faCommentDots, faCog, faSignOutAlt } from "@fortawesome/free-solid-svg-icons";
import { useNavigate } from 'react-router-dom';

const SettingsPage = () => {
  const [activeTab, setActiveTab] = useState("settings");
  const [categories, setCategories] = useState([]);
  const [newCategory, setNewCategory] = useState("");

  const handleAddCategory = () => {
    if (newCategory) {
      setCategories([...categories, newCategory]);
      setNewCategory("");
    }
  };

  const navigate = useNavigate();

  const handleUserManagement = () => {
    navigate('/UserManagement');
  };

  return (
    <Container fluid className="mt-4" dir="rtl">
      <Row className="min-vh-100">
        {/* Sidebar */}
        
        <Col md={3} className="bg-dark text-white p-3">
          <div className="text-center mb-4">
            <h4>مدیر سیستم</h4>
            <p>نقش: مدیر</p>
          </div>
          <nav>
            <ul className="nav flex-column">
            <li className="nav-item mb-3">
                <a
                  href="#"
                  className="nav-link text-white d-flex align-items-center gap-2"
                  onClick={() => setActiveTab("pages")}
                >
                  <FontAwesomeIcon icon={faChartBar} />
                  داشبورد
                </a>
              </li>
              <li className="nav-item mb-3">
                <a
                  href="#"
                  className="nav-link text-white d-flex align-items-center gap-2"
                  onClick={() => setActiveTab("pages")}
                >
                  <FontAwesomeIcon icon={faChartBar} />
                  مدیریت کاربران
                </a>
              </li>
              <li className="nav-item mb-3">
                <a
                  href="#"
                  className="nav-link text-white d-flex align-items-center gap-2"
                  onClick={() => setActiveTab("pages")}
                >
                  <FontAwesomeIcon icon={faChartBar} />
                  مدیریت نظرات
                </a>
              </li>
              <li className="nav-item mb-3">
                <a
                  href="#"
                  className="nav-link text-white d-flex align-items-center gap-2"
                  onClick={() => setActiveTab("pages")}
                >
                  <FontAwesomeIcon icon={faChartBar} />
                  مدیریت سایت
                </a>
              </li>
              <li className="nav-item mb-3">
                <a
                  href="#"
                  className="nav-link text-white d-flex align-items-center gap-2"
                  onClick={() => setActiveTab("pages")}
                >
                  <FontAwesomeIcon icon={faChartBar} />
                  گزارش ها
                </a>
              </li>
              <li className="nav-item mb-3">
                <a
                  href="#"
                  className={`nav-link text-white d-flex align-items-center gap-2 ${activeTab === "settings" ? "bg-primary" : ""}`}
                  onClick={() => setActiveTab("settings")}
                >
                  <FontAwesomeIcon icon={faCog} />
                  تنظیمات 
                </a>
              </li>
              <li className="nav-item mb-3">
                <a
                  href="#"
                  className="nav-link text-white d-flex align-items-center gap-2"
                  onClick={() => setActiveTab("categories")}
                >
                  <FontAwesomeIcon icon={faUsers} />
                  تعریف دسته‌بندی‌ها
                </a>
              </li>
               <li className="nav-item">
                <a
                  href="#"
                  className="nav-link text-white d-flex align-items-center gap-2"
                >
                  <FontAwesomeIcon icon={faSignOutAlt} />
                  خروج
                </a>
              </li>
            </ul>
          </nav>
        </Col>

        {/* Main Content */}
        <Col md={9} className="bg-light p-4">
          <h2 className="text-center mb-4">صفحه تنظیمات</h2>
          <Tab.Container activeKey={activeTab}>
            <Tab.Content>
              {/* مدیریت صفحات */}
              <Tab.Pane eventKey="pages">
                <h4>مدیریت صفحات</h4>
                <Form>
                  <Form.Group controlId="contactUs">
                    <Form.Label>صفحه تماس با ما</Form.Label>
                    <Form.Control as="textarea" rows={3} placeholder="متن تماس با ما را وارد کنید..." />
                  </Form.Group>
                  <Button variant="primary" className="mt-2">ذخیره تغییرات</Button>
                </Form>
              </Tab.Pane>

              {/* تعریف دسته‌بندی‌ها */}
              <Tab.Pane eventKey="categories">
                <h4>تعریف دسته‌بندی‌ها</h4>
                <Form inline>
                  <Form.Control
                    type="text"
                    placeholder="نام دسته‌بندی جدید"
                    value={newCategory}
                    onChange={(e) => setNewCategory(e.target.value)}
                  />
                  <Button variant="success" className="ml-2" onClick={handleAddCategory}>
                    اضافه کردن
                  </Button>
                </Form>
                <Table striped bordered hover className="mt-3">
                  <thead>
                    <tr>
                      <th>#</th>
                      <th>نام دسته‌بندی</th>
                    </tr>
                  </thead>
                  <tbody>
                    {categories.map((category, index) => (
                      <tr key={index}>
                        <td>{index + 1}</td>
                        <td>{category}</td>
                      </tr>
                    ))}
                  </tbody>
                </Table>
              </Tab.Pane>
                    <Tab.Pane eventKey="settings">
                    <h4>تعریف دسته‌بندی‌ها</h4>
                <Form inline>
                  <Form.Control
                    type="text"
                    placeholder="نام دسته‌بندی جدید"
                    value={newCategory}
                    onChange={(e) => setNewCategory(e.target.value)}
                  />
                  <Button variant="success" className="ml-2" onClick={handleAddCategory}>
                    اضافه کردن
                  </Button>
                </Form>
                <Table striped bordered hover className="mt-3">
                  <thead>
                    <tr>
                      <th>#</th>
                      <th>نام دسته‌بندی</th>
                    </tr>
                  </thead>
                  <tbody>
                    {categories.map((category, index) => (
                      <tr key={index}>
                        <td>{index + 1}</td>
                        <td>{category}</td>
                      </tr>
                    ))}
                  </tbody>
                </Table>
                <h4>مدیریت گزارش‌ها</h4>
                <p>لیست گزارش‌های ارسال شده توسط کاربران:</p>
                <Table striped bordered hover>
                  <thead>
                    <tr>
                      <th>#</th>
                      <th>نوع گزارش</th>
                      <th>توضیحات</th>
                      <th>اقدام</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>1</td>
                      <td>کامنت</td>
                      <td>محتوای نامناسب</td>
                      <td>
                        <Button variant="danger" size="sm">حذف</Button>
                      </td>
                    </tr>
                    <tr>
                      <td>2</td>
                      <td>کاربر</td>
                      <td>حساب مشکوک</td>
                      <td>
                        <Button variant="warning" size="sm">بلاک</Button>
                      </td>
                    </tr>
                  </tbody>
                </Table>



                    </Tab.Pane>
              {/* مدیریت گزارش‌ها */}
              <Tab.Pane eventKey="flags">
                <h4>مدیریت گزارش‌ها</h4>
                <p>لیست گزارش‌های ارسال شده توسط کاربران:</p>
                <Table striped bordered hover>
                  <thead>
                    <tr>
                      <th>#</th>
                      <th>نوع گزارش</th>
                      <th>توضیحات</th>
                      <th>اقدام</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>1</td>
                      <td>کامنت</td>
                      <td>محتوای نامناسب</td>
                      <td>
                        <Button variant="danger" size="sm">حذف</Button>
                      </td>
                    </tr>
                    <tr>
                      <td>2</td>
                      <td>کاربر</td>
                      <td>حساب مشکوک</td>
                      <td>
                        <Button variant="warning" size="sm">بلاک</Button>
                      </td>
                    </tr>
                  </tbody>
                </Table>
              </Tab.Pane>
            </Tab.Content>
          </Tab.Container>
        </Col>
      </Row>
    </Container>
  );
};

export default SettingsPage;

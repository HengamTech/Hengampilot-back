import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

const ReviewForm = () => {
  const [formData, setFormData] = useState({
    category: '',
    review: '',
    rating: 0,
    companyName: '', // این فیلد را از ابتدا حذف می‌کنیم
  });
  const [errors, setErrors] = useState({});
  const [suggestedCompanies, setSuggestedCompanies] = useState([]); // شرکت‌های پیشنهادی
  const [newCompany, setNewCompany] = useState(''); // نام شرکت جدید

  const categories = [
    'خدمات مسافرتی',
    'خدمات منزل',
    'آموزش',
    'لوازم منزل',
    'ورزش',
    'غذا',
    'رستوران و کافه',
    'خدمات عمومی',
    'مالی',
    'رسانه و اخبار',
    'خدمات حقوقی',
  ];

  const companies = {
    'ورزش': ['سایت ورزش سه', 'پارس فوتبال', 'ورزش 11'],
    'رستوران و کافه': ['کافه گالری', 'رستوران شب‌های تهران'],
    'خدمات مسافرتی': ['آژانس مسافرتی ایرانگردی', 'آژانس قاصدک'],
    // این داده‌ها ممکن است از API گرفته شوند.
  };

  // به‌روزرسانی شرکت‌های پیشنهادی بر اساس انتخاب دسته‌بندی
  const handleCategoryChange = (e) => {
    const category = e.target.value;
    setFormData({ ...formData, category });
    setNewCompany(''); // پاک کردن نام شرکت جدید هنگام تغییر دسته‌بندی
    if (category && companies[category]) {
      setSuggestedCompanies(companies[category]);
    } else {
      setSuggestedCompanies([]); // اگر دسته‌بندی انتخاب نشده باشد، لیست پیشنهادات پاک شود
    }
    setErrors({ ...errors, category: '' }); // پاک کردن خطای دسته‌بندی
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
    setErrors({ ...errors, [name]: '' });
  };

  const handleStarClick = (rating) => {
    setFormData({ ...formData, rating });
    setErrors({ ...errors, rating: '' });
  };

  const validateForm = () => {
    const newErrors = {};
    if (!formData.category) newErrors.category = 'لطفاً دسته‌بندی را انتخاب کنید.';
    if (!formData.review.trim()) newErrors.review = 'لطفاً نظر خود را وارد کنید.';
    if (formData.rating === 0) newErrors.rating = 'لطفاً تعداد ستاره‌ها را انتخاب کنید.';
    return newErrors;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const formErrors = validateForm();
    if (Object.keys(formErrors).length > 0) {
      setErrors(formErrors);
    } else {
      console.log('Form submitted:', formData);
      alert('نظر شما با موفقیت ثبت شد!');
      setFormData({ category: '', review: '', rating: 0 });
      setSuggestedCompanies([]); // پاک کردن پیشنهادات بعد از ارسال
    }
  };

  const handleAddNewCompany = () => {
    if (newCompany.trim()) {
      // ارسال نام شرکت جدید به پنل ادمین
      console.log('ارسال به پنل ادمین:', newCompany);
      alert(`شرکت "${newCompany}" به پنل ادمین ارسال شد.`);
      setSuggestedCompanies([...suggestedCompanies, newCompany]);
      setFormData({ ...formData, companyName: newCompany });
      setNewCompany(''); // پاک کردن فیلد شرکت جدید
    }
  };

  return (
    <div className="container mt-5">
      <div className="row align-items-center">
        <div className="col-md-5 d-flex align-items-center justify-content-center">
          <img
            src="https://img.freepik.com/free-photo/3d-rendering-pen-ai-generated_23-2150695409.jpg?t=st=1732267774~exp=1732271374~hmac=46fe48c446b61a4ed5d02ab32693475926fea40da232eb36e0f683fb4760df98&w=740"
            alt="Review Form"
            className="img-fluid rounded"
            style={{ width: '100%', height: 'auto', maxHeight: '500px', objectFit: 'cover' }}
          />
        </div>
        <div className="col-md-7">
          <form onSubmit={handleSubmit} className="p-3 border rounded" style={{ direction: 'rtl' }}>
            {/* دسته‌بندی */}
            <div className="mb-3">
              <label htmlFor="category" className="form-label">
                دسته‌بندی شرکت
              </label>
              <select
                className={`form-select ${errors.category ? 'is-invalid' : ''}`}
                id="category"
                name="category"
                value={formData.category}
                onChange={handleCategoryChange}
              >
                <option value="">انتخاب کنید</option>
                {categories.map((category, index) => (
                  <option key={index} value={category}>
                    {category}
                  </option>
                ))}
              </select>
              {errors.category && <div className="invalid-feedback">{errors.category}</div>}
            </div>

            {/* نظر */}
            <div className="mb-3">
              <label htmlFor="review" className="form-label">
                نظر پیشنهادی
              </label>
              <textarea
                className={`form-control ${errors.review ? 'is-invalid' : ''}`}
                id="review"
                name="review"
                rows="4"
                value={formData.review}
                onChange={handleChange}
              ></textarea>
              {errors.review && <div className="invalid-feedback">{errors.review}</div>}
            </div>

            {/* ستاره‌ها */}
            <div className="mb-3">
              <label className="form-label">تعداد ستاره پیشنهادی</label>
              <div>
                {[1, 2, 3, 4, 5].map((star) => (
                  <span
                    key={star}
                    onClick={() => handleStarClick(star)}
                    style={{
                      cursor: 'pointer',
                      fontSize: '1.5rem',
                      color: star <= formData.rating ? 'gold' : 'gray',
                    }}
                  >
                    ★
                  </span>
                ))}
              </div>
              {errors.rating && <div className="text-danger mt-2">{errors.rating}</div>}
            </div>

            {/* پیشنهادات شرکت‌ها */}
            {formData.category && suggestedCompanies.length > 0 && (
              <div className="mb-3">
                <label className="form-label">شرکت‌های پیشنهادی</label>
                <select
                  className="form-select"
                  name="companyName"
                  value={formData.companyName}
                  onChange={handleChange}
                >
                  <option value="">انتخاب کنید</option>
                  {suggestedCompanies.map((company, index) => (
                    <option key={index} value={company}>
                      {company}
                    </option>
                  ))}
                </select>
              </div>
            )}

            {/* افزودن شرکت جدید */}
            {formData.category && !suggestedCompanies.includes(formData.companyName) && (
              <div className="mb-3">
                <label htmlFor="newCompany" className="form-label">
                  شرکت پیشنهادی خود را وارد کنید
                </label>
                <input
                  type="text"
                  className="form-control"
                  id="newCompany"
                  value={newCompany}
                  onChange={(e) => setNewCompany(e.target.value)}
                />
                <button
                  type="button"
                  className="btn btn-secondary mt-2"
                  onClick={handleAddNewCompany}
                >
                  افزودن
                </button>
              </div>
            )}

            <button type="submit" className="btn btn-primary w-100">
              ثبت نظر
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default ReviewForm;

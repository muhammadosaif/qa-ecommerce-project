# 💼 qa-ecommerce-project

**End-to-end QA automation framework for an e-commerce application.**  
Built with **Selenium**, **Pytest**, **Postman**, and **GitHub Actions** for robust test automation, CI/CD integration, and API validation.

---

## 📁 Project Structure

```
qa-ecommerce-project/
├── automation/
│   ├── conftest.py                 # Pytest fixtures
│   ├── requirements.txt            # Python dependencies
│   └── tests/
│       ├── pages/                  # Page Object Models
│       │   ├── base_page.py
│       │   ├── checkout_page.py
│       │   └── login_page.py
│       ├── test_checkout.py        # Checkout test cases
│       └── test_login.py           # Login test cases
│
├── api-tests/
│   ├── Ecommerce.postman_collection.json
│   └── Ecommerce.postman_environment.json
│
├── test-cases/
│   ├── Login_Test_Cases.xlsx
│   ├── Checkout_Test_Cases.xlsx
│   └── Search_Test_Cases.xlsx
│
├── defects/
│   └── Bug_Report_Sample.xlsx      # Sample bug report format
│
├── reports/
│   └── sample_test_report.html     # Example test result output
│
├── .github/
│   └── workflows/
│       └── run-tests.yml           # GitHub Actions CI workflow
│
├── LICENSE
└── README.md
```

---

## 🧪 Technologies Used

- **Python 3.x**
- **Selenium**
- **Pytest**
- **Postman**
- **GitHub Actions**
- **HTML Reports (pytest-html)**

---

## 🚀 Getting Started

### 🛆 Setup Python Environment

1. Clone the repo:
   ```bash
   git clone https://github.com/muhammadosaif/qa-ecommerce-project.git
   cd qa-ecommerce-project/automation
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## ✅ Running Tests

### Run all tests:
```bash
pytest --html=../reports/report.html
```

### Run specific test file:
```bash
pytest tests/test_login.py --html=../reports/login_report.html
```

---

## 🔁 CI/CD with GitHub Actions

Test suite runs automatically on each push using the `.github/workflows/run-tests.yml` file.  
It uses `pytest` and uploads the test report as an artifact.

---

## 🌐 API Testing with Postman

- Open `api-tests/Ecommerce.postman_collection.json` in Postman.
- Use `Ecommerce.postman_environment.json` for environment variables.
- Supports automated testing via Postman’s **Collection Runner** or **Newman CLI**.

---

## 🐞 Bug Reporting

All bugs discovered during testing should be reported in the `defects/Bug_Report_Sample.xlsx` template.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 👨‍💻 Author

**Muhammad Osaif**  
[GitHub](https://github.com/muhammadosaif)  
muhammadosaif991@gmail.com

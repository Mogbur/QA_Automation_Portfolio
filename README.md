# 🧪 QA Automation Portfolio by Henri

Welcome to my personal QA Automation Portfolio! This repo is a demonstration of my ability to perform both **manual and automated testing** using tools like **Selenium, Pytest, Python, and Requests**.

I built this project from scratch while learning and implementing real-world test automation workflows. My goal: become a top-tier freelance QA Engineer with real results and reusable code.

---

## 🔥 Highlights

- ✅ Login test (valid & invalid credentials)
- ✅ Signup and account creation
- ✅ UI visibility checks
- ✅ Screenshot capture on test failure
- ✅ Custom overlay handling
- ✅ Parametrized testing
- ✅ API test with JSON validation
- ✅ Account deletion test
- ✅ Product search and navigation
- ✅ Google search test (just for fun!)

---

## 🧰 Tech Stack

- **Language:** Python 3.13
- **Frameworks:** Pytest, Selenium
- **Other Tools:** ChromeDriver, Requests, pytest-html
- **OS:** Windows 10 Pro
- **IDE:** VS Code

---

## 📁 Folder Structure

```
QA_Portfolio/
├── tests/                   # ✅ 13 test cases (UI, API, E2E)
│   ├── test_account_creation_fill_form.py
│   ├── test_api_jsonplaceholder.py
│   ├── test_google_search.py
│   ├── test_login_cases.py
│   ├── test_login_herokuapp.py
│   ├── test_login_param.py
│   ├── test_logout_and_delete_account.py
│   ├── test_negative_login_cases.py
│   ├── test_search.py
│   ├── test_search_intentional_fail.py
│   ├── test_signup_form_validation.py
│   ├── test_signup_success.py
│   └── test_ui_elements_after_signup.py
│
├── utils/                   # 🔧 Custom helper functions
│   ├── overlay_handler.py
│   └── screenshot.py
│
├── reports/                # 📝 HTML reports from test runs
│   └── test_report.html
│
└── screenshots/            # 📸 Screenshots from failed tests
    └── *.png
```

## 🧪 Demo

This test automates a full signup ➝ logout ➝ login ➝ account deletion flow using Python, Selenium, and Pytest.

![Logout & Delete Demo](QA_Portfolio/demo_logout_delete.gif)

---

## ✅ Highlights

- Full end-to-end signup → login → delete flow
- Dynamic element handling & popups
- Real API test (GET request validation)
- Negative and parameterized login test cases
- Built-in screenshot proofing for failed runs
- HTML test reports for client/team sharing

---

## 🧠 What I Learned

- Robust browser automation using Selenium
- Efficient bug isolation and failure tracing
- Real QA environment debugging and overlay handling
- Automating signup flows with dropdowns, form fields, waits
- Reusability via custom `utils/` scripts

---

## ⚡ Quick Start

Clone this repo, install the dependencies, and run all tests:

```bash
    git clone https://github.com/Mogbur/QA_Automation_Portfolio.git
    cd QA_Automation_Portfolio
    pip install -r requirements.txt
    pytest tests/ --html=reports/test_report.html
```

---

## 📦 Run Tests

1. **Install requirements**
   ```bash
   pip install -r requirements.txt

---
  
2. **Run all tests with HTML report**
    pytest tests/ --html=reports/test_report.html

    
3. **View screenshots**
- Any test that fails will create a screenshot in `screenshots/`.

🖼️ **Sample Test Report:**  
[View HTML Report](reports/test_report.html)  
📸 **Example Screenshot from a Failing Test:**  
![Sample Screenshot](screenshots/sample_fail.png)

---

## 📣 Let's Connect

I'm open to freelance work, part-time projects, or agency collaborations.  
This is just the beginning — I'm building toward a full QA automation agency.

Drop me a message and let's break some bugs together! 🐛🚫  
📬 Contact
Email: gamermogbur@gmail.com
Check out my other work at [github.com/Mogbur](https://github.com/Mogbur)

# Form Autofill Bot with Selenium

Automates filling out and submitting a practice form at
https://demoqa.com/automation-practice-form

## 🔧 Tools & Tech

- Python 3.x
- Selenium WebDriver
- ChromeDriverManager
- VS Code

## 👤 Personal Info Used

- **Name:** Aaron Jones
- **Email:** aaron.jones.dev@gmail.com
- **Phone:** 480-213-4567
- **Address:** 4321 Lambeezy Lane, Phoenix, AZ 85004

## 💻 What It Does

1. Opens Chrome and navigates to the DemoQA form
2. Fills in name, email, gender, phone, subject, hobbies, address
3. Selects state & city from dropdowns
4. Submits the form
5. Takes a screenshot of the confirmation modal 
![Form Submission Screenshot](`form_submission_result.png`)

## 🚀 How to Run

```bash
git clone https://github.com/billiondollarjones/form-autofill-selenium.git
cd form-autofill-selenium
pip install selenium webdriver-manager
python main.py

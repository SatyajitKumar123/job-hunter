# 🎯 JobHunter - Job Application Tracker

JobHunter is a CRUD (Create, Read, Update, Delete) web application built with **Django**. It helps users organize their job search by tracking companies, positions, and application statuses.

This project demonstrates core Django concepts including Authentication, User Ownership, and Database Relationships.

## 🚀 Features

* **User Authentication:** Secure Login and Logout system.
* **Data Privacy:** Users can only view, edit, and delete *their own* job applications.
* **CRUD Operations:** Full ability to Add, View, Edit, and Delete job entries.
* **Search Functionality:** Filter applications by Company Name or Job Title.
* **Status Tracking:** Visual status indicators (Applied, Interviewing, Offer, Rejected).
* **Responsive Design:** Clean HTML/CSS interface.

## 🛠️ Tech Stack

* **Backend:** Python, Django 5
* **Database:** SQLite (Default)
* **Frontend:** Django Templates, HTML5, CSS3

## 💻 Installation & Setup

Follow these steps to run the project locally on your machine.

**1. Clone the repository**
```bash
git clone [https://github.com/SatyajitKumar123/job-hunter.git](https://github.com/SatyajitKumar123/job-hunter.git)
cd job-hunter
````

**2. Create a Virtual Environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install Dependencies**

```bash
pip install django
# Or if you have a requirements file:
# pip install -r requirements.txt
```

**4. Apply Migrations**

```bash
python manage.py migrate
```

**5. Create a Superuser (Admin)**
You need an account to log in initially.

```bash
python manage.py createsuperuser
```

**6. Run the Server**

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

## 🧠 Key Concepts Learned

This project was built to practice:

  * **Function-Based Views (FBVs)** for explicit logic control.
  * **Django ORM** for database queries and filtering.
  * **Q Objects** for complex search queries (OR logic).
  * **Decorators** (`@login_required`) for route protection.
  * **ModelForms** for data validation and saving.

## 📄 License

This project is open source and available for educational purposes.

````

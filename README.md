
# Django Library Management System (LMS)

A simple web-based Library Management System built with Django. This app allows management of books, users (patrons), and borrow records.

## 📚 Features

- Add, view, edit, and delete:
  - Books
  - Patrons (Users)
  - Borrow Records
- Search books and borrow records by User ID or Book ID
- Auto-generated Membership ID for users
- Dashboard with summaries
- Basic styling with Flowbite CSS

## 🛠️ Technologies Used

- Python 3.x
- Django 4.x
- SQLite3
- HTML/CSS (Flowbite)
- Bootstrap (optional)

## 🚀 Getting Started

### Prerequisites

- Python installed
- `pip` installed

### Installation


# Clone the repository
```bash
git clone https://github.com/your-username/django-lms.git
cd django-lmsx
```
# Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
# Install dependencies
```bash
pip install -r requirements.txt
```

# Apply migrations
```bash
python manage.py migrate
```
# Run development server
```bash
python manage.py runserver
```
# Create Superuser
```bash
python manage.py createsuperuser
```

# 📂 Project Structure
  ```bash
  ├── library/
  │   ├── migrations/
  │   ├── templates/
  │   ├── static/
  │   ├── models.py
  │   ├── views.py
  │   └── urls.py
  ├── lms/ (main project folder)
  ├── db.sqlite3
  └── manage.py
  ```
# ✍️ Author
  Developed by Pranish Shrestha

# 📄 License
  This project is licensed under the MIT License.

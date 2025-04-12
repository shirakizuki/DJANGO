# donezo: Reimagine your productivity with Smart Tasks
**A Task Management App** built with Django

Donezo is a sleek and simple task management system that helps users organize their to-dos with an intuitive interface, user authentication, and a responsive dashboard.

---

## 🚀 Features

- ✅ User registration and login
- ✅ Personalized dashboard greeting users by name
- ✅ Sidebar navigation with active link highlighting
- ✅ Task list view and visual layout
- ✅ Clean design using vanilla CSS and Font Awesome icons

---


## 🛠️ Tech Stack

- Python 3.x  
- Django 4.x  
- SQLite (default database)  
- HTML5 & CSS3 (Vanilla CSS)  
- Font Awesome for icons  

---

## 📦 Setup Instructions

```bash

# Clone the repository
git clone https://github.com/MarcKyle/moni-project.git
cd myproject

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Start the development server
python manage.py runserver
```

## 🧪 Example User Flow

1. Users can access login through `/view` route.
2. For registration, users can sign up via a `/register/` route.
    User registration includes the following:
    * first and last name
    * username
    * email
    * password
    
    Once the user successfully registers, it will be redirected to the home route ``.
3. For login, user can login via a `/login/` route.
    User login includes the following:
    * username
    * password

    Once the user successfully registers, it will be redirected to the home route ``.

###  Session Handling
- Session cookies managed securely using Django's session middleware.
- CSRF protection enabled on all forms.
- User-specific data filtered using `request.user`.
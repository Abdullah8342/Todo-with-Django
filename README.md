# 📝 Django Todo List App

A fully functional **Django-based Todo List application** with user authentication and CRUD operations for managing personal tasks.

---

## 🚀 Features

- 🧑‍💼 **User Authentication**
  - Signup
  - Login
  - Logout

- ✅ **Task Management**
  - Add new tasks
  - Edit/update existing tasks
  - Delete tasks
  - Mark tasks as complete/incomplete
  - Tasks are private to each logged-in user

---

## 🧱 Data Model

### `Task` Model

| Field        | Type             | Description                               |
|--------------|------------------|-------------------------------------------|
| `title`      | `CharField`      | Short title of the task                   |
| `description`| `TextField`      | Detailed description of the task          |
| `created`    | `DateTimeField`  | Automatically generated creation date     |
| `is_complete`| `BooleanField`   | Tracks whether the task is completed      |
| `user`       | `ForeignKey`     | Links the task to the user who created it |

---

## 📁 Project Structure

```
todo_project/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── README.md
├── todo_project/              # Main Django project
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── base/                      # Core App
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── forms.py
    ├── urls.py
    ├── templates/
    │   ├── base.html
    │   ├── create_task.html
    │   ├── task_detail.html
    |   ├── taskview.html
    |   ├── task_delete.html
    |   ├── update_task.html
    └── migrations/
  accounts/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── forms.py
    ├── urls.py
    ├── templates/
    │   ├── base.html
    │   ├── signup.html
    └── migrations/
```

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/django-todo-app.git
cd django-todo-app
```

### 2. Create Virtual Environment & Activate It

```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

### 7. Open in Browser

```
http://127.0.0.1:8000/
```

---

## 🛠️ Built With

- Python 3.x
- Django 4.x
- SQLite (default Django database)
- HTML

---

## ✅ Future Enhancements

- Add task due dates and reminders
- Categorize tasks by priority
- Tagging support
- Dark mode UI
- REST API using Django REST Framework (DRF)
- Responsive frontend with Tailwind or Bootstrap

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Abdullah**  
GitHub: [@Abdullah8342](https://github.com/Abdullah8342)  
Email: abdullah.4110r.work@gmail.com

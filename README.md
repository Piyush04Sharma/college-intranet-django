# College Intranet (Django)

    python -m venv venv
    source venv/bin/activate        # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

Open http://127.0.0.1:8000/dashboard/ -> redirected to login.
Set First name / Last name for the user in /admin/ to see the full name.

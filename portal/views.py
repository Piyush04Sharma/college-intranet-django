from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Sample data: list of dictionaries (title, department, date)
NOTICES = [
    {"title": "Mid-Semester Examination Schedule", "department": "Examination Cell", "date": "2026-11-28"},
    {"title": "Staff Meeting - Academic Council", "department": "Administration", "date": "2026-11-30"},
    {"title": "Lab Equipment Audit", "department": "Physics", "date": "2026-12-02"},
    {"title": "Library Digital Resources Training", "department": "Library", "date": "2026-12-04"},
    {"title": "Annual Sports Day Planning", "department": "Physical Education", "date": "2026-12-08"},
]


@login_required  # anonymous users are redirected to settings.LOGIN_URL?next=/dashboard/
def dashboard(request):
    user = request.user
    context = {
        "full_name": user.get_full_name() or user.get_username(),
        "last_login": user.last_login,
        "notices": NOTICES,
    }
    return render(request, "portal/dashboard.html", context)

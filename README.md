[README.md](https://github.com/user-attachments/files/27760229/README.md)
# Modern Hospital Appointment System

A clean, responsive, and fully functional Hospital Appointment System built with **Django (Python)**, **HTML5**, **CSS3**, **JavaScript**, and **Bootstrap 5**. The system allows patients to view hospital services, explore doctors' profiles, and book medical appointments seamlessly.

## 🚀 Features

- **Responsive Design**: Adapts perfectly to desktops, tablets, and mobile devices.
- **Dynamic Doctor Profiles**: Detailed profiles with images, experience, qualifications, and consultation fees.
- **Service Listings**: Explore different hospital departments (Cardiology, Neurology, etc.).
- **Appointment Booking**: Secure and intuitive booking system with date restrictions (prevents past dates).
- **Appointment Receipt**: Generates a receipt containing the appointment ID and patient details after successful booking.
- **Admin Dashboard**: Built-in Django Admin to manage doctors, departments, and monitor patient appointments.
- **Contact Us**: Functional contact form for user queries.

## 💻 Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5.3
- **Backend**: Python, Django 4.x
- **Database**: SQLite3 (Default, easily swappable to MySQL/PostgreSQL)
- **Icons**: FontAwesome 6

## 📂 Project Structure

```
hospital/
│
├── hospital_system/          # Core Django project settings
│   ├── settings.py           # Database and App configurations
│   ├── urls.py               # Main URL routing
│   └── wsgi.py               # WSGI config for deployment
│
├── hospital/                 # Main App module
│   ├── models.py             # Database tables (Doctor, Appointment, etc.)
│   ├── views.py              # Application logic and rendering
│   ├── urls.py               # App-level routing
│   └── admin.py              # Admin panel configurations
│
├── templates/                # HTML templates (base.html, home.html, etc.)
├── static/                   # Static files (CSS, JS, Images)
├── media/                    # User-uploaded files (Doctor Images)
├── manage.py                 # Django management script
└── README.md                 # Project documentation
```

## 🛠️ Setup & Installation

Follow these steps to set up the project on your local machine.

### 1. Prerequisites
Ensure you have Python installed. You can check by running:
```bash
python --version
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On Mac/Linux
```

### 3. Install Dependencies
```bash
pip install django pillow
```
*(Note: `pillow` is required for handling image uploads)*

### 4. Apply Database Migrations
This will create the necessary tables in the SQLite database.
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Admin)
Create an admin account to access the dashboard:
```bash
python manage.py createsuperuser
```
Follow the prompts to set a username, email, and password.

### 6. Run the Development Server
```bash
python manage.py runserver
```

### 7. Access the Website
- **Public Website**: `http://127.0.0.1:8000/`
- **Admin Dashboard**: `http://127.0.0.1:8000/admin/`

## 👨‍⚕️ Adding Sample Data
To test the website properly, log in to the **Admin Dashboard** (`/admin/`) and add a few `Departments` and `Doctors`. Once added, they will automatically appear on the website and become available in the Appointment Booking dropdown menus.

## 📝 License
This project is open-source and free to use for educational and commercial purposes.

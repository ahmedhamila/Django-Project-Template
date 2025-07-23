# Django Project Template

A scalable, production-ready Django project starter with a clean structure, reusable app scaffolding, Docker support, and environment-based settings.
Use this template to skip repetitive setup and keep your projects consistent and maintainable from day one.

## ✨ Features

This Django starter template includes:

* ✅ **Built-in JWT Authentication** — endpoints for signup, email or phone login, and token refresh, ready out of the box.
* ✅ **Custom Role-Based Authorization** — flexible system to define roles and permissions, and assign them per user.
* ✅ **Automatic Dockerized Workflow** — fully configured `docker-compose` to spin up Postgres and Django, handle migrations, and create a superuser automatically if credentials are provided.
* ✅ **Integrated API Documentation** — automatic, interactive **Swagger UI** to test your endpoints easily.
* ✅ **CamelCase API support** — automatic camelCase rendering and parsing for requests and responses using `djangorestframework-camel-case`.
* ✅ **API Pagination Ready** — sensible pagination defaults for any list endpoints.
* ✅ **Production-Ready Environment Separation** — organized `settings` for base, development, and production.
* ✅ **Custom App Generator** — quickly scaffold new Django apps with a clean, consistent structure.
* ✅ **Example Azure Web App Service Workflow** — shows how to deploy this project seamlessly on Azure.

Use this as a solid base for production-ready Django projects — so you can spend less time setting up, and more time building.


## 📦 Project Structure

```
.
├── .github/                      # GitHub workflows
├── app_template/                 # Template for generating new apps with consistent structure.
│   └── ...                       # See 'Django App Structure' below.
│
├── core/                         # Main Django project configuration.
│   ├── config/                   # Project configuration files.
│   │   ├── __init__.py
│   │   ├── cors.py               # CORS settings.
│   │   └── jwt.py                # JWT settings.
│   ├── management/
│   │   └── commands/
│   │       └── startcustomapp.py # Custom command to scaffold new apps from `app_template`.
│   ├── settings/                 # Environment-specific settings.
│   │   ├── __init__.py
│   │   ├── base.py               # Base settings shared across environments.
│   │   ├── development.py        # Development settings.
│   │   └── production.py         # Production settings.
│   ├── __init__.py
│   ├── asgi.py                   # ASGI entry point.
│   ├── env.py                    # Helpers for environment variables.
│   ├── urls.py                   # Project-level URL configs.
│   └── wsgi.py                   # WSGI entry point.
│
├── src/                          # All Django apps live here.
│   ├── example_app/              # Example app.
│   │   └── ...                   # See 'Django App Structure' below.
│   ├── users/                    # Users app.
│   │   └── ...                   # See 'Django App Structure' below.
│   └── utils/                    # Utilities app.
│       └── ...                   # See 'Django App Structure' below.
│
├── .env                          # Local environment variables.
├── .env.example                  # Example env file for reference.
├── .flake8                       # Flake8 linting configuration.
├── .gitignore                    # Files/folders to ignore in Git.
├── .isort.cfg                    # Isort configuration.
├── .pre-commit-config.yaml       # Pre-commit hooks.
├── docker-compose.yml            # Docker Compose configuration.
├── Dockerfile                    # Build your app image.
├── manage.py                     # Django’s CLI utility.
├── Pipfile                       # Pipenv dependency manager.
├── Pipfile.lock                  # Pipenv lock file.
├── pyproject.toml                # Optional: for Poetry/other build tools.
├── README.md                     # This README.
└── requirements.txt              # Requirements file (if not using Pipenv).
```


## 🗂️ Django App Structure

Each app follows this clean hierarchy by default:

```
<app_name>/
├── admin/           # Admin interface configurations.
├── controllers/     # View logic.
├── fixtures/        # Data fixtures for seeding/testing.
├── migrations/      # Database migrations.
├── models/          # App-specific models.
├── serializers/     # Data serialization.
├── services/        # Business logic layer.
├── tests/           # Unit & integration tests.
├── __init__.py      # App module init.
├── apps.py          # App config.
└── urls.py          # App-specific URLs.
```


## ⚙️ Installation & Usage

### ✅ Prerequisites

* Python **3.10**
* `pip`
* Recommended: [Pipenv](https://pipenv.pypa.io/)

---

### 1️⃣ Install Pipenv

```bash
pip install pipenv
```

---

### 2️⃣ Install Dependencies

```bash
pipenv install
```

---

### 3️⃣ Activate Virtual Environment

```bash
pipenv shell
```

---

### 4️⃣ Create & Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

---

### 6️⃣ Set Up Environment Variables

Create a `.env` file:

```env
# Secret key
SECRET_KEY=*********************

# Debug mode
DEBUG=True

# Database config
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_password
DB_HOST=localhost  # or 'db' if using Docker
DB_PORT=5432

# Superuser config
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=adminpassword
```

---

### 7️⃣ Run Development Server

```bash
python manage.py runserver
```


## ✨ Start a New App (with Template)

Create a new app with the predefined structure:

```bash
python manage.py startcustomapp my_new_app --src
```

---

## 🐳 Using Docker

### Prerequisites

* Docker
* Docker Compose

---

### 1️⃣ Build & Start Containers

```bash
docker-compose build
docker-compose up
```

---

### 2️⃣ Run Migrations (Inside Container)

```bash
docker-compose run web pipenv run python manage.py makemigrations
docker-compose run web pipenv run python manage.py migrate
```

---

### 3️⃣ Create Superuser (Inside Container)

```bash
docker-compose run web pipenv run python manage.py createsuperuser
```

---

### 4️⃣ Stop Containers

```bash
docker-compose down
```

---

## ✅ Environment Variables (Docker)

Make sure `.env` is present at the project root — Docker Compose uses it automatically.

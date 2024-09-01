---

# Django Project Template

## Installation Guide

### Prerequisites

Ensure you have Python==3.10 and pip installed on your system.

### Install `pipenv`

If you don't have `pipenv` installed, you can install it using pip:

```sh
pip install pipenv
```

### Create a Virtual Environment and Install Dependencies

Inside your project directory, use `pipenv` to create a virtual environment and install project dependencies:

```sh
pipenv install
```

### Activate the Virtual Environment

Activate the virtual environment:

```sh
pipenv shell
```

### Create Migrations

Create the initial database migrations:

```sh
python manage.py makemigrations
```

### Apply Migrations

Apply the initial database migrations:

```sh
python manage.py migrate
```

### Create Superuser (Optional)

If your project uses Django's admin interface, you can create a superuser account to access the admin panel:

```sh
python manage.py createsuperuser
```

### Environment Variables

Create a `.env` file in the project root directory and add the following content:

```env
# Secret configuration
SECRET_KEY=*********************
DEBUG=True
# Data Base configuration
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_password
DB_HOST=localhost || db(for docker)
DB_PORT=5432
# SuperUser configuration (username field = email)
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=adminpassword
```

### Run the Development Server

Start the Django development server with the specified settings:

```sh
python manage.py runserver
```

### Start New App from Template

```sh
python manage.py startcustomapp zakchi --src
```

## Docker Guide

To run the Django project using Docker, follow these steps:

### Prerequisites

Ensure you have Docker and Docker Compose installed on your system.

### Build and Run Docker Containers

1. **Build Docker Images**: In the root of your project directory, run the following command to build the Docker images:

    ```sh
    docker-compose build
    ```

2. **Start Containers**: Once the images are built, start the Docker containers:

    ```sh
    docker-compose up
    ```

    This command will start both the Django application and the PostgreSQL database in separate containers.

### Create Migrations

To create initial database migrations, you need to run the command inside the `web` container:

```sh
docker-compose run web pipenv run python manage.py makemigrations
```

### Apply Migrations

Apply the initial database migrations with:

```sh
docker-compose run web pipenv run python manage.py migrate
```

### Create Superuser (Optional)

If you want to create a superuser account, run:

```sh
docker-compose run web pipenv run python manage.py createsuperuser
```

### Stop Docker Containers

To stop the running containers, use:

```sh
docker-compose down
```

### Environment Variables

Ensure you have a `.env` file in the project root directory with the necessary environment variables. Docker Compose will use this file to set up the environment for the containers.

---

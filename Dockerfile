# Pull the official base image
FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev gcc

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /code

# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install

# Copy the project files to the container
COPY . /code/

# Expose port 8000 to the outside world
EXPOSE 8000

# Run the Django server
CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]

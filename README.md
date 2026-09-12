# Django Chat App

A simple Django chat application with a REST API.

## Features

- Real-time chat room structure
- Django views and templates
- DRF API endpoints
- Filter support with django-filter

## Setup

1. Create and activate a virtual environment:

   python -m venv .venv
   .venv\Scripts\activate

2. Install dependencies:

   pip install -r requirements.txt

3. Copy environment variables:

   copy .env.example .env

4. Update the values in `.env` if needed.

5. Install the environment loader if it is not already installed:

   pip install python-dotenv

6. Run migrations:

   python manage.py migrate

6. Start the development server:

   python manage.py runserver

## Environment variables

Create a `.env` file with values like:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,[::1]
```

## GitHub upload notes

- Do not commit your `.env` file.
- Do not commit the SQLite database file.
- Keep `.gitignore` updated before pushing.

## Useful commands

```bash
python manage.py check
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

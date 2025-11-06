from core.env import config


CORS_ALLOWED_ORIGINS = [
    config("FRONTEND_URL"),
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
ALLOWED_HOSTS = [
    config("BACKEND_HOST"),
    "127.0.0.1",
]
CSRF_TRUSTED_ORIGINS = [
    f"https://{config('BACKEND_HOST')}",
    "http://127.0.0.1",
]

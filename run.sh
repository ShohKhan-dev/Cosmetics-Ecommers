cd /web/backend-oncosmetic &&
source .venv/bin/activate &&
source conf &&
gunicorn -b 0.0.0.0:8001 config.wsgi:application --workers 4
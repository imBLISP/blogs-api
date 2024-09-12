#!/bin/bash
python /populate-elasticsearch.py
fastapi dev --host 0.0.0.0 /app/main.py &
celery -A app.worker worker --loglevel=info
# syntax=docker/dockerfile:1
FROM python:3.8-alpine
COPY . /
WORKDIR /
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install -r requirements.txt
EXPOSE 8000
RUN chmod +x /start.sh
CMD ["sh", "/start.sh"]
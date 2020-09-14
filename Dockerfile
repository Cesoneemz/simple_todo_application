FROM node:14.9.0-alpine as frontend
WORKDIR /app
COPY frontend .
RUN npm install
RUN npm run build

FROM python:3.8.5-alpine

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir -p /usr/src/app/

WORKDIR /usr/src/app/

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY project .
COPY --from=frontend /app/dist /vue
RUN pip install --no-cache-dir -r req.txt

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]


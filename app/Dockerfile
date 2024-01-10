FROM python:3.12 AS base

ENV PATH /opt/venv/bin:$PATH
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH=/

FROM base AS builder
RUN python -m venv /opt/venv
COPY *.txt .
RUN pip install --requirement requirements.txt

FROM base
WORKDIR /app
COPY --from=builder /opt/venv /opt/venv
COPY . .

ARG options
ENV OPTIONS $options

ARG PORT=8000
ENV PORT $PORT
EXPOSE $PORT

CMD exec gunicorn $OPTIONS --bind :$PORT --workers 1 --threads 8 --timeout 60 main:app

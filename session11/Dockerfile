FROM python:3.14-slim

RUN pip install uv

WORKDIR /app

COPY . .

RUN uv sync

EXPOSE 8000

ENV PYTHONPATH=/app/src

CMD ["uv", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
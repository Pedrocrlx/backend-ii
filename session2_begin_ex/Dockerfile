FROM python:3.14

RUN pip install uv

WORKDIR /app

COPY . .

RUN uv sync

EXPOSE 8000

CMD ["uv", "run", "fastapi", "dev", "src/api/main.py"]


FROM python:3.10-slim


WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --extra-index-url https://download.pytorch.org/whl/cpu -r requirements.txt


COPY . .

CMD ["python", "main.py"]

FROM python:3.11-slim

WORKDIR /app

# system dependencies (safe ML stack baseline)
RUN apt-get update && apt-get install -y gcc

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy application
COPY . .

EXPOSE 8000

# production server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# 1. Base light image
FROM python:3.11-slim

# 2. Not create pyc, log to stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Folder working into container
WORKDIR /app

# 4. Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy source code
COPY . .

# 6. Create folder data (mount volume later)
RUN mkdir -p data/checkpoint data/output

# 7. Run app
CMD ["python", "main.py"]

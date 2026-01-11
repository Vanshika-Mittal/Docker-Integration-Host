# Use official Python image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install daphne

# Copy project files
COPY . /app/

# Expose port (default Django port)
EXPOSE 8000

# Collect static files (optional, if you use static files)
# RUN python manage.py collectstatic --noinput

# Run Daphne ASGI server
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "home.asgi:application"]
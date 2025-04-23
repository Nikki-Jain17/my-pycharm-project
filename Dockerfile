# Use official Python base image
FROM python:3.13-slim

# Set working directory inside container
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    meson \
    ninja-build \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Install necessary Python packages, including allure-pytest and boto3
RUN pip install --no-cache-dir allure-pytest boto3

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project contents including tests, run_tests.py, and notification script
COPY . .

# Copy the notification script into the container
COPY send_notification.py /app/send_notification.py

# Set default command (can be overridden in Kubernetes YAML using args)
# The command will run tests, generate the Allure report, and send an SNS notification
CMD ["bash", "-c", "pytest --alluredir=/allure-results tests/test_sql_to_azure.py && python /app/send_notification.py"]

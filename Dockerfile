# Use the official Python base image
FROM python:3.13.0
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . .

# Install dependencies the normal way
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# using poetry
RUN pip install poetry
RUN poetry install

# Expose the port the app will run on
EXPOSE 8000
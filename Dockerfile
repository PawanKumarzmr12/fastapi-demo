# Base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy poetry files first
COPY pyproject.toml poetry.lock* /app/

# Install poetry
RUN pip install poetry

# Install dependencies
RUN poetry config virtualenvs.create false \
 && poetry install --no-dev

# Copy project files
COPY . /app

# Expose port
EXPOSE 8000

# Run app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

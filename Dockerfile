# agentML Docker Image

FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements files
COPY requirements-opencode.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements-opencode.txt

# Copy application code
COPY . .

# Create workspace directory
RUN mkdir -p /workspace /app/agent_workspace

# Set environment variables for the application
ENV WORKSPACE=/workspace
ENV PYTHONPATH=/app:$PYTHONPATH

# Expose port for potential API service
EXPOSE 8000

# Default command
CMD ["python", "-c", "print('agentML ready. Run tests with: pytest')"]

# Use official Python runtime as base image
FROM python:3.10-slim

# Set container working directory
WORKDIR /app

# Install system dependencies for building packages
RUN apt-get update && apt-get install -y \
       build-essential \
       python3-dev \
       libyaml-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container
COPY . .

# Upgrade pip and install Python dependencies
RUN python3 -m pip install --upgrade pip
    # \ && python3 -m pip install Cython

# Install additional dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Streamlit default port
EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
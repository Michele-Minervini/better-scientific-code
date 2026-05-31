# 1. Base Image: Start with a lightweight version of Ubuntu with Python 3.11 pre-installed
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /research

# 3. Install any heavy OS-level dependencies (e.g., C++ compilers, Git, or MPI)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy your requirements file first (this speeds up future builds via caching)
COPY requirements.txt .

# 5. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the rest of your research code into the container
COPY . .

# 7. Default command: What should the container do when someone turns it on?
CMD ["python", "main_simulation.py"]
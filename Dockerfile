# Python ka official lightweight image use kar rahe hain
FROM python:3.12

# System packages install kar rahe hain jo Pygame aur virtual screen (xvfb) ke liye zaroori hain
RUN apt-get update && apt-get install -y \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libfreetype6-dev \
    libportmidi-dev \
    libgl1 \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# App folder ko container ke andar working directory banate hain
WORKDIR /app

# Dependencies install karna
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Baaki saara code container me copy karna
COPY . .

# Virtual screen ke sath game run karne ki command
CMD ["xvfb-run", "-a", "python", "src/main.py"]
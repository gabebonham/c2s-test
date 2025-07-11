# Initializing Environment

## LINUX/MACOS

### python3 -m venv venv

### source venv/bin/activate

### pip install -r requirements.txt

### docker compose up -d

## WINDOWS

### python -m venv venv

### venv\Scripts\activate

### pip install -r requirements.txt

### docker-compose up -d

# Initialize Project

### python -m main

## Don't fortget to take docker down with

### LINUX/MACOS: docker compose down -v

### WINDOWS: docker-compose down -v

# In case you quit the program without killing the api process that runs in the backgroud

### ps aux | grep uvicorn

## Copy the PID ID and kill it

## ! Don't kill this process: 320208 0.0 0.0 4092 2048 pts/5 S+ 19:17 0:00 grep --color=auto uvicorn

### kill {PID}

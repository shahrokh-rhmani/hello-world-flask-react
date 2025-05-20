# Hello World App Deployment Guide

# 1. Server Connection & System Update

```
ssh root@your-server-ip
apt update && apt upgrade -y
```

# 2. Install Prerequisites

```
# Python and pip
apt install python3 python3-pip python3-venv -y

# Node.js 
curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
apt install -y nodejs 

# Nginx and tools
apt install nginx git build-essential -y
```

# 3. Clone Project

```
git clone https://github.com/your-username/hello-world-app.git
cd hello-world-app
```

# 4. Backend Setup (Flask)

```
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
```

Create systemd service file:

```
sudo nano /etc/systemd/system/flaskapp.service
```

Paste this configuration:

```
[Unit]
Description=Gunicorn Flask App
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/root/hello-world-app/backend
Environment="PATH=/root/hello-world-app/backend/venv/bin"
ExecStart=/root/hello-world-app/backend/venv/bin/gunicorn \
          --workers 3 \
          --bind unix:flaskapp.sock \
          --timeout 120 \
          app:app

[Install]
WantedBy=multi-user.target
```

Start and enable service:

```
sudo systemctl start flaskapp
sudo systemctl enable flaskapp
sudo systemctl status flaskapp
```

# 5. Frontend Setup (React)

```
cd ../frontend
npm install
npm run build

sudo mkdir -p /var/www/hello-world-app
sudo cp -r build/* /var/www/hello-world-app/
```

# 6. Nginx Configuration

```
sudo nano /etc/nginx/sites-available/hello-world-app
```

Paste this configuration:

```
server {
    listen 80;
    server_name your-ip-or-domain;

    root /var/www/hello-world-app;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location /api {
        include proxy_params;
        proxy_pass http://unix:/root/hello-world-app/backend/flaskapp.sock;
    }
}
```

Enable configuration:

```
sudo ln -s /etc/nginx/sites-available/hello-world-app /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

# 7. Permissions Setup

```
sudo chown -R www-data:www-data /root/hello-world-app/backend
sudo chmod 660 /root/hello-world-app/backend/flaskapp.sock
sudo chmod 755 /root /root/hello-world-app /root/hello-world-app/backend
```

# 8. Verification Steps

Check Gunicorn installation:

```
source /root/hello-world-app/backend/venv/bin/activate
pip list | grep gunicorn
```

Test Unix socket:

```
curl --unix-socket /root/hello-world-app/backend/flaskapp.sock http://localhost/api/hello
```

Expected output: 

```
{"message":"Hello from Flask!"}
```

Create requirements.txt (if needed):

```
echo "flask==2.3.3
werkzeug==2.3.7
flask-cors==4.0.0
gunicorn==23.0.0" > /root/hello-world-app/backend/requirements.txt
```
















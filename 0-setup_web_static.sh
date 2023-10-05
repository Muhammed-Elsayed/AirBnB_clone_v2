#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static

# install nginx if it is not already installed
sudo apt update
sudo apt install nginx -y

mkdir -p /data/web_static/releases/test/index.html
mkdir -p /data/web_static/shared/

echo "Hello, World!" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

sudo tee /etc/nginx/sites-available/default > /dev/null <<EOF
server {
	listen 80;
	listen [::]:80 default_server;
	add_header X-Served-By $HOSTNAME;
	root /var/www/html;
	index index.html index.htm;

	location /hbnb_static {
		alias /data/web_static/current/;
	}

	location /redirect_me {
        	return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
	}

	error_page 404 /404.html;
	location = /404.html {
		root /var/www/html;
		internal;
	}
}
EOF
sudo service nginx restart

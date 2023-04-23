#!/usr/bin/env bash
# set up web servers for deployment of web_static
apt update
apt -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "<html>
        <head>
        </head>
        <body>
            Holberton School
        </body>
     </html>" > /data/web_static/releases/test/index.html
ln -s /data/web_static/releases/tests/ /data/web_static/current
chown -R ubuntu:ubuntu /data
#file="/etc/nginx/sites-available/default"
#sed -i '/server_name _;/a \\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' "$file"
sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
service nginx restart

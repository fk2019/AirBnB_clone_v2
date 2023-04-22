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
location="\\\tlocation /hbnb_static {\\n\t\talias /data/web_static/current/;\n\t}\n"
file="/etc/nginx/sites-available/default"
sed -i "/server_name _;/a $location" "$file"
service nginx restart

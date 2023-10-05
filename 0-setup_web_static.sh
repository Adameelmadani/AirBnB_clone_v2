#!/usr/bin/env bash
#Install nginx if it's not installed
sudo apt-get update
sudo apt-get install -y nginx
mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
echo "<!DOCTYPE html>
<html>
	<head>
	<title>Test page</title>
	</head>
	<body>
	<h1>A test page</h1>
	</body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

old="server_name _;"
new="server_name _;\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}"
sudo sed -i "s|$old|$new|" /etc/nginx/sites-enabled/default
sudo service nginx restart

#!/usr/bin/env bash
# This script sets up web servers for deployment of web_static

# Install Nginx if not already installed
if ! command -v nginx &>/dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/{releases/test,shared}

# Create fake HTML file for testing
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create symbolic link, delete and recreate if it already exists
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership of /data/ to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_path="/etc/nginx/sites-available/default"
sudo sed -i '/^\s*server_name _;/a\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' "$config_path"

# Restart Nginx
sudo service nginx restart

exit 0


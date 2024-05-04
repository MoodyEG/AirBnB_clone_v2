# Puppet for setup
exec { 'install':
  provider => shell,
  command  => 'sudo apt-get update -y ; sudo apt-get install nginx -y ; sudo service nginx start ; \
  sudo mkdir -p /data/web_static/releases/test/ ;\sudo mkdir -p /data/web_static/shared/ ; \
  echo "simple content" | sudo tee /data/web_static/releases/test/index.html ; \
  sudo ln -sf /data/web_static/releases/test/ /data/web_static/current ; sudo chown -R ubuntu:ubuntu /data/ ; \
  sudo sed -i "45i \\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t}\n" /etc/nginx/sites-available/default ; \
  sudo service nginx restart ; exit 0',
}

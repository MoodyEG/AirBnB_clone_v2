# Puppet for setup
user { 'ubuntu':
  ensure     => 'present',
  managehome => true,
}
group { 'ubuntu':
  ensure => 'present',
}
exec { 'install':
  provider => shell,
  command  => 'sudo apt-get update -y ; sudo apt-get install nginx -y ; sudo service nginx start ; \
  sudo mkdir -p /data/web_static/releases/test/ ; sudo mkdir -p /data/web_static/shared/ ; \
  echo "simple content" | sudo tee /data/web_static/releases/test/index.html ; \
  sudo ln -sf /data/web_static/releases/test/ /data/web_static/current ; sudo chown -R ubuntu:ubuntu /data/ ; \
  echo "server {\n\tlisten 80 default_server;\n\tlisten [::]:80 default_server;\
  \n\troot /var/www/html;\n\tindex home.html index.html index.htm index.nginx-debian.html;\
  \n\tserver_name _;\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n\tlocation \
  /redirect_me {\n\t\treturn 301 https://image.pngaaa.com/935/3311935-middle.png;\n\t}\n\tlocation \
  / {\n\t\ttry_files \$uri \$uri/ =404;\n\t}
  }" | sudo tee /etc/nginx/sites-available/default ; \
  sudo service nginx restart ; exit 0',
}

# monitoring

Installation

git clone https://github.com/lvthillo/docker-elk.git
cd docker-elk/
docker-compose up -d
docker run -d -p 8080:80 --log-driver gelf --log-opt gelf-address=udp://localhost:12201 nginx:latest
sudo pip install Flask
sudo mkdir -p /tmp/var/log/

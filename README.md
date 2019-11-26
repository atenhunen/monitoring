# monitoring

Installation

git clone https://github.com/lvthillo/docker-elk.git
cd docker-elk/
docker-compose up -d
docker run -d -p 8080:80 --log-driver gelf --log-opt gelf-address=udp://localhost:12201 nginx:latest
sudo pip install Flask
sudo mkdir -p /tmp/var/log/
brew install filebeat

Running

# Terminal 1
cd monitoring
flask run

# Terminal 2
python monitoring/simulator.py 2 2
First parameter is number of requests per user, second is number of users.
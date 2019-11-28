# monitoring
This is a small demo of API logging. Server.py emulates and API and logs requests. Simulator.py simulates users calling the API.

# Installation

brew install python
brew install filebeat
sudo pip3 install requirements.txt
git clone https://github.com/lvthillo/docker-elk.git
cd docker-elk/
docker-compose up -d
docker run -d -p 8080:80 --log-driver gelf --log-opt gelf-address=udp://localhost:12201 nginx:latest
sudo mkdir -p /tmp/var/log/
filebeat -e

# Running

Terminal 1
cd monitoring
gunicorn --bind 0.0.0.0:5000 wsgi:app -w 8

Terminal 2
python monitoring/simulator.py < request-count > < user-count >
First parameter is number of requests per user, second is number of users.
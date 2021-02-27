#!/bin/bash
# curl https://get.docker.com | sudo bash
# sudo apt install -y curl jq
# version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
# sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo usermod -aG docker $(whoami)
sudo usermod -aG docker jenkins
sudo chmod 666 /var/run/docker.sock

docker-compose down --rmi all
docker-compose build
sudo docker login -u ${USERNAME} -p ${PASSWORD} https://registry.hub.docker.com
sudo docker-compose push


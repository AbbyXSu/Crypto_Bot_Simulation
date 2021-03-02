sudo chmod +x /usr/local/bin/docker-compose
sudo usermod -aG docker $(whoami)
sudo usermod -aG docker jenkins
sudo chmod 666 /var/run/docker.sock
docker-compose down --rmi all
docker-compose build
sudo docker login
sudo docker push ${AUTHOR}/revenue_service:v2
sudo docker push ${AUTHOR}/db
sudo docker push ${AUTHOR}/expenditure_service:v2
sudo docker push ${AUTHOR}/report_aggregate_service:v2
sudo docker push ${AUTHOR}/report_engine:v2
sudo docker push ${AUTHOR}/report_ui:v2


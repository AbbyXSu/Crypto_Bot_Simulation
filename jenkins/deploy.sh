scp -i ~/.ssh/id_rsa docker-compose.yml jenkins@swarm-manager:/home/jenkins/docker-compose.yml
ssh -i ~/.ssh/id_rsa jenkins@swarm-manager << EOF
    export DATABASE_URI=${DATABASE_URI}
    export AUTHOR=${AUTHOR}
    export DB_PASSWORD=${DB_PASSWORD}
    docker stack deploy --compose-file /home/jenkins/docker-compose.yml application
EOF
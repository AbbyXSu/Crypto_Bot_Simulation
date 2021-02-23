scp -i ~/.ssh/id_rsa docker-compose.yaml jenkins@swarm-manager:/home/jenkins/docker-compose.yaml
ssh -i ~/.ssh/id_rsa jenkins@swarm-manager << EOF
    export DATABASE_URI=${DATABASE_URI}
    export AUTHOR=${AUTHOR}
    export DB_PASSWORD=${DB_PASSWORD}
    docker stack deploy --compose-file /home/jenkins/docker-compose.yaml financial-report-generator-stack
EOF
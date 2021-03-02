# Financial Report Generator - A SOA Application

Resource: 

Link to Github project board: https://github.com/AbbyXSu/Financial_report_generator/projects/1

Successful Jenkins Build documentation of the 1st version of the application:https://github.com/AbbyXSu/Financial_report_generator/issues/16#issuecomment-788729676

Successful Jenkins Build documentation of the 2nd version of the application : https://github.com/AbbyXSu/Financial_report_generator/issues/16#issuecomment-788729759


## Requirement and Specification
It is required that an application should be developed using an service-orientated architecture (SOA) design and using following feature technologies: 

- Development and deployment using an orchestration tool Docker Swarm, and containerisation via docker compose and dockerfile 
- Version Control Systerm using Git and Feature_Branch model
- Webhooks is used to trigger Jenkins to recreate and redeploy the changed application
- CI/CD pipeline via Jenkins
- Ansible as an  provisioning, configuration management, and application-deployment tool enabling infrastructure as code, Anisble playbook and inventory is created for setting up and configurating the deployment environment
- NGINX is used as a reverse proxy and load balance for the application

Technologies used to achieve the requirements:

- Kanban Board: Github Project Board
- Version Control: Git
- CI/CD Server: Jenkins
- Configuration Management: Ansible
- Cloud server: GCP virtual machines
- Containerisation: Docker and Docker Compose
- Orchestration Tool: Docker Swarm
- Reverse Proxy: NGINX
- Python programming and Bash scripting 

## My Approach 

There are two versions of the application, the initial application contain simpler business logic and tha later one contain more vivid graph to demonstarte the trend of financial performance over time.

### Design and Structure of the application
![ERD](https://user-images.githubusercontent.com/77119427/109541044-387b2680-7abb-11eb-8ad8-690410ea1c55.PNG)

The application has five services in total ,with the first 4 services fulfilling the requiremnts of having a minimum of 4 services in the application, and a extra service for an User Interface Front end service:

- **Service 1** : Report Engine, this is an backend processer to process request from frontends and communicate with the backend services and database. It directly persists data and interact with MYSQL database 
- **Service 2** :renevue service simulating and generating revenue data 
- **Service 3** :expenditure service simulating and generating expense data 
- **Service 4**:act as an data aggregate service processer and generate a set of financail performance measurement/reports
- **Frontend User Interface service**: this directly receive requests from the client and interact with NGINX to achieve load balancing.

The requirement suggests that service 1 is the frontend UI and also DAL data access layer to presist data to the database, which indicate an persistance layer coupled with UI structure.

However, it is assessed that the seperation between frontend and backend is an better pratice than the suggested requirement and bring many benefits for the future Continuous delivery and development of the application, the frontend/backend seperation approach is taken following the below evaluation:

![UI and backend](https://user-images.githubusercontent.com/77119427/109568202-7d648480-7ade-11eb-8b63-b759aad0af92.PNG)

### Database Structure 

![database structure](https://user-images.githubusercontent.com/77119427/109569062-bc470a00-7adf-11eb-806f-379bbaec9ad4.PNG)
MYSQL database is used in this application, database is created, containerised and deployed through Docker containerisation along with all other services via docker compose. The database is prepopulated to ensure the table is established and connected to the API. MYSQL workbench is used during development stage to ensure the smooth procedures of data presistence and database management. 

### Project Tracking
Github Project board was the chosen method when planning the project and tracking the progress of tasks set out. This was done to ensure a steady workflow and create an agile methodology where changes could be made through the production of the web app. This was necessary to allow for an agile workflow ensuring smaller tasks were being completed and this allowed for a structured approach when tackling the project. Below is the project board used for this project:
![project board](https://user-images.githubusercontent.com/77119427/109570077-6a06e880-7ae1-11eb-8542-d51ecd631807.PNG)

### Second Interpretations of the Application

![Version 2 rolling update](https://user-images.githubusercontent.com/77119427/109542405-eb984f80-7abc-11eb-9f59-7ea47b82ab37.PNG)

Second versions of the application is created in order to demonstarte an rolling update using docker swarm and achieving A/B deployment with zero downtime.

## Feature Technologies and CI/CD Pipeline
![pipline](https://user-images.githubusercontent.com/77119427/109572022-6fb1fd80-7ae4-11eb-95d2-cc7322196c10.PNG)

### Webhook trigger Jenkins builds
![webhooks gitpush on jenkins](https://user-images.githubusercontent.com/77119427/109613390-fab4e700-7b28-11eb-83bc-b413ede3600e.PNG)

![webhook github](https://user-images.githubusercontent.com/77119427/109613362-f092e880-7b28-11eb-91f5-47fd3743ad27.PNG)

A webhook is a mechanism to automatically trigger the build of a Jenkins project upon a commit pushed in a Git repository.
In order for builds to be triggered automatically by push and pull request events, a Jenkins Web Hook needs to be added to the GitHub repository. 
An webhook triggered build event will be recorded on build status at the start of the build and Github will also recored the delivery status of the push triggered delivery event on their webhook records(As demonstrate above).

### CI/CD pipeline 
![version 2 jenkins](https://user-images.githubusercontent.com/77119427/109614441-8e3ae780-7b2a-11eb-9844-fb220ffc2b5a.PNG)

The above records shows the status of the Jenkins CI/CD-pipiline builds. The build status indicate if the build is successful or failed with tracking logs detaillig the issues and actions during the build.

Environment Variables were set for the project and therefore stores as credentials on jenkins. Credentials such as Docker Hub login, Database URI, Database password and author is maneged under Jenkins's Credentials/Secret management. There are many benefits in setting up Environment Variables,The major benefits of using environment variables are:Environment Variables can provide better security without leaving foorprint of your credentials on the source code, it also provide easy configuration for development where configuration and tools used could be everchanging.

**First stage -Testing:** Pytest and mock testing is used to perform unittesting, all tests has passed and reached above 90% coverage.   

**Second stage - Build and Push Docker images:** After successful testing of the codes, Jenkins will therefore automatically move to build and push docker images via executing the docker-compose file and build images for each services based on their Dockerfile specification. This step is crucial for any update or development of the services as customised images would be built and push to the Docker Hub for the use of later deployment.

**Third stage - Ansible configuration:** on the third stage, Jenkins will trigger Ansible configuration to build by executing ansible playbook.yml and inventory.ini. The purpose of the Ansible automate configuration in this project is to connect with the other VMs on the GCP, install and start docker, configuring NGINX, to initialise Docker Swarm manager and to finally join the swarm worker node with the manager node. All the set up of the deployment environment will eventually contribute to the success of the deployment.

![swarm v1](https://user-images.githubusercontent.com/77119427/109540846-f225c780-7aba-11eb-8f9d-64fd7c005126.PNG)

**Last stage - Deployment via Docker Stack Deploy:** The application will be deployed as a stack across docker swarm via the docker manager. I have introduce 5 replicas for version2 and 3 replica for version 1 of the application. More replicas of the service containers introduce more redundency and overhead to the application where requests from the client will be handled without delay. It will also minimise the level of affect if one of the container shutdown or went corrupted.

![v1 docker service ls](https://user-images.githubusercontent.com/77119427/109540524-7c216080-7aba-11eb-9098-e72903a0ff6a.PNG)
### Docker Swarm via Docker and Docker Compose
Docker runs a lightweight version of Linux, which does not include the compilers necessary to compile the underlying C/Fortran libraries. in order to install the package Matplotlib for the 2nd version of the application, first these dependancies should be installed via Dockerfile. The advantage of using docker and docker compose for Matplotlib in the service is, the images is compiled, customised and thereafter push to the docker hub for deployment. For deployment, the images can be easily pulled and deployed to multiple machine without any complication or further individual compiling of the VMs. therefore increased the efficiency of the CI/CD process.

![Matplotlib with docker](https://user-images.githubusercontent.com/77119427/109622634-3bfec400-7b34-11eb-9e1f-a28b99f969d5.PNG)

### NGINX the reverse Proxy 
A proxy server is a go‑between or intermediary server that forwards requests for content from multiple clients to different servers across the Internet. A reverse proxy server is a type of proxy server that typically sits behind the firewall in a private network and directs client requests to the appropriate backend server. A reverse proxy like NGINX provides an additional level of abstraction and control to ensure the smooth flow of network traffic between clients and servers.
The NGINX in this application has act as a “traffic cop,” sitting in front of your backend servers and distributing client requests across a group of servers in a manner that maximizes speed and capacity utilization by achieving Load balancing .

It also act as a security API gateway as it ensures that multiple servers can be accessed from a single record locator or URL regardless of the structure of backend network.

## Risk Assessment
![risk assess](https://user-images.githubusercontent.com/77119427/109629366-a6673280-7b3b-11eb-9005-27db281256f6.PNG)

## Further Improvement 
Overall, this project was successful in creating a service-orientated architecture for my application. However, there are a few improvements that I would like to implement:
- An actual microservice architect should be implemented should there be further development of the application
- A more  asthetically pleasing UI using CSS and bootstrap
- scale up the Docker Swarm to provide higher redundancy and availability
- More elements of the accounting ratios can be introduced for a more comprehensive financail performance report.
- Internal reverse proxy should be set up for internal developers and users in order to keep pirate company assets seperated from public domain.

## Acknowledgements 
QA Academy for the teaching and support so I can carry out this project successfully. My dearest friends and family who inspired and supported me throughout the project.
## Author
Abby X Su

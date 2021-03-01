# Financial Report Generator - A SOA Application

Resource: 

Link to Github project board: https://github.com/AbbyXSu/Financial_report_generator/projects/1

## Requirement and Specification
It is required that an application should be developed using an service-orientated architecture (SOA) design and using following feature technologies: 

- Development and deployment using an orchestration tool Docker Swarm, and containerisation via docker compose and dockerfile 
- Version Control Systerm using Git and Feature_Branch model
- Webhooks is used to trigger Jenkins to recreate and redeploy the changed application
- CI/CD pipeline via Jenkins
- Ansible as an  provisioning, configuration management, and application-deployment tool enabling infrastructure as code, Anisble playbook and inventory is created for setting up and configurating the deployment environment
- NGINX is used as a reverse proxy and load balance for the application

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




 

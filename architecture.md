![ECS Fargate Deployment Architecture](https://github.com/ogasege/data-acq/blob/main/architecture-images/ECS-deployment-architecture.png)

# ECS Fargate Deployment Architecture with AWS Secrets Manager and Monitoring

This architecture is defined by a CloudFormation template to deploy a Dockerized application on AWS ECS using Fargate, leveraging AWS Secrets Manager for securely storing Docker image URIs and CloudWatch for monitoring. The deployment ensures scalability, high availability, and secure task execution.

## CloudFormation Stack Components

### Parameters:
1. **VPC**: Specifies the VPC ID where the ECS service will be deployed.
2. **Subnets**: The list of subnets in which the ECS service will operate. This ensures availability across different Availability Zones.
3. **ContainerPort**: The port on which the Docker container listens, with a default value of 80.
4. **DesiredCount**: The desired number of tasks that should run in the ECS service, defaulting to 1.
5. **DockerSecret**: The name of the AWS Secrets Manager secret that contains the Docker image URI.

---

## Resources:

### 1. **ECSCluster**
   - A managed container cluster service that orchestrates Docker containers. 
   - Defined as `AWS::ECS::Cluster` with the name `data-acq-cluster`.

### 2. **ECSTaskExecutionRole**
   - An IAM role allowing ECS tasks to interact with AWS services such as CloudWatch (for logging) and ECR (for pulling Docker images). 
   - The role includes policies for creating log streams, pushing log events, and pulling container images from ECR.

### 3. **ECSTaskDefinition**
   - Defines the ECS task which describes the Docker container, its resource allocations (CPU, Memory), and how it interacts with other AWS services. 
   - The task pulls the Docker image from AWS Secrets Manager using the secret `DockerSecret` and runs the container with specified CPU (256 units) and memory (512MB).
   - **Log Configuration**: Integrated with CloudWatch logs for monitoring.

### 4. **ECSSecurityGroup**
   - Controls inbound access to the ECS tasks by allowing HTTP traffic on the specified container port (default: 80).
   - This security group ensures the Docker container can receive traffic, allowing inbound traffic over TCP on the `ContainerPort`.

### 5. **ECSService**
   - The ECS service manages the tasks, ensuring the desired number of tasks are running at any given time. It scales tasks using Fargate's serverless capabilities and ensures load balancing.
   - **Network Configuration**: Tasks are assigned public IP addresses and deployed into the subnets provided, with the associated security group controlling access.
   - **Health Check Grace Period**: A grace period of 60 seconds is set to ensure smooth startup and health checking of tasks.

### 6. **CloudWatch Logs**
   - AWS CloudWatch is configured to collect logs from the ECS tasks, enabling real-time monitoring and visibility into application performance and health.

---

## Outputs:
1. **ECSClusterName**: The name of the ECS cluster created.
2. **ECSServiceName**: The name of the ECS service managing the application tasks.

---

## Security and Monitoring:
- **AWS Secrets Manager** securely stores and retrieves the Docker image URI, ensuring that sensitive information like repository credentials are not hardcoded in the task definition.
- **CloudWatch Logs** allows real-time log tracking and troubleshooting for the running ECS tasks.
- **ECS Auto Scaling** (not explicitly defined here) can be integrated to dynamically scale the number of running tasks based on CloudWatch alarms, ensuring high availability.

This setup ensures that your containerized application on AWS ECS is deployed securely and can scale based on demand, while leveraging AWS managed services for networking, security, monitoring, and secret management.
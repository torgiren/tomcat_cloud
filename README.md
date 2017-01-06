# Tomcat cloud
Tomcat cloud is Tomcat based pseudo cloud architecture.

Each server machine has X Tomcat server instances - one app per Tomcat server.
Autobalancing tool start and stop Tomcat instances on particular hosts balance utilization of servers in cloud (with respect to defined min and max values of number of instances of particular app


Components:
- Ansible playbook:
  Is used to:
  - install and configure Tomcat server
  - deploy (and upgrade) applications

- Arbiter:
  - Determinate which instances should be started and which should be stopped.
  - Send start and stop requests by Cloud Node
  - Monitor Tomcat instances' health by Cloud Node

- Cloud Node:
  - Receive requests from Arbiter
  - Authorise Arbiter
  - Start and stop Tomcat instances

# Devops_pipeline docker jenkins intrication project
This a devops + jenkins + docker intricate where we build a pipeline between developers and production team with out the help of operation team
In this world of automation and new era of 5g network its very necessary that we overcome the necessity of website management system.so this 
is a little try to make this vision successful .

# Tasks:
For this project for automation process, We have to make 3 jobs on Jenkins:

JOB#1
If Developer push to dev1 branch then Jenkins will fetch from dev and deploy on the dev-docker environment.

JOB#2
If Developer push to master branch then Jenkins will fetch from master and deploy on the master-docker environment. As they both 
dev-docker and master-docker environments are on different docker containers.

JOB#3
Manually the QA team will check (test) for the website running in the dev-docker environment. If it is running fine then Jenkins will merge
the dev branch to master branch and trigger #job 2

# Prerequisits :
. docker-ce 

. Red hat enterprise linux 8(u can use any other)

. Git bash 

. Github account

. Jernkins.

# Requirements:
. first install red hat iso file properly and mount it to your virtual machine
iso link for rhel 8: https://drive.google.com/file/d/1VZ5GLjpo8h35yJQzhMZxwLYRoe_zLxDl/view?usp=sharing

.Oracle vm virtual box link:https://www.virtualbox.org/wiki/Downloads

.Then properly configure yum,download http server ,ngrok.

.for installation of docker follow link: https://docs.docker.com/ee/docker-ee/rhel/

.for installation of jenkins follow link: 
        https://wiki.jenkins.io/display/JENKINS/Installing+Jenkins+on+Red+Hat+distributions

.It requires latest version of openjdk because jenkins run behind with java

.Install git bash from internet .

.While doing the project we recommend you to plz make sure u do these commands:

    systemctl enable httpd
    systemctl disable firewalld

# Project starts:
.first make 2 branches in git bash

.set hooks in master in .git/hooks/post-commit
 
 .Then follow the following steps that i created in drive to complete your project.

https://docs.google.com/document/d/1lgqpEcO0mjkaDKEOV8sbf0qugBxEerPuO0Qhtk4tOyY/edit?usp=sharing

 

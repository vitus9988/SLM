## 라즈베리파이5 우분투 베이스 세팅 (20250221 기준)

### 1. docker install

1) sudo apt-get update
2) sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
3) curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
4) sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
5) sudo apt-get update
6) sudo apt-get install docker-ce docker-ce-cli containerd.io
7) sudo docker run hello-world

### 2. docker build

sudo docker build -t [image name:version] [Dockerfile path]

### 3. docker run [bash shell]

1) sudo docker run -it -d --name [container name] [image name:version] /bin/bash
2) sudo docker exec -it [container id] /bin/bash



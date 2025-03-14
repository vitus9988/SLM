## 라즈베리파이5 우분투 베이스 세팅 (20250221 기준)

### 1. docker install

```bash
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo docker run hello-world
```

### 2. docker build

```bash
sudo docker build -t [image name:version] [Dockerfile path]
```
### 3. docker run [bash shell]

```bash
sudo docker run -it -d --name [container name] [image name:version] /bin/bash
or
sudo docker run -it -d -p [host port:container port] --name [container name] [image name:version] /bin/bash
sudo docker exec -it [container id] /bin/bash
```




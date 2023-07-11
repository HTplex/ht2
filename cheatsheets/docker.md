# Docker Cheatsheet
## install docker
offical link: https://docs.docker.com/engine/install/ubuntu/
simple script:
```
curl https://get.docker.com | sh \
  && sudo systemctl --now enable docker
```
## install docker nvidia runtime
official link: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

setup 
install nvidia-container toolkit
```
distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
      && curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
      && curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | \
            sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
            sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list

sudo apt-get update
sudo apt-get install -y nvidia-container-toolkit
sudo nvidia-ctk runtime configure --runtime=docker
sudo systemctl restart docker
```
## install docker compose
As of Jun.25.2023, docker compose no longer need extra installation 


## basic commands 
build using docker compose + start docker
`docker compose -f ./tensorrt.yaml up -d`
list docker images
`docker images`
check containers
`docker ps -a`
attach docker
`docker exec -it <container-id> /bin/bash`
remove instance
`docker rm <container-id> -f`
remove image
`docker rmi <images>`


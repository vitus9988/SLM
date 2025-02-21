# Dockerfile 예시
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.11 python3-pip locales language-pack-ko vim curl tmux zip git wget htop && \
    curl https://getcroc.schollz.com/ | bash && \
    locale-gen ko_KR.utf8 && \
    dpkg-reconfigure locales && \
    echo "export LANGUAGE=ko_KR.UTF-8" >> ~/.bashrc && \
    echo "export LANG=ko_KR.UTF-8" >> ~/.bashrc && \
    /bin/bash -c "source ~/.bashrc" && \
    rm /usr/bin/python3 && \
    ln -s /usr/bin/python3.11 /usr/bin/python3 && \
    apt-get install -y python3.11-distutils && \
    apt-get remove -y software-properties-common && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/* &&\
    pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu && \
    pip3 install transformers numpy pandas

WORKDIR /home/workspace

## prometheus install (20250322 기준)

### 1. tar file download && run

https://prometheus.io/download/ -> LTS "linux-armv7" version link copy
```bash
wget prometheus-*.linux-armv7.tar.gz
tar -zxvf prometheus-*.linux-armv7.tar.gz
cd prometheus-*.linux-armv7
./prometheus --config.file=prometheus.yml
```

### 2. docker container
```bash
docker run -d -p [host port:container port] \
-v [prometheus-*.linux-armv7 path]:/prometheus \
--name prometheus \
alpine \
/prometheus/prometheus --config.file=/prometheus/prometheus.yml
```

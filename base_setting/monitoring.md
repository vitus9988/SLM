## prometheus & node_exporter & grafana install

### 1. prometheus tar file download && run

https://prometheus.io/download/ -> LTS "linux-armv7" version link copy
```bash
wget prometheus-*.linux-armv7.tar.gz
tar -zxvf prometheus-*.linux-armv7.tar.gz
cd prometheus-*.linux-armv7
./prometheus --config.file=prometheus.yml
```

### 2. node_exporter tar file download && run

https://prometheus.io/download/#node_exporter -> Release notes "linux-armv7" version link copy
```bash
wget node_exporter-*.linux-armv7.tar.gz
tar -zxvf node_exporter-*.linux-armv7.tar.gz
cd node_exporter-*.linux-armv7
./node_exporter
```

### 3. prometheus.yml edit
```bash
[BEFORE]
scrape_configs:
    - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]

[AFTER]
scrape_configs:
    - job_name: "node_exporter" # any
    static_configs:
      - targets: ["localhost:9100"] # node_exporter base port
```

### a. prometheus + node_exporter docker container
```bash
docker run -d -p [prometheus host port:container port] -p [node_exporter host port:container port]\
-v [prometheus-*.linux-armv7 path]:/prometheus \
-v [node_exporter-*.linux-armv7 path]:/node_exporter \
--name prometheus \
alpine \
sh -c "/prometheus/prometheus --config.file=/prometheus/prometheus.yml & /node_exporter/node_exporter"
```

### b. grafana docker container run
```bash
docker run -d -p 3000:3000 grafana/grafana
```


### 4. prometheus + node_exporter + grafana docker-compose.yml
```bash
docker network create monitoring

vim docker-compose.yml

version: '3'
services:
  prometheus:
    image: alpine
    container_name: prometheus
    ports:
      - "[prometheus host port:container port]"
      - "[node_exporter host port:container port]"
    volumes:
      - [prometheus-*.linux-armv7 path]:/prometheus
      - [node_exporter-*.linux-armv7 path]:/node_exporter
    command: sh -c "/prometheus/prometheus --config.file=/prometheus/prometheus.yml & /node_exporter/node_exporter"
    networks:
      - monitoring
    restart: always

  grafana:
    image: grafana/grafana
    container_name: grafana
    ports:
      - "3000:3000"
    volumes:
      - [local grafana mapping path]:/var/lib/grafana
    networks:
      - monitoring
    user: "$UID:$GID"
    restart: always

networks:
  monitoring:
    driver: bridge


docker compose up -d
```

### 5. grafana setting

http://localhost:3000
(id:admin / pw: admin [basic account])

1. [Connections] -> [Data source]
2. connections prometheus server URL -> http://prometheus:prometheus port
3. Save & Test

4. [Dashboards] -> [New] -> [Import]
4-1. [grafana.com/dashboards](https://grafana.com/grafana/dashboards/) -> user Dashboard templates ID copy
5. Dashboard ID paste -> [Load] -> [select prometheus data source] -> [Import]



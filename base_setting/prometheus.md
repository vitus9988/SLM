## prometheus & node_exporter install (20250322 기준)

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

### 4. docker container
```bash
docker run -d -p [prometheus host port:container port] -p [node_exporter host port:container port]\
-v [prometheus-*.linux-armv7 path]:/prometheus \
-v [node_exporter-*.linux-armv7 path]:/node_exporter \
--name prometheus \
alpine \
sh -c "/prometheus/prometheus --config.file=/prometheus/prometheus.yml & /node_exporter/node_exporter"
```



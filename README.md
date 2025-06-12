# SLM project

라즈베리파이5(8G) 베이스의 SLM 운용 정리 레포


## Setting & Install

- [llamacpp](base_setting/llamacpp.md)
  - llamacpp-OpenBLAS [Dockerfile](base_setting/docker/Dockerfile(llamacpp-OpenBLAS))
    ```bash
    docker pull vitus9988/llamacpp-openblas:latest
    ```
- [ollama](base_setting/ollama.md)
- [grafana & prometheus](base_setting/monitoring.md)


## Model Test

|Model|Tps|
|---|---|
|lama3.2:1b|8|
|qwen2.5:0.5b|21|
|deepseek-r1:1.5b|9|
|gemma2:2b-instruct-q4_K_S|5|
|qwen2.5:0.5b-instruct-q4_K_S|21|
|qwen2.5:3b-instruct-q4_K_M|5|
|kanana-nano-2.1b-instruct-Q4_K_M|7|
|gemma-3-1b-it-Q4_K_M|13|
|gemma-3-4b-it-Q4_K_M|4|
|EXAONE-Deep-2.4B-Q4_K_M|6|
|HyperCLOVAX-SEED-Text-Instruct-1.5B-Q4_K_M|9|






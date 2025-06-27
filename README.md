# SLM project

Raspberry Pi 5 base SLM Operation

----

## Quick setting / start

- [llamacpp](base_setting/llamacpp.md)
  - llamacpp-OpenBLAS [Dockerfile](base_setting/docker/Dockerfile(llamacpp-OpenBLAS-Lite))
    
    ```sh
    # docker image pull
    docker pull vitus9988/llamacpp-openblas:latest

    # llama-cli local model
    docker run --rm -v $(pwd)/models:/models \
    vitus9988/llamacpp-openblas:latest llama-cli \
    -m /models/gemma-3n-E2B-it-Q4_K_M.gguf -p "세계에서 가장 높은산은?"
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
|gemma-3n-E2B-it-litert-lm-preview|3|






## llama.cpp install

### 1. cmake install

#build-essential, openssl installed
```bash
https://cmake.org/download tar file download (wget link)
tar -zxvf [cmake tar file]
cd [cmake dir]
./bootstrap
#openssl not find error -> apt-get update / apt-get install libssl-dev
make
make install
```

### 1-1. vulkan install
```bash
arm vulkan sdk install
https://github.com/jakoch/vulkan-sdk-arm (arm base ubuntu vulkan sdk)

tar -xJvf vulkansdk-arm-*.tar.xz
cd [vulkan sdk dir]
source setup-env.sh
./vulkan -j 1
```

### 2. llama-cpp install
```bash
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
[CPU env]
cmake -B build
cmake --build build --config Release
pip3 install -r requirements.txt

[vulkan env]
cmake -B build -DGGML_VULKAN=ON
cmake --build build --config Release
pip3 install -r requirements.txt
```

### 3. model convert & quantize
```bash
1) huggingface model local download
huggingface-cli download [model name] --local-dir=[model save path]

2) download model gguf convert
python3 convert_hf_to_gguf.py [model save path] --outtype [convert type] ex)bf16  

3) gguf convert model quantize
cd llama.cpp/build/bin
./llama-quantize [gguf model path] [quantize save path] [quantize type] ex)Q4_K_M
```

### 4. model use
```bash
1) llama.cli run
cd llama.cpp/build/bin
./llama-cli -m [model path] -p [prompt]

2) llama server run
cd llama.cpp/build/bin
./llama-server -m [model path] --port [port]
# docker container env -> [--host 0.0.0.0] option add

2-1) llama server run (multimodal)
ex) SmolVLM-500M-Instruct-f16 
cd llama.cpp/build/bin/
./llama-server --jinja -fa -m SmolVLM-500M-Instruct-f16.gguf \
--mmproj mmproj-SmolVLM-500M-Instruct-f16.gguf -c 2048 -ngl 0 --no-mmproj-offload -t 10

[shell script call]
#!/usr/bin/env bash
IMG=$1
MODEL="SmolVLM-500M-Instruct-f16"
B64=$(base64 -w0 "$IMG")

curl -H "Content-Type: application/json" \
     -H "Authorization: Bearer sk-local" \
     -d @- http://localhost:8080/v1/chat/completions <<EOF
{
  "model": "$MODEL",
  "max_tokens": 64,
  "temperature": 0.1,
  "presence_penalty": 0.3,
  "messages": [{
    "role": "user",
    "content": [
      {"type":"image_url",
       "image_url":{"url":"data:image/jpeg;base64,${B64}"}},
      {"type":"text","text":"Briefly describe the following image."}
    ]
  }]
}
EOF

chmod +x script.sh
./script.sh [imgfile]


3) Like OAI Call
[model stream]
cd llama.cpp/build/bin
./llama-server --jinja -fa -m [model path]

    [python call]
    import request
    url = "http://localhost:8080/v1/chat/completions"
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "Hello world"}]
    }
    resp = requests.post(url, json=payload)
    print(resp.json())
```

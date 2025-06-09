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

4-1) llama.cli run
cd llama.cpp/build/bin
./llama-cli -m [model path] -p [prompt]

4-2) llama server run
cd llama.cpp/build/bin
./llama-server -m [model path] --port [port]
# docker container env -> [--host 0.0.0.0] option add

4-3) Like OAI Call
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

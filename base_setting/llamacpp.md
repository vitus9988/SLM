## llama.cpp install (20250305 기준)

### 1. cmake install

(build-essential, openssl installed)
```bash
https://cmake.org/download tar file download (wget link)
tar -zxvf [cmake tar file]
cd [cmake dir]
./bootstrap
(openssl not find error -> apt-get update / apt-get install libssl-dev)
make
make install
```

### 2. llama-cpp install

1) git clone https://github.com/ggml-org/llama.cpp
2) cd llama.cpp
[CPU env]
3) cmake -B build
4) cmake --build build --config Release
5) pip3 install -r requirements.txt


### 3. model convert & quantize

1) huggingface model local download
ex) huggingface-cli download [model name] --local-dir=[model save path]

2) download model gguf convert
python3 convert_hf_to_gguf.py [model save path] --outtype [convert type] ex)bf16  

3) gguf convert model quantize
cd llama.cpp/build/bin
./llama-quantize [gguf model path] [quantize save path] [quantize type] ex)Q4_K_M

4) llama.cli run
cd llama.cpp/build/bin
./llama-cli -m [model path] -p [prompt]

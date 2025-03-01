## ollama 베이스 세팅 (20250301기준)

### 1. ollama install

curl -fsSL https://ollama.com/install.sh | sh

### 2. model load

ollama serve

1) ollama run [model name]

or 

1) *.gguf model download

2) vim Modelfile

```python
From [*.gguf absolute path]
Template [model template]
```

3) ollama create [local model name] -f Modelfile

4) ollama run [local model name]

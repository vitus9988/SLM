## discord bot - llama.cpp

### 1. llama.cpp server oai call 로컬 모델 실행
```bash
llama.cpp/build/bin
./llama-server --jinja -fa -m [model path]
```

### 2. app.py 실행
```bash
asyncio.sleep(8) 시간만큼의 대화를 저장,
로컬 모델에 context 전달하여 결과를 채널에 전송.
기존에 저장된 대화는 초기화.
```

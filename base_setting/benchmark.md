## lm-evaluation-harness & llamacpp python server

### 1. llamacpp server run (config.json)

config.json (Raspberry Pi 5 8GB setting)
```bash
{
  "host": "0.0.0.0",
  "port": 8000,
  "models": [
    {
      "model": model path,
      "n_gpu_layers": 0,
      "n_threads": 4,
      "n_threads_batch": 4,
      "n_batch": 256,
      "n_ubatch": 256,
      "type_k": 8,
      "use_mmap": true,
      "use_mlock": false
    }
  ]
}
```
```bash
python3 -m llama_cpp.server --config_file config.json
```

### 2. lm-eval benchmark testing
```bash
lm_eval --model gguf \
--model_args base_url=http://0.0.0.0:8000 \
--tasks kobest_boolq \
--num_fewshot 0 \
--seed 42 \
--batch_size auto \
--output_path ./kobest0shot \
--log_samples \
--show_config \
--limit 0.01
```

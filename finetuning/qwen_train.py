import os
import transformers
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from datasets import load_dataset
from wandb import login
from trl import SFTConfig, SFTTrainer, DataCollatorForCompletionOnlyLM

#qwen2.5 full finetuning

model_id = "Qwen/Qwen2.5-7B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    torch_dtype=torch.bfloat16,
)

data = load_dataset("MarkrAI/KOpen-HQ-Hermes-2.5-60K", split="train")

def apply_chat(x):
    context = x['text']
    Instruction = x['Instruction']
    Reasoning = x['Reasoning']
    Reasoning_Answer = x['Reasoning Answer']
    Final_Answer = x['Final Answer']
    chat = [
        # {"role": "user", "content": f"# Context: {context}\n# Question: {Instruction}"},
        # {"role": "assistant", "content": f"# Subquestions: {Reasoning}\n# Subquestion Answers: {Reasoning_Answer}\n# Final Answer: {Final_Answer}"},
        {"role": "user", "content": f"{Instruction}"},
        {"role": "assistant", "content": f"{Final_Answer}"},
    ]
    return tokenizer.apply_chat_template(chat, tokenize=False)

data = data.map(
    lambda x: {'text': apply_chat(x)},
    num_proc=16,
)

response_template = "<|im_start|>assistant\n"
collator = DataCollatorForCompletionOnlyLM(response_template, tokenizer=tokenizer)
tokenizer.pad_token = tokenizer.eos_token

sft_config = SFTConfig(
    dataset_text_field="text",
    max_seq_length=4096,
    output_dir="/tmp",
    per_device_train_batch_size=1,
    gradient_accumulation_steps=1,
    # max_steps=100, ## 초소량만 학습: 100 step만 학습. 약 4분정도 걸립니다.
    learning_rate=1e-5,
    bf16=True,
    logging_steps=100,
    # optim="lomo", # 31.4GB @ bs=1
    optim="adalomo", # 36.8GB @ bs=4
    # optim="adafactor", # CUDA OOM @ bs=1
    # optim="adamw_hf", # CUDA OOM @ bs=1
    gradient_checkpointing=True,
    report_to='wandb',
    save_strategy='steps',
    save_steps=10000,
    use_liger=True,
    dataset_num_proc=16,
    push_to_hub=True,
    hub_model_id='beomi/Qwen2.5-7B-Instruct-kowiki-qa',
)

trainer = SFTTrainer(
    model=model,
    train_dataset=data,
    args=sft_config,
    data_collator=collator,
)

model.config.use_cache = False  # silence the warnings. Please re-enable for inference!
trainer.train()
model.eval()
model.config.use_cache = False

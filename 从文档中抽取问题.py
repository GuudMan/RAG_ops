# 导入所需的库
from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig
import torch
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0, 1"

# 定义模型路径
mode_name_or_path = '/root/autodl-tmp/langchainqwen14b/model_local/qwen/Qwen1.5-7B-Chat'

# 定义一个函数，用于获取模型和tokenizer
def get_model():
    # 从预训练的模型中获取tokenizer
    tokenizer = AutoTokenizer.from_pretrained(mode_name_or_path, use_fast=False)
    # 从预训练的模型中获取模型，并设置模型参数
    model = AutoModelForCausalLM.from_pretrained(mode_name_or_path, torch_dtype=torch.bfloat16,  device_map="auto")
  
    return tokenizer, model

# 加载Qwen1.5-4B-Chat的model和tokenizer
tokenizer, model = get_model()

file_path = "./ops/zedx2txt/director/安全/1571996119322.txt"
text = ""
with open(file_path, mode="r", encoding="utf-8") as f:
    lines = f.readlines()
    if lines:
        for line in lines:
            text += line

prompt = "将下面的文字抽取为问题，答案对的形式， 尽可能抽取多个问题，只需返回问答答案对， 以字典形式返回。\n" + text

print(prompt)
messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
    ]

# 调用模型进行对话生成
input_ids = tokenizer.apply_chat_template(messages,tokenize=False,add_generation_prompt=True)
model_inputs = tokenizer([input_ids], return_tensors="pt").to('cuda')
generated_ids = model.generate(model_inputs.input_ids,max_new_tokens=512)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]
response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

print(response)
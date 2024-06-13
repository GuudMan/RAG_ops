from TinyAgent.Agent import Agent
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "2, 3"


agent = Agent("./model_local/qwen/Qwen1.5-7B-Chat")

print(agent.system_prompt)


response, _ = agent.text_completion(text="你好", history=[])
print(response)
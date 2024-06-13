
# import torch
# from modelscope import snapshot_download, AutoModel, AutoTokenizer
# import os
# model_dir = snapshot_download('qwen/Qwen1.5-14B-Chat', 
# cache_dir='/root/autodl-tmp/langchainqwen14b/model_local')

# import torch
# from modelscope import snapshot_download, AutoModel, AutoTokenizer
# from modelscope import GenerationConfig
# model_dir = snapshot_download('qwen/Qwen1.5-7B-Chat', 
#                               cache_dir='/root/autodl-tmp/langchainqwen14b/model_local', 
#                               revision='master')


# from modelscope import snapshot_download
# model_dir = snapshot_download("BAAI/bge-reranker-base", 
#                               cache_dir='/root/autodl-tmp/langchainqwen14b/model_local',
#                               )

from huggingface_hub import snapshot_download
snapshot_download(
  repo_id="BAAI/bge-reranker-base",
  local_dir='/root/autodl-tmp/langchainqwen14b/model_local'
)
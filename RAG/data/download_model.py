import torch
from modelscope import snapshot_download, AutoModel, AutoTokenizer
import os

# 下载internLM模型
model_dir = snapshot_download('Shanghai_AI_Laboratory/internlm-chat-7b', cache_dir='RAG/model', revision='v1.0.3')


# 下载embedding模型：sentence-transformer
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
# 下载模型
os.system('huggingface-cli download --resume-download sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 --local-dir RAG/model/sentence-transformer')
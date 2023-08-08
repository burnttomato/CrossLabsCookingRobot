from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch
import sys

cache_path = "../../../.cache/huggingface/hub"


model_id="tiiuae/falcon-7b-instruct"
tokenizer=AutoTokenizer.from_pretrained(model_id,trust_remote_code=True)
model=AutoModelForCausalLM.from_pretrained(model_id,device_map="auto",torch_dtype=torch.float16, cache_dir=cache_path ,trust_remote_code=True)


path = sys.argv[1]
text_file = open(path, "r")

prompt = text_file.read()
text_file.close()

pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
)
sequences = pipeline(
    prompt,
    max_length=300,
    do_sample=True,
    top_k=10,
    num_return_sequences=10,
    eos_token_id=tokenizer.eos_token_id,
)
for seq in sequences:
    print(f"Result: {seq['generated_text']}")

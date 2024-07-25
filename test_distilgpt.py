import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def test_model():
    try:
        print("Loading DistilGPT-2 model...")
        model = GPT2LMHeadModel.from_pretrained('distilgpt2')
        tokenizer = GPT2Tokenizer.from_pretrained('distilgpt2')

        print("Generating text with DistilGPT-2 model...")
        prompt = "Hello, World!"
        input_ids = tokenizer.encode(prompt, return_tensors='pt')
        attention_mask = torch.ones(input_ids.shape, dtype=torch.long)
        output = model.generate(input_ids, attention_mask=attention_mask, max_length=50, pad_token_id=tokenizer.eos_token_id)
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
        print("Generated text:", generated_text)
    except Exception as e:
        print(f"Error during model test: {e}")

if __name__ == "__main__":
    test_model()


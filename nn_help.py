import pandas as pd
from transformers import LlamaForCausalLM, LlamaTokenizer
import torch

# Load the Titanic dataset
df = pd.read_csv('titanic.csv')

# Initialize LLaMA 2 model and tokenizer
model_name = "meta-llama/Llama-2-7b-chat-hf"  # You might need to change this based on your access
tokenizer = LlamaTokenizer.from_pretrained(model_name)
model = LlamaForCausalLM.from_pretrained(model_name)

def generate_response(question, context):
    prompt = f"Context: {context}\n\nQuestion: {question}\n\nAnswer:"
    inputs = tokenizer(prompt, return_tensors="pt")
    
    with torch.no_grad():
        output = model.generate(**inputs, max_length=200)
    
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response.split("Answer:")[1].strip()

def main():
    print("Titanic Dataset Q&A System")
    print("Type 'exit' to quit")
    
    while True:
        question = input("\nEnter your question about the Titanic dataset: ")
        if question.lower() == 'exit':
            break
        
        # Provide a relevant context from the dataset
        context = df.head().to_string()
        
        response = generate_response(question, context)
        print(f"\nAnswer: {response}")

if __name__ == "__main__":
    main()
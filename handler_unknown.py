from transformers import pipeline

# Load LLM pipeline (distilgpt2 for now, upgradeable later)
llm = pipeline("text-generation", model="distilgpt2", framework="pt")

def handle_unknown(user_input):
    """
    Generate an open-ended response using an LLM.
    Used when no known intent is matched.
    """
    output = llm(user_input, max_length=100, do_sample=True, truncation=True)
    return output[0]['generated_text'].strip()

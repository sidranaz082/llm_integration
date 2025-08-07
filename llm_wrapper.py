from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

def generate_response(prompt):
    try:
        result = generator(prompt, max_new_tokens=100, truncation=True)
        return {
            "success": True,
            "response": result[0]["generated_text"]
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
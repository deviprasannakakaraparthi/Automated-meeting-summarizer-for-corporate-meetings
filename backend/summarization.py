from transformers import PegasusForConditionalGeneration, PegasusTokenizer

# Load pre-trained Pegasus model and tokenizer
model_name = "google/pegasus-xsum"  # You can use other variants like "google/pegasus-large"
model = PegasusForConditionalGeneration.from_pretrained(model_name)
tokenizer = PegasusTokenizer.from_pretrained(model_name)

def summarize_text(text):
    # Tokenize the text
    inputs = tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)

    # Generate summary
    summary_ids = model.generate(inputs['input_ids'], num_beams=4, min_length=30, max_length=150, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary


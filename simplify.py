from transformers import pipeline

# Load summarization model
summarizer = pipeline("summarization", model="t5-small")

def simplify_text(text):
    if not text.strip():
        return "Please enter some text to simplify."

    # Limit text size to avoid memory issues
    text = text.strip()
    text = text[:1000]  # first 1000 characters

    # Generate summary
    summary = summarizer(text, max_length=60, min_length=20, do_sample=False)

    # Convert to bullet points
    simplified = summary[0]['summary_text']
    bullets = simplified.replace('.', '.\n- ')
    final_output = "- " + bullets.strip()
    return final_output

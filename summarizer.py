# summarizer.py

from transformers import pipeline

summarizer = pipeline("summarization", model="knkarthick/MEETING_SUMMARY", tokenizer="knkarthick/MEETING_SUMMARY")

def summarize_text(text, max_chunk=1000):
    try:
        print("⚙️ Preprocessing text...")
        text = text.strip().replace("\n", " ")
        chunks = [text[i:i + max_chunk] for i in range(0, len(text), max_chunk)]
        summaries = []
        print(f"📦 Total chunks: {len(chunks)}")

        for i, chunk in enumerate(chunks):
            print(f"🔹 Summarizing chunk {i + 1}/{len(chunks)}")
            summary = summarizer(chunk, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
            summaries.append(summary)

        return " ".join(summaries)
    except Exception as e:
        print("❌ Summarization failed:", e)
        return "Summarization failed."

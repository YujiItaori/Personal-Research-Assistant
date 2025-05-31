# app.py

from flask import Flask, render_template, request
from scraper import fetch_links_and_articles
from summarizer import summarize_text
import re

app = Flask(__name__)

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ""
    if request.method == 'POST':
        query = request.form['query']
        print("🔍 Received query:", query)

        articles = fetch_links_and_articles(query)
        print(f"📄 Found {len(articles)} articles.")

        texts = [clean_text(article['text']) for article in articles if article['text']]
        texts.sort(key=len, reverse=True)
        combined_text = " ".join(texts[:2])  # top 2 longest articles
        combined_text = combined_text[:1500]  # limit to avoid overload

        if combined_text:
            try:
                print("🧠 Running summarizer...")
                summary = summarize_text(combined_text)
                print("✅ Summary generated.")
            except Exception as e:
                print("❌ Error during summarization:", e)
                summary = "Summarization failed."
        else:
            summary = "No content found."
            print("⚠️ No text extracted from articles.")

    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)

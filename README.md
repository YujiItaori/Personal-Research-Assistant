# 🧠 Personal Research Assistant

Your AI-powered assistant for researching any topic. Just enter a query, and this app will search the web, extract relevant information from top articles, and generate a concise summary — all in seconds.

---

## 🔍 Why Use This?

Reading through multiple articles can be time-consuming, especially when you're doing research. This assistant does the heavy lifting for you:

- ✅ Automates web search  
- ✅ Extracts meaningful content from top-ranked articles  
- ✅ Summarizes the key points using NLP  
- ✅ Provides results in seconds  

Whether you're a student, researcher, developer, or just curious — this tool saves time and effort.

---

## 🚀 Features

- 🌐 **Web Search Integration** via DuckDuckGo  
- 📄 **Automatic Content Extraction** from real articles  
- 🧠 **Smart Summarization** using DistilBART transformer  
- ⚡ **Multi-threaded fetching** for speed  
- 🎯 **Clean & Simple UI** built with Flask  

---

## 📦 Technologies Used

- `Python`
- `Flask`
- `transformers` (Hugging Face)
- `newspaper3k` (for article parsing)
- `duckduckgo_search` (for web results)
- `concurrent.futures` (for threading)

---

## 💡 How It Works

1. User enters a search query
2. The assistant searches the web using DuckDuckGo
3. Top 3 article links are fetched and parsed using `newspaper3k`
4. The two longest relevant articles are selected
5. Extracted text is summarized using a pretrained NLP model

---

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.8 or later
- pip

### Installation

## Clone the repo
git clone https://github.com/YujiItaori/Personal-Research-Assistant.git
cd Personal-Research-Assistant

## (Optional) Create a virtual environment
python -m venv research_env
research_env\Scripts\activate  # On Windows

## Install dependencies
pip install -r requirements.txt

## Run the app
flask run
Open your browser and go to: http://127.0.0.1:5000

## 🖼️ Example Use Case
Query: What is Artificial Intelligence?
Result: A summarized version of the most informative articles on the topic, presented in a concise and readable format.


## 🚧 Future Improvements
🔎 Add keyword highlighting in the summary

📈 Store search history and summaries

🎙️ Add voice input for hands-free searching

🌍 Multilingual summarization support

💾 Option to export summary as PDF or text file

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

## 🪪 License
This project is open-source and available under the MIT License.

## ✨ Credits
Created by Yuji Itaori
Using open-source technologies from the AI and Python communities.![Screenshot 2025-05-31 160514](https://github.com/user-attachments/assets/cd5a042a-f4b7-4645-848b-b5490342446a)


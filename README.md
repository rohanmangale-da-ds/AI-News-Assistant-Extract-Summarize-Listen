# 📰 AI-News-Assistant-Extract-Summarize-Listen

This project automates the process of fetching live news from Times of India, summarizing it using Hugging Face NLP models, converting it into audio speech, and finally allowing the user to listen to the news one by one or all at once.

It integrates web scraping, transformer-based summarization (Hugging Face BART model), and text-to-speech (TTS) audio generation using Hugging Face CSM model, making it a complete AI-powered News Assistant.

## Features

🔎 News Extraction → Scrapes latest headlines and articles from Times of India.

✂️ Summarization → Summarizes news using Hugging Face facebook/bart-large-cnn.

🎙️ Audio Generation → Converts summarized text into .wav audio files using Hugging Face sesame/csm-1b.

🎧 Play All News → Plays audio files sequentially with synchronized headline & summary text.

⏱️ Time Tracking → Reports how long extraction, summarization, and audio generation take.

## Technologies Used

Python 3.10+

BeautifulSoup4 – Web scraping

Requests – Fetching webpage content

Hugging Face Transformers

facebook/bart-large-cnn → Summarization

sesame/csm-1b → Text-to-Speech (TTS)

Torch – Deep learning backend

TQDM – Progress tracking

Pygame – Audio playback

Winsound – System notifications


## Project Structure
📦 AI-News-Assistant
├── main.py                # Orchestrates full pipeline (extraction → summarization → audio → playback)
├── news_extractor.py      # Scrapes news from Times of India & saves raw data
├── summary_text.py        # Summarizes scraped articles using transformers
├── play_all.py            # Plays generated audio with headline + summary display
├── news_data.json         # Raw extracted news (generated dynamically)
├── summarized_news_data.json # Summarized news (generated dynamically)
├── listen_news/           # Folder where generated .wav audio files are stored


## ⚙️ How It Works

Run the pipeline

python main.py


News Extraction → Scrapes articles from Times of India and saves them to news_data.json.

Summarization → Uses Hugging Face facebook/bart-large-cnn to summarize articles → output saved in summarized_news_data.json.

Audio Generation → Uses Hugging Face sesame/csm-1b to convert summarized text to .wav audio → stored in listen_news/.

Playback → User can play all generated audios with synchronized headline & summary.

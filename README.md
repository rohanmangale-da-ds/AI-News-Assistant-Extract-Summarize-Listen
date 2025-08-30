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

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## Sample news data and ausio files are also in repo
### News 1
<img width="975" height="245" alt="image" src="https://github.com/user-attachments/assets/3d26da7f-2b53-4650-aeb8-961049095c7b" />

### News 1 Summarized
<img width="975" height="72" alt="image" src="https://github.com/user-attachments/assets/8bfa72de-3c74-45dd-b765-9f756ef7a64e" />

### News 2
<img width="975" height="196" alt="image" src="https://github.com/user-attachments/assets/67b34e1a-cea4-443c-bc31-a8fb999bc2d2" />

### News 2 Summarized
<img width="975" height="70" alt="image" src="https://github.com/user-attachments/assets/2c7d3d94-afbc-41ff-944a-8116b4c33d9e" />

### News 3
<img width="975" height="236" alt="image" src="https://github.com/user-attachments/assets/771e631f-48fe-4cc9-9309-9a9902377faa" />

### News 3 Summarized
<img width="975" height="85" alt="image" src="https://github.com/user-attachments/assets/5189344b-4ae4-486a-b426-de1f03f0c4cd" />






# Use a pipeline as a high-level helper
from transformers import pipeline
import json
import time
import torch
from transformers import CsmForConditionalGeneration, AutoProcessor
from tqdm import tqdm

# import functions
from news_extractor import extractor
from summary_text import news_summarizer
from play_all import play_all_news

# Extract news data
time_taken_to_extract = extractor()

# Summarize news data
time_taken_to_summarize = news_summarizer()


with open('summarized_news_data.json', 'r', encoding='utf-8') as f:
    summarized_news_data = json.load(f)


total_news = int(input(">>> Enter the total number of news articles you want to listen (1-5): "))

model_id = "sesame/csm-1b"
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load processor & model
processor = AutoProcessor.from_pretrained(model_id)
model = CsmForConditionalGeneration.from_pretrained(model_id, device_map=device)
start = time.time() 
# Loop through each news item
# Loop through each news item with tqdm progress bar
for i in tqdm(range(total_news), desc="Generating Audio", unit="news"):
    text = f"Headline {i+1}: {summarized_news_data[i]['headline']} news {summarized_news_data[i]['body']}"

    conversation = [
        {
            "role": "0",
            "content": [
                {
                    "type": "text",
                    "text": text,
                }
            ]
        },
    ]

    # Prepare inputs
    inputs = processor.apply_chat_template(
        conversation,
        tokenize=True,
        return_dict=True,
    ).to(device)

    # Generate audio for each news
    audio = model.generate(
        **inputs,
        output_audio=True,
        max_new_tokens=int(6000),  # proportional to text length
    )

    # Save each audio file separately
    filename = f"listen_news\\news_{i+1}_{summarized_news_data[i]['headline'][10]}..._.wav"
    processor.save_audio(audio, filename)
    print(f"Audio saved: {filename}")

end = time.time()
print()
print("-x-x"*38)
print()
print(f"Total time taken for extraction: {time_taken_to_extract} seconds")
print(f"Total time taken for summarization: {time_taken_to_summarize} seconds")
print(f"Total time taken for audio generation: {end - start} seconds")
import winsound
winsound.Beep(1000, 1500)

# Play all news audio files
user_approved = input(">>> Do you want to play all the news audio files? (y/n): ").strip().lower()

if user_approved == 'y':
    play_all_news(total_news, summarized_news_data)
else:
    print("You chose not to play the news audio files.")











import os
import pygame
import json
import winsound

def play_all_news(total_news, summarized_news_data):
    """
    This function plays all the news articles using the pygame library.
    while showing headlines and summaries.
    """
    # get all the filenames ffrom listen_news directory
    files = os.listdir('listen_news')
    files = [f for f in files if f.endswith('.wav')]
    # Initialize the pygame mixer
    try:
        pygame.mixer.init()
    except pygame.error as e:
        print(f"Error initializing pygame mixer: {e}")
        return

    for i, file in enumerate(files):
        # Check if the file exists
        if (i+1) > total_news:
            break
        file_path = os.path.join("listen_news", file) 
        if not os.path.exists(file_path):
            print(f"Error: {file} not found.")
            continue
        
        try:
            print()
            print('-o-o'*38)
            print()
            print(f"Headline: {summarized_news_data[i]['headline']}")
            print(f"Summary: {summarized_news_data[i]['body']}")
            
            # Load the sound file
            sound = pygame.mixer.Sound(file_path)
            
            # Play the sound
            sound.play()
            
            # Wait for the sound to finish playing
            while pygame.mixer.get_busy():
                pygame.time.Clock().tick(10)

        except Exception as e:
            print(f"Error playing {file}: {e}")
        winsound.Beep(800, 800)

if __name__ == "__main__":
    with open('summarized_news_data.json', 'r', encoding='utf-8') as f:
        summarized_news_data = json.load(f)
    total_news = int(input(">>> Enter the total number of news articles you want to listen (1-5): "))
    # Example usage: play all news audio files
    # You can change the number to match the number of news articles you have
    # Example usage (assuming you have WAV files named news_1.wav, news_2.wav, etc.)
    play_all_news(total_news, summarized_news_data)
  
    
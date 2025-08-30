import json 
from transformers import pipeline
import time
import json
import winsound

def news_summarizer():
    """
    This function summarizes news articles from a JSON file and saves the summaries to another JSON file.
    It returns the total time taken for the summarization process.
    """
    start = time.time()
    with open('news_data.json', 'r', encoding='utf-8') as f:
        all_news_data = json.load(f)

    total_news = len(all_news_data)

    from transformers import pipeline

    summarized_news = []

    def chunk_text(text, max_chars=1500):
        return [text[i:i+max_chars] for i in range(0, len(text), max_chars)]

    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    for i in range(total_news):
        ARTICLE = all_news_data[i]['body']
        Headline = all_news_data[i]['headline']

        chunks = chunk_text(ARTICLE, max_chars=1500)
        chunk_summaries = []

        for chunk in chunks:
            summary = summarizer(chunk, max_length=80, min_length=min(40, len(chunk)-1), do_sample=False)
            chunk_summaries.append(summary[0]['summary_text'])

        final_summary = " ".join(chunk_summaries)

        print(f"Headline: {Headline}")
        print(f"Summary: {final_summary}")
        print("-" * 156)
        summary_dict = {
                        "headline": Headline,
                        "body": final_summary
                                                }
        #Append the dictionary to your list
        summarized_news.append(summary_dict)

    with open('summarized_news_data.json', 'w', encoding='utf-8') as f:
        # Use json.dump() to write the entire list
        json.dump(summarized_news, f, indent=4, ensure_ascii=False)

    end = time.time()
    total_time = end-start
    print(f"Total time taken: {end - start} seconds")
    winsound.Beep(1000, 500)
    return total_time


if __name__ == "__main__":
    news_summarizer()
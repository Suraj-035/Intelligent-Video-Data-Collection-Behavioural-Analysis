# scripts/scrape_youtube.py
from yt_dlp import YoutubeDL

def search_videos(query, max_results=5):
    ydl_opts = {
        "quiet": True,
        "extract_flat": True,
        "force_generic_extractor": True
    }

    with YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(
            f"ytsearch{max_results}:{query}",
            download=False
        )

    return [entry["url"] for entry in result["entries"]]

if __name__ == "__main__":
    urls = search_videos("job interview")
    print(urls)
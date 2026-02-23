# main.py

from scripts.scrape_youtube import search_videos
from scripts.download_video import download_video
from scripts.extract_frames import extract_frames
from scripts.extract_audio import extract_audio
from scripts.analyze_faces import analyze_frames
from scripts.analyze_audio import analyze_audio
from scripts.fuse_behaviour import infer_behaviour
from scripts.detect_objects import detect_accessories
from scripts.infer_clothing import infer_clothing
from scripts.infer_activity import infer_activity
from scripts.generate_description import generate_description
from scripts.update_csv import append_to_csv

SEARCH_QUERY = "Indian Politics"
MAX_VIDEOS = 3

def run_pipeline():
    urls = search_videos(SEARCH_QUERY, MAX_VIDEOS)

    for url in urls:
        print(f"\nProcessing: {url}")

        # Download
        download_video(url, "data/raw_videos/%(id)s.%(ext)s")

        video_id = url.split("v=")[-1]

        # Paths
        video_path = f"data/raw_videos/{video_id}.mp4"
        frame_dir = f"data/processed_videos/{video_id}/frames"
        audio_path = f"data/processed_videos/{video_id}/audio.wav"

        # Processing
        extract_frames(video_path, frame_dir)
        extract_audio(video_path, audio_path)

        face = analyze_frames(frame_dir)
        audio = analyze_audio(audio_path)
        accessories, person_boxes = detect_accessories(frame_dir)
        clothing = infer_clothing("Unknown", face["gender"])
        activity = infer_activity(person_boxes)

        fused = infer_behaviour(face, audio, accessories, clothing, activity)

        
        description = generate_description(fused)

        record = {
            "Video ID": video_id,
            "Video method": "scraped",
            "Language": "Hindi/English",
            "Gender": face["gender"],
            "Age Group": face["age_group"],
            "Region": "Unknown",
            "Description": description
        }

        append_to_csv(record)
        print(description)

if __name__ == "__main__":
    run_pipeline()
# scripts/extract_audio.py

import subprocess
import os

def extract_audio(video_path, output_audio_path):
    os.makedirs(os.path.dirname(output_audio_path), exist_ok=True)

    command = [
        "ffmpeg",
        "-y",
        "-i", video_path,
        "-vn",
        "-ac", "1",
        "-ar", "16000",
        output_audio_path
    ]
    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    print(f"Audio extracted to {output_audio_path}")

if __name__ == "__main__":
    extract_audio(
        video_path="data/raw_videos/LuZV9kkzscg.mp4",
        output_audio_path="data/processed_videos/LuZV9kkzscg/audio.wav"
    )
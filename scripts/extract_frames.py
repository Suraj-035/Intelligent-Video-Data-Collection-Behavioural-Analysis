# scripts/extract_frames.py
import cv2
import os

def extract_frames(video_path, output_dir, fps_interval=1):
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps * fps_interval)

    frame_count = 0
    saved_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_count % frame_interval == 0:
            frame_name = f"frame_{saved_count}.jpg"
            cv2.imwrite(os.path.join(output_dir, frame_name), frame)
            saved_count += 1

        frame_count += 1

    cap.release()
    print(f"Extracted {saved_count} frames from {video_path}")

if __name__ == "__main__":
    extract_frames(
        video_path="data/raw_videos/gDN7cJ3Rt80.mp4",
        output_dir="data/processed_videos/gDN7cJ3Rt80/frames"
    )
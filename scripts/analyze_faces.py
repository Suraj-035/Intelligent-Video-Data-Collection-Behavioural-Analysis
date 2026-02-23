# scripts/analyze_faces.py

import os
from deepface import DeepFace
from collections import Counter

FRAME_DIR = "data/processed_videos/gDN7cJ3Rt80/frames"

def bucket_age(age):
    if age < 15:
        return "Below 15"
    elif age <= 25:
        return "15-25"
    elif age <= 35:
        return "26-35"
    elif age <= 45:
        return "36-45"
    elif age <= 55:
        return "46-55"
    else:
        return "55+"

def analyze_frames(frame_dir, max_frames=5):
    frames = sorted(os.listdir(frame_dir))[:max_frames]

    ages = []
    genders = []
    emotions = []

    for frame in frames:
        frame_path = os.path.join(frame_dir, frame)
        try:
            result = DeepFace.analyze(
                img_path=frame_path,
                actions=["age", "gender", "emotion"],
                enforce_detection=False
            )

            res = result[0]
            ages.append(res["age"])
            genders.append(res["dominant_gender"])
            emotions.append(res["dominant_emotion"])

        except Exception as e:
            print(f"Skipped {frame}: {e}")

    return {
        "age_group": bucket_age(int(sum(ages) / len(ages))) if ages else "Unknown",
        "gender": Counter(genders).most_common(1)[0][0] if genders else "Unknown",
        "emotion": Counter(emotions).most_common(1)[0][0] if emotions else "Neutral"
    }

if __name__ == "__main__":
    output = analyze_frames(FRAME_DIR)
    print(output)
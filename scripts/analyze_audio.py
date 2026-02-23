# scripts/analyze_audio.py

import librosa
import numpy as np

AUDIO_PATH = "data/processed_videos/LuZV9kkzscg/audio.wav"

def analyze_audio(audio_path):
    y, sr = librosa.load(audio_path, sr=None)

    # Loudness (RMS Energy)
    rms = librosa.feature.rms(y=y)[0]
    avg_rms = float(np.mean(rms))

    # Speech activity proxy
    zero_crossing_rate = np.mean(librosa.feature.zero_crossing_rate(y))

    # Heuristic rules
    speaking = avg_rms > 0.05
    shouting = avg_rms > 0.10

    return {
        "speaking": speaking,
        "shouting": shouting,
        "avg_rms": round(avg_rms, 4),
        "zero_crossing_rate": round(zero_crossing_rate, 4)
    }

if __name__ == "__main__":
    result = analyze_audio(AUDIO_PATH)
    print(result)
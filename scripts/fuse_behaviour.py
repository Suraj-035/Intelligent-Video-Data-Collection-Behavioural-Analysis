def infer_behaviour(face, audio, accessories, clothing, activity):
    if audio["speaking"] and audio["shouting"]:
        speech = "speaking loudly"
    elif audio["speaking"]:
        speech = "speaking calmly"
    else:
        speech = "silent"

    emotion_map = {
        "angry": "expressing anger",
        "sad": "appearing sad",
        "happy": "appearing happy",
        "neutral": "with a neutral expression",
    }

    return {
        "age_group": face["age_group"],
        "gender": face["gender"],
        "speech": speech,
        "emotion": emotion_map.get(face["emotion"], "with unclear emotion"),
        "clothing": clothing,
        "accessories": accessories,
        "activity": activity
    }
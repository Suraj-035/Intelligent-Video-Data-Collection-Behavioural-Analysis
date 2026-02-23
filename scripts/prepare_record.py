# scripts/prepare_record.py

def prepare_csv_record(
    video_id,
    method,
    language,
    region,
    face,
    audio,
    description
):
    return {
        "Video ID": video_id,
        "Video method": method,
        "Language": language,
        "Gender": face["gender"],
        "Age Group": face["age_group"],
        "Region": region,
        "Description": description
    }
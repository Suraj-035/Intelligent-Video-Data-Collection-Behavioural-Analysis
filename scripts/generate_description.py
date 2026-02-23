def generate_description(fused):
    
    activity_phrase = ""
    if fused.get("activity") and fused["activity"] != "activity unclear":
        activity_phrase = f"{fused['activity']}, "

    # Accessories phrase
    acc = ""
    if fused.get("accessories"):
        acc = " and wearing " + ", ".join(fused["accessories"])

    return (
        f"The video likely shows a {fused['age_group']} {fused['gender'].lower()} "
        f"{activity_phrase}"
        f"{fused['speech']}, {fused['emotion']}, "
        f"{fused['clothing']}{acc}."
    )
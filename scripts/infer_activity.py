# scripts/infer_activity.py

import numpy as np

def infer_activity(person_boxes):
    """
    person_boxes: list of (x1, y1, x2, y2) from multiple frames
    """

    if not person_boxes:
        return "activity unclear"

    heights = [(y2 - y1) for (_, y1, _, y2) in person_boxes]
    avg_height = np.mean(heights)

    
    if avg_height > 300:
        return "standing"
    elif avg_height > 150:
        return "sitting"
    else:
        return "posture unclear"
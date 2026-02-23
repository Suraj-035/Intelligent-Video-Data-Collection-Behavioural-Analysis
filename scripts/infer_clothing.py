# scripts/infer_clothing.py

def infer_clothing(region, gender):
    if region in ["North India", "South India", "East India", "West India"]:
        return "wearing casual or traditional attire"
    return "wearing casual clothing"
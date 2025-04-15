import json
import os

def load_captions(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    result = []
    for vid, meta in data.items():
        for (start, end), sentence in zip(meta['timestamps'], meta['sentences']):
            result.append({
                "video_id": vid,
                "duration": meta["duration"],
                "start": start,
                "end": end,
                "caption": sentence,
                "video_url": f"https://www.youtube.com/watch?v={vid[2:]}"
            })

    return result

# Example usage
if __name__ == "__main__":
    dataset = load_captions(r"C:\Users\nunoj\Desktop\MPWD\Project\VideoDialog\captions\train.json")
    print(f"Loaded {len(dataset)} captions.")
    print(dataset[0])

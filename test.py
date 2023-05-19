from easyturk import EasyTurk, interface


data = [{
                "id": 0,
                "task instruction": "aaa",
                "image": "https://cs.stanford.edu/people/rak248/VG_100K/1160052.jpg",
                "caption": "caption",
                "new_caption": "new caption",
                "modification": "what is modified from caption to new_caption",
                "question 1": "aaa",
                "question 2": "bbb",
                "question 3": "ccc"
        },
        {
                "id": 0,
                "task instruction": "task instruction",
                "image": "image url",
                "captions": ["caption 1", "caption 2", "caption 3", "caption 4", "caption 5"]
        },
        {
                "id": 1,
                "task instruction": "task instruction",
                "image": "image url",
                "captions": ["caption A", "caption B", "caption C", "caption D", "caption E"]
        }
]
# hit_ids = interface.launch_caption(data, reward=0, tasks_per_hit=3)
# print(hit_ids)
hit_ids = ["341YLJU22XSSV5B8EPI9BYVS4MV2I1"]

results = interface.fetch_completed_hits(hit_ids, approve=False)
print(results[hit_ids[0]])
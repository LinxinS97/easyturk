from easyturk import EasyTurk, interface


data = [{
        "id": 0,
        "task instruction": "task instruction",
        "image": "https://cs.stanford.edu/people/rak248/VG_100K/1160052.jpg",
        "captions": ["caption 1", "caption 2", "caption 3", "caption 4", "caption 5"]
}, {
        "id": 1,
        "task instruction": "task instruction",
        "image": "https://cs.stanford.edu/people/rak248/VG_100K/1160052.jpg",
        "captions": ["caption A", "caption B", "caption C", "caption D", "caption E"]
}]
# task_per_hit: how many data one worker can access.
hit_ids = interface.launch_task(data, template='human_eval.html', title='Human Evaluation', reward=0, tasks_per_hit=2)
print(hit_ids)

# Use the code below to fetch the complete hit.
# results = interface.fetch_completed_hits(hit_ids, approve=False)
# print(results[hit_ids[0]])
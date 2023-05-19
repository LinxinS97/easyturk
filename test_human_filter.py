from easyturk import EasyTurk, interface


data = [{
        "id": 0,
        "task instruction": "task instruction",
        "image": "https://cs.stanford.edu/people/rak248/VG_100K/1160052.jpg",
        "caption": "caption",
        "new_caption": "new_caption",
        "modifications": "what is modified from caption to new_caption",
        "question 1": "q1",
        "question 2": "q2",
        "question 3": "q3"
}, {
        "id": 1,
        "task instruction": "task instruction",
        "image": "https://cs.stanford.edu/people/rak248/VG_100K/1160052.jpg",
        "caption": "caption",
        "new_caption": "new_caption",
        "modifications": "what is modified from caption to new_caption",
        "question 1": "aaa",
        "question 2": "bbb",
        "question 3": "ccc"
}]
hit_ids = interface.launch_task(data, template='human_filter.html', title='Human Filter', reward=0, tasks_per_hit=2)
print(hit_ids)

# Use the code below to fetch the complete hit.
# results = interface.fetch_completed_hits(hit_ids, approve=False)
# print(results[hit_ids[0]])
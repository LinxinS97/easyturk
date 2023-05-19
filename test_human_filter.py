from easyturk import EasyTurk, interface
import json

question_map = {
    'type1': {
        'question 1': 'aaa',
        'question 2': 'bbb',
        'question 3': 'ccc'
    },
    'type2': {
        'question 1': 'aaa',
        'question 2': 'bbb',
        'question 3': 'ccc'
    },
    'type3': {
        'question 1': 'aaa',
        'question 2': 'bbb',
        'question 3': 'ccc'
    },
    'type4': {
        'question 1': 'aaa',
        'question 2': 'bbb',
        'question 3': 'ccc'
    },
    'type5': {
        'question 1': 'aaa',
        'question 2': 'bbb',
        'question 3': 'ccc'
    },
    'type6': {
        'question 1': 'aaa',
        'question 2': 'bbb',
        'question 3': 'ccc'
    },
    'type7': {
        'question 1': 'aaa',
        'question 2': 'bbb',
        'question 3': 'ccc'
    }
}


t_type = 'type1'
data = []

with open('dataset/chatgpt_swap_att_cos_filtered.jsonl', 'r', encoding='utf-8') as f:
    json_list = list(f)

for json_str in json_list:
    tmp = {
        **json.loads(json_str),
        **question_map[t_type]
    }
    tmp['filepath'] = f'https://clip-comp.s3.amazonaws.com/val2017/{tmp["filepath"].split("/")[-1]}'
    data.append(tmp)


hit_ids = interface.launch_task(data, template='human_filter.html', title='Human Filter Test 3', reward=0, tasks_per_hit=10)
print(hit_ids)

# Use the code below to fetch the complete hit.
# results = interface.fetch_completed_hits(hit_ids, approve=False)
# print(results[hit_ids[0]])
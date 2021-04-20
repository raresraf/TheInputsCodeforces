
import json

with open('dataset.json') as f:
  data = json.load(f)

dumps = {}
for entry in data:
	if entry["source"] == "codeforces":
		if entry['tags'] == []:
			continue
		print(f"index: {entry['index']}; tags {entry['tags']}")
		dumps[entry['index']] = entry['tags']

with open('metadata.json', 'w', encoding='utf-8') as json_file:
  json.dump(dumps, json_file, ensure_ascii=False, indent=4, sort_keys=True)
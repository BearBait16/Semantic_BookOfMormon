import json

x = 0
json_data = []
with open ("Book_of_Mormon.txt") as file:
    content = file.read()
    verses_split_file = content.split('\n\n')

for verses in verses_split_file:
    lines = verses.split('\n', 1)
    title = lines[0].strip()
    text = lines[1].strip()
    data = {
        "Title": title,
        "Text": text
    }
    json_data.append(data)
    print(title)
    x += 1

with open('BomJson.json', 'w') as file:
    json.dump(json_data, file)

print(f"There are {x} verses")
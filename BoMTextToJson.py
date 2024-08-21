x = 0

with open ("Book_of_Mormon.txt") as file:
    content = file.read()
    verses_split_file = content.split('\n\n')
    for verses in verses_split_file:
        x += 1

print(f"There are {x} verses in the Book of Mormon")


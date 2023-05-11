import json

def main():
    file_pointer = open("ch06/exercises/news.txt", "r")
    file_data = file_pointer.read()
    file_pointer.close()
    
    fptr = open("ch06/exercises/subs.json", "r")
    file2_data = json.load(fptr)
    for k, v in file2_data.items():
        file_data = file_data.replace(k, v)
        print(k, v)
    file3 = open("ch06/exercises/betternews.txt", "w")
    file3.write(file_data)
    file3.close()

main()


file1 = "a.txt"
file2 = "b.txt"
file3 = "c.txt"
merge_file = "merged_file.txt"

def read_file(file_name):
    with open(file_name, "r") as file:
        data = file.read()
    return data


data1 = read_file(file1)
data2 = read_file(file2)
data3 = read_file(file3)

def write_file(*arguments):
    
    for i in arguments:
        with open(merge_file, "a") as file:
            file.write(i +"\n")

    return merge_file


data = write_file(data1, data2, data3)


def countVal(strings):
    counter = 0
    for string in strings:
        if string.endswith('?'):
            counter += 1
    return counter


if __name__ == "__main__":
    arr = ["56??","???","5?1"]
    result = countVal(arr)
    print(result)
    

print("self Logic Question")
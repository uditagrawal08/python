def add(arr):
    return arr[0] if len(arr)==1 else arr[0]+add(arr[1:])
print([int(input(f"Enter value no. {i+1} :::")) for i in range(int(input("How many numbers you want, Sir ...:")))])
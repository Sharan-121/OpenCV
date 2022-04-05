arr = [1, 1, 1, 1, 2]
max = arr[0]
sec_max = arr[0]

for i in range(1, len(arr)):
    if arr[i] > max:
        sec_max = max
        max = arr[i]
    elif arr[i] < max and arr[i] > sec_max:
        sec_max = arr[i]

print(max)
print(sec_max)

"""
Program: Rotate List
Description: Rotate list right and left by k positions.
"""

k = int(input("Enter k (number of rotations): "))

lst = [1, 2, 3, 4, 5, 6, 7]
k = k % len(lst)

rotated_list = lst[-k:] + lst[:-k]
print(f"right shift: {rotated_list}")


rotated_list = lst[k:] + lst[:k]
print(f"left shift: {rotated_list}")

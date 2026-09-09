my_list = [(1,2),(3,1),(2,4)]
sorted_list = sorted(my_list, key=lambda x:x[1])
print("第二要素に基づいて昇順にソートされたリスト",sorted_list)

def sift_down(arr, n, i):
    """
    下滤操作：确保以 i 为根的子树满足大顶堆属性 [cite: 10]
    """
    largest = i
    left = 2 * i + 1   # 左孩子下标
    right = 2 * i + 2  # 右孩子下标

    # 检查左孩子是否大于当前最大值
    if left < n and arr[left] > arr[largest]:
        largest = left
    # 检查右孩子是否大于当前最大值
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 如果最大值不是根节点，则进行交换
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # 递归下滤，确保被换下去的节点在新的位置也满足堆属性
        sift_down(arr, n, largest)

def build_heap(arr):
    """
    自底向上构建大顶堆 [cite: 5, 10]
    """
    n = len(arr)
    # 最后一个非叶子节点的下标计算：n // 2 - 1 [cite: 10]
    start_index = n // 2 - 1
    
    print(f"原始数组: {arr}")
    print(f"从下标 {start_index} 开始自底向上构建堆...\n")
    
    for i in range(start_index, -1, -1):
        sift_down(arr, n, i)
        print(f"对下标 {i} (元素 {arr[i]}) 执行下滤后的数组: {arr}")

# 运行示例
example_arr = [1, 9, 6, 8, 5]
build_heap(example_arr)
print(f"\n最终建堆结果: {example_arr}")
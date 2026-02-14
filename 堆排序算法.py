def sift_down(arr, n, i):
    """
    下滤操作：维护大顶堆属性
    :param arr: 存储堆的数组
    :param n: 堆的当前大小
    :param i: 当前需要下滤的节点下标
    """
    largest = i          # 初始化最大值为当前节点
    left = 2 * i + 1     # 左孩子下标
    right = 2 * i + 2    # 右孩子下标

    # 如果左孩子存在且大于根节点
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 如果右孩子存在且大于当前最大的节点
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 如果最大值不是当前节点，则交换并继续递归下滤
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        sift_down(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # 1. 建堆 (BuildHeap): 从最后一个非叶子节点开始向上调整 
    # 最后一个非叶子节点下标为 n // 2 - 1
    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, n, i)

    # 2. 排序 (Sorting): 依次取出堆顶元素放到数组末尾，并重新调整堆
    for i in range(n - 1, 0, -1):
        # 将当前最大的堆顶 arr[0] 交换到末尾 arr[i]
        arr[i], arr[0] = arr[0], arr[i]
        # 调整剩余部分，使其重新满足堆属性
        sift_down(arr, i, 0)

# 测试代码
if __name__ == "__main__":
    test_arr = [1, 9, 6, 8, 5]  # 使用第4题的序列进行验证 [cite: 8]
    heap_sort(test_arr)
    print("排序后的数组:", test_arr)
def largest_sum_10_percent(a: list[int]) -> int:
    n = len(a)
    window_size = n // 10
    max_sum = float('-inf')
    max_sum_window = []
    
    for i in range(n - window_size + 1):
        window_sum = sum(a[i:i+window_size])
        if window_sum > max_sum:
            max_sum = window_sum
            max_sum_window = a[i:i+window_size]
            
    print(max_sum)
    print(max_sum_window)
    return max_sum
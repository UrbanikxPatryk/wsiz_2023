def best_multiply(a: list[int]) -> int:
    n = len(a)
    max_product = float('-inf')
    
    for i in range(n):
        for j in range(i+1, n):
            product = a[i] * a[j]
            if product > max_product:
                max_product = product
                
    return max_product
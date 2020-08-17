def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    hash_table = {}
    result = []
    for n in a:
        hash_table[n] = n

    for n in a:
        if n < 0:
            if abs(n) in hash_table:
                result.append(abs(n))
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
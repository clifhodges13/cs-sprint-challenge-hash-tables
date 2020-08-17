def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    weight_table = {}

    i = 0
    for w in weights:
        weight_table[w] = {
            "value": w,
            "diff": (limit - w)
        }
        i += 1
    
    j = 0
    while j < length:
        cur_wt = weights[j]
        if weight_table[cur_wt]["diff"] in weights:
            diff = 0
            if cur_wt == weight_table[cur_wt]["diff"]:
                diff = weights.index(weight_table[cur_wt]["diff"])+1
            else:
                diff = weights.index(weight_table[cur_wt]["diff"])
            wts = sorted([j, diff], reverse=True)
            return tuple(wts)
        j += 1

    return None

def delete_nth(order, num):
    result = []
    occurrences = {}
    for n in order:
        count = occurrences.setdefault(n, 0)
        if count >= num:
            continue
        result.append(n)
        occurrences[n] += 1
    return result

print(delete_nth([1,2,3,3,4,2,1,7], 1))

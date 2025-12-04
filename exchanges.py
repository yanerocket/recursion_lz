def permutations(elements):
    if len(elements) <= 1:
        return [elements]
    
    result = []
    
    for i in range(len(elements)):
        current = elements[i]
        remaining = elements[:i] + elements[i+1:] # cрез списка для получения нужного элемента
        for p in permutations(remaining):
            result.append([current] + p)
    return result

print(permutations([1, 2, 3]))
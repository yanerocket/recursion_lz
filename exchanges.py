def permutations(elements):
    if len(elements) <= 1:
        return [elements]
    
    result = []
    
    for i in range(len(elements)):
        current = elements[i]
        remaining = elements[:i] + elements[i+1:] 
        for p in permutations(remaining):
            result.append([current] + p)
    return result

def main():
    print(permutations([1, 2, 3]))

if __name__ == '__main__':
    main()


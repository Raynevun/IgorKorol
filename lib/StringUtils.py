import collections

def calculate_char_sequence(value):
    results = collections.defaultdict(int)
    for c in value:
        results[c] += 1
    return  results

def print_collection(value):
    print("Char sequence in beacon value :\n")
    for k in value.keys():
        print(k, ',', value[k])
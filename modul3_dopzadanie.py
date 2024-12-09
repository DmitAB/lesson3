


def calculate_structure_sum(data_structure, numbers1 = [], letters1 = []):
    #print(f"{data_structure=}")
    #if numbers1 is None:
    #numbers1 = []
    #if letters1 is None:
    #letters1 = []
    for i1 in range(len(data_structure)):
        if isinstance(data_structure[i1], int):
            if data_structure[i1] == 0:
                continue
            numbers1.append(data_structure[i1])
            data_structure[i1] = 0
            continue

        if isinstance(data_structure[i1], str):
            letters1.append(data_structure[i1])
            data_structure[i1] = 0
            continue
        if isinstance(data_structure[i1], dict) == True:
            data_structure.append(list(data_structure[i1].values()))
            data_structure.append(list(data_structure[i1].keys()))
            data_structure[i1] = 0
            continue
        def data_structure2(*args):
            for i1 in range(len(data_structure)):
                if isinstance(data_structure[i1], int):
                    if data_structure[i1] == 0:
                        continue
                    numbers1.append(data_structure[i1])
                    data_structure[i1] = 0
                    continue
                if isinstance(data_structure[i1], str):
                    letters1.append(data_structure[i1])
                    data_structure[i1] = 0
                    continue
                if isinstance(data_structure[i1], dict) == True:
                    data_structure.append(list(data_structure[i1].values()))
                    data_structure.append(list(data_structure[i1].keys()))
                    data_structure[i1] = 0
                    continue
                for i2 in data_structure[i1]:
                    data_structure.append(i2)
                    continue
                data_structure[i1] = 0
                continue
            if any(data_structure):
                return data_structure2(data_structure)
            else:
                return calculate_structure_sum(data_structure, numbers1 = [], letters1 = [])
        data_structure2(data_structure)
    sum1 = 0
    sum2 = 0
    for j in numbers1:
        sum1 = sum1 + j
        continue
    for k in letters1:
        sum2 = sum2 + len(k)
        continue
    sum_ = sum1 + sum2
    return  sum_


data_structure = [[1, 2, 3],{'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)

result = calculate_structure_sum(data_structure)
print(result)

result = calculate_structure_sum(data_structure)
print(result)
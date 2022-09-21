if __name__ == '__main__':
    
    records = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    
    def take_score(record):
        return record[1]

    records.sort(key=take_score)
    second_lowest_score = records[1][1]
    
    second_lowest_names = []
    for name, score in records:
        if score == second_lowest_score:
            second_lowest_names.append(name)
    
    print()
    print(f"The second lowest grade of {second_lowest_score} belong to:")
    for name in sorted(second_lowest_names):
        print(name)
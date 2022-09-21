if __name__ == '__main__':
    
    records = []
    scores = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        scores.append(score)

    unique_scores = list(set(scores))
    second_lowest_score = sorted(unique_scores)[1]

    second_lowest_names = []
    for name, score in records:
        if score == second_lowest_score:
            second_lowest_names.append(name)
    
    print()
    print(f"The second lowest grade of {second_lowest_score} belong to:")
    for name in sorted(second_lowest_names):
        print(name)
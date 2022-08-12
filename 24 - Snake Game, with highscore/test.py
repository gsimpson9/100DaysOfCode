with open('high_score.txt') as f:
    score = f.readline()
    print(score)


with open('high_score.txt', 'w') as f:
    score = f.write("1")
    print(score)
import numpy as np
import random

currentPos = [2, 0]
coinPos = [0, 0]
coinExist = [False]
score = [0]
scoreMultiple = [1]
score_multiple_price = [20]
expand_price = [20]
current_matrix_size = [3]
shopAvaliable = [f'-score_multiple {score_multiple_price[0]} score\n-expand {expand_price[0]}\n-q = quit']


matrix = np.full((3, 3), ' ', str)
matrix[currentPos[0]][currentPos[1]] = 'P'

print(matrix)

def putCoin():
    if coinExist[0] == True:
        matrix[coinPos[0]][coinPos[1]] = 'A'
        return
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        coinPos[0] = x
        coinPos[1] = y
        if coinPos == currentPos:
            continue
        matrix[x][y] = 'A'
        break

    coinExist[0] = True
    
def checkScore():
    if currentPos == coinPos:
        score[0] += scoreMultiple[0]
        coinExist[0] = False

while True:
    query = input()
    query = query.lower()
    if query == 'w':
        matrix[currentPos[0]][currentPos[1]] = ' '
        if currentPos[0] == 0:
            currentPos[0] = len(matrix[0]) - 1

        else:
            currentPos[0] -= 1
        matrix[currentPos[0]][currentPos[1]] = 'P'
        checkScore()
        putCoin()
        print('score = '+str(score[0]))
        print(matrix)
    
    elif query == 'd':
        matrix[currentPos[0]][currentPos[1]] = ' '
        if currentPos[1] == len(matrix[0]) - 1:
            currentPos[1] = 0

        else:
            currentPos[1] += 1

        matrix[currentPos[0]][currentPos[1]] = 'P'
        checkScore()
        putCoin()
        print('score = '+str(score[0]))
        print(matrix)

    elif query == 'a':
        matrix[currentPos[0]][currentPos[1]] = ' '
        if currentPos[1] == 0:
            currentPos[1] = len(matrix[0]) - 1

        else:
            currentPos[1] -= 1

        matrix[currentPos[0]][currentPos[1]] = 'P'
        checkScore()
        putCoin()
        print('score = '+str(score[0]))
        print(matrix)

    elif query == 's':
        matrix[currentPos[0]][currentPos[1]] = ' '
        if currentPos[0] == len(matrix) - 1:
            currentPos[0] = 0

        else:
            currentPos[0] += 1

        matrix[currentPos[0]][currentPos[1]] = 'P'
        checkScore()
        putCoin()
        print('score = '+str(score[0]))
        print(matrix)

    elif query == 'shop':
        print(shopAvaliable[0])
        shopQuery = input('buy = ')
        shopQuery = shopQuery.lower()
        if shopQuery == 'scoremultiple':
            if score >= score_multiple_price:
                scoreMultiple[0] += 1
                score_multiple_price[0] = score_multiple_price[0] * 2
                continue
            else:
                print(f'score kamu tidak cukup\nscore = {score}')

        elif shopQuery == 'expand':
            if score >= expand_price:
                current_matrix_size[0] += 1
                coordinate = current_matrix_size[0]
                matrix = np.full((coordinate, coordinate), ' ', str)
                putCoin()
                expand_price[0] = expand_price * 2

    elif query == 'q':
        break



print('done.')

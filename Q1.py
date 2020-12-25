# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
import numpy as np

# You may change this function parameters
def findMaxProfit(numOfPredictedDay, predictedSharePrices):
    # Participants code will be here
    n = numOfPredictedDay 
    memo = np.empty(shape=(n, n), dtype=int)
    # print(memo)

    for i in range(n):
        for j in range(n):
            if i <= j:
                memo[i][j] = predictedSharePrices[j] - predictedSharePrices[i]
            else:
                memo[i][j] = 0
              
    m, h = np.unravel_index(np.argmax(memo, axis=None), memo.shape)
    
    ret = predictedSharePrices[h] - predictedSharePrices[m]

    return ret


def main():
    line = input().split()
    numOfPredictedDay = int(line[0])
    predictedSharePrices = list(map(int, line[1:]))

    answer = findMaxProfit(numOfPredictedDay, predictedSharePrices)

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main()


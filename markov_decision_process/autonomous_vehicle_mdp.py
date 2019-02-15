import numpy as np
from copy import deepcopy


def transpose(A):
    n = len(A)
    B = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(n):
            B[i][j] = A[j][i]
    return B


def getMaxExpectedUtility2(r, c, U):
    pr = 0
    nRow, nCol = getNorth(r,c)
    sRow, sCol = getSouth(r,c)
    eRow, eCol = getEast(r,c)
    wRow, wCol = getWest(r,c)

    p1 = np.float64(0.7 * U[nRow][nCol] + 0.1 * U[sRow][sCol] + 0.1 * U[eRow][eCol] + 0.1 * U[wRow][wCol])
    p2 = np.float64(0.1 * U[nRow][nCol] + 0.7 * U[sRow][sCol] + 0.1 * U[eRow][eCol] + 0.1 * U[wRow][wCol])
    p3 = np.float64(0.1 * U[nRow][nCol] + 0.1 * U[sRow][sCol] + 0.7 * U[eRow][eCol] + 0.1 * U[wRow][wCol])
    p4 = np.float64(0.1 * U[nRow][nCol] + 0.1 * U[sRow][sCol] + 0.1 * U[eRow][eCol] + 0.7 * U[wRow][wCol])

    MEU = max(p1, p2, p3, p4)
    return MEU


def getNorth(r, c):
    if r-1 < 0:
        return r, c
    else:
        return r-1, c


def getSouth(r, c):
    if r+1 > grid-1:
        return r,c
    else:
        return r+1,c

def getEast(r,c):
    if c+1 > grid-1:
        return r,c
    else:
        return r,c+1

def getWest(r,c):
    if c-1 < 0:
        return r,c
    else:
        return r,c-1


def formPolicy(Utility, xend, yend):
    maxDir = 0
    policyval = [[0 for x in range(grid)] for y in range(grid)]
    for i in range(grid):
        for j in range(grid):
            if i == xend and j == yend:
                continue
            r,c = getNorth(i,j)
            up = Utility[r][c]

            r,c = getSouth(i,j)
            down = Utility[r][c]

            r,c = getEast(i,j)
            right = Utility[r][c]

            r,c = getWest(i,j)
            left = Utility[r][c]

            max_val = max(up, down, left, right)
            if max_val == up:
                maxDir = "up"
            elif max_val == down:
                maxDir = "down"
            elif max_val == left:
                maxDir = "left"
            elif max_val == right:
                maxDir = "right"
            policyval[i][j] = maxDir
    return policyval

def printUtility(Utility):
    for i in Utility:
        print i

def moveUp(r,c):
    if r-1 < 0:
        return 0,c
    else:
        return r-1,c

def moveDown(r,c):
    if r+1 > grid-1:
        return grid-1,c
    else:
        return r+1,c

def moveRight(r,c):
    if c+1 > grid-1:
        return r,grid-1
    else:
        return r,c+1

def moveLeft(r,c):
    if c-1 < 0:
        return r,0
    else:
        return r,c-1

def callActionfunc(dir,r,c):
    if dir == "left":
        r,c = moveLeft(r,c)
    if dir == "up":
        r,c = moveUp(r,c)
    if dir == "down":
        r,c = moveDown(r,c)
    if dir == "right":
        r,c = moveRight(r,c)
    return r,c

def turn_left(r,c, face):
    transitMap = {
        "up":"left",
        "left":"down",
        "down":"right",
        "right":"up"
    }
    dir = transitMap[face]
    face = dir
    r,c = callActionfunc(dir,r,c)
    return r,c,face

def turn_right(r,c,face):
    transitMap = {
        "up":"right",
        "right":"down",
        "down":"left",
        "left":"up"
    }
    dir = transitMap[face]
    face = dir
    r,c = callActionfunc(dir,r,c)
    return r,c,face

def turn_opposite(r,c,face):
    transitMap = {
        "up":"down",
        "down":"up",
        "left":"right",
        "right":"left"
    }
    dir = transitMap[face]
    face = dir
    r,c = callActionfunc(dir,r,c)
    return r,c,face

def simulate(Ro,Co,Rn, Cn, policy):
    ans = []
    for j in range(10):

        np.random.seed(j)
        swerve = np.random.random_sample(1000000)
        k = 0
        r,c = Ro, Co
        face = "up"
        cost = 0

        while(True) :
            if (r == Rn)and (c == Cn):
                break

            nextDir = policy[r][c]
            face = nextDir
            if swerve[k] > 0.7:
                if swerve[k] > 0.8:
                    if swerve[k] > 0.9:
                        r, c, face = turn_opposite(r, c, face)
                        cost += Reward[r][c]
                        # print r, ",", c, " Facing1",face, "swerve ",swerve[k]
                    else:
                        r, c, face = turn_right(r, c, face)
                        cost += Reward[r][c]
                        # print r, ",", c, " Facing2", face, "swerve ",swerve[k]
                else:
                    r, c, face = turn_left(r,c,face)
                    cost += Reward[r][c]
                    # print r, ",", c, " Facing3", face, "swerve ",swerve[k]
            else:
                r, c = callActionfunc(nextDir, r, c)
                face = nextDir
                cost += Reward[r][c]
                # print r, ",", c, " Facing4", face, "swerve :", swerve[k]
            k += 1
        ans.append(cost)
    # print sum(ans)/10
    return np.float64(np.floor(sum(ans)/10))

def printMatrix(matrix):
    for i in matrix:
        print i

if __name__ == '__main__':
    Policy = []
    input = open("grading_case_hw3\grading_case\input56.txt", 'r')
    output = open("output50.txt", 'w')
    grid = int(input.readline().strip())
    nCars = int(input.readline().strip())
    nObstacles = int(input.readline().strip())
    obstacleLocation = []
    obstacleCoords = [[0 for x in range(grid)] for y in range(grid)]
    for i in range(nObstacles):
        tempTuple = input.readline().strip().split(",")
        tempTuple[0] = int(tempTuple[0])
        tempTuple[1] = int(tempTuple[1])
        obstacleLocation.append(tempTuple)  # col, row

    startLocation = []
    for col in range(nCars):
        tempTuple = input.readline().strip().split(",")
        tempTuple[0] = int(tempTuple[0])
        tempTuple[1] = int(tempTuple[1])
        startLocation.append(tempTuple)  # col, row

    terminalLocation = []
    for col in range(nCars):
        tempTuple = input.readline().strip().split(",")
        tempTuple[0] = int(tempTuple[0])
        tempTuple[1] = int(tempTuple[1])
        terminalLocation.append(tempTuple)  # col, row

    for car in range(nCars):

        Utility = [[0.0 for x in range(grid)] for y in range(grid)]
        Reward = [[-1.0 for x in range(grid)] for y in range(grid)]
        xEnd, yEnd = terminalLocation[car]      # col, row

        # mark utilities and rewards for obstacles
        for o in obstacleLocation:
            Reward[o[0]][o[1]] = -101

        Reward[xEnd][yEnd] = 99

        Utility = np.transpose(Utility)
        Reward = np.transpose(Reward)

        #swap xEnd and yEnd
        xEnd, yEnd = yEnd, xEnd

        d = 0
        e = 0.1
        gamma = 0.9
        while True:
            d = 0
            Utility1 = deepcopy(Utility)
            for i in range(grid):
                for j in range(grid):
                    if i == xEnd and j == yEnd:
                        Utility[i][j] = Reward[i][j]
                        continue
                    Utility[i][j] = Reward[i][j] + gamma * getMaxExpectedUtility2(i,j,Utility)

                    if abs(Utility1[i][j] - Utility[i][j]) > d:
                        d = abs(Utility1[i][j] - Utility[i][j])

            if d <= e*(1-gamma)/gamma:
                break
        # print Utility
        p = formPolicy(Utility, xEnd, yEnd)
        Policy.append(p)
        # print Policy[car]
        # printMatrix(Policy[car])
        val = simulate(startLocation[car][1],startLocation[car][0],xEnd,yEnd,Policy[car])
        # print "Answer : ", val
        output.write(str(int(val)) + "\n")
    input.close()
    output.close()



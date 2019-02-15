Implementing an approach to tackle partially observable(probabilistic) environment using Markov Decision process

# Task Description
The idea is to implement a decision process considering the situation of an autonomous vehicle. Given a city map in the form grid/matrix, the car navigates through the city using the path with maximum profit. The maximum profit could be the destination in real time scenario. 
The situation adds constraints by including obstacles such buildings and road crossings that reduce the profit. For every obstacle the car hits, the profit reduces by 100 points and for every unit of distance covered, the car spends 1 point. 
The situation is partial observable since the car could go in the correct direction on 70% of the time with 10% change of going in the wrong direction. The directions north, south, east and west. 

The code consists of two parts:
1. Determining the path of maximum utility.
2. Simulating the moves of a car by 10 random seeds. 
The output is average profit earned in simulation for each car. 

# Input 
The file input.txt in the current directory of your program will be formatted
as follows:
First line: strictly positive 32-bit integer s, size of grid [grid is a square of size sxs]
Second line: strictly positive 32-bit integer n, number of cars
Third line: strictly positive 32-bit integer o, number of obstacles
Next o lines: 32-bit integer x, 32-bit integer y, denoting the location of obstacles
Next n lines: 32-bit integer x, 32-bit integer y, denoting the start location of each
car
Next n lines: 32-bit integer x, 32-bit integer y, denoting the terminal location of
each car

# Output 

n lines: 32-bit integer, denoting the mean money earned in simulation for each
car, integer result of floor operation

# Example

input.txt
3
1
1
0,1
2,0
0,0

Output.txt
95

For example, say you have a 3x3 grid, as follows, with 1 car in start position 1,0
(green):
![alt text](https://github.com/chethanabhaskara/aritficial_intelligence/blob/master/markov_decision_process/city_grid.png)

You determine that based on the locations of certain obstacles and people, you
should move in these directions in each cell:
![alt text](https://github.com/chethanabhaskara/aritficial_intelligence/blob/master/markov_decision_process/max_utility_path.png)



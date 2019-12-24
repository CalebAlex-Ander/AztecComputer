'''====================================
Advent of Code Day III
Pt 1 Completed on 
Crossed Wires
====================================='''

def main():
    '''wire1 = "R75, D30, R83, U83, L12, D49, R71, U7, L72"
    wire2 = "U62, R66, U55, R34, D71, R55, D58, R83"'''
    fileInput = open("Day3.txt")
    fileInput = fileInput.read()
    wire1, wire2 = fileInput.split("\n")
    wire1 = wire1.split(",")
    wire2 = wire2.split(",")
    '''wire1 = wire1.split()
    for i in range(len(wire1)):
        wire1[i] = wire1[i].strip(',')

    wire2 = wire2.split()
    for i in range(len(wire2)):
        wire2[i] = wire2[i].strip(',')'''
    grid1 = coordinateGrid(wire1)
    grid2 = coordinateGrid(wire2)
    intersections = []
    for i1 in grid1:
        for i2 in grid2:
            if i1 == i2:
                intersections.append(i2)
    print(intersections)
    distances = []
    for intersection in intersections:
        distances.append(abs(intersection[0])+abs(intersection[1]))
    smallestDistance = min(distances[1:])
    print(smallestDistance)

                         
        
def coordinateGrid(instructions):
    wirexy = [(0,0)]
    #This puts the wire's corners' coordinates in wirexy as tuples.
    for i in range(len(instructions)):
        if instructions[i][0] == 'R':
            for i2 in range(int(instructions[i][1:])):
                wirexy.append((wirexy[-1][0]+1, wirexy[-1][-1]))
            #wirexy.append((wirexy[-1][0]+int(wire1[i][1:]), wirexy[-1][-1]))
        if instructions[i][0] == 'L':
            for i2 in range(int(instructions[i][1:])):
                wirexy.append((wirexy[-1][0]-1, wirexy[-1][-1]))
            #wirexy.append((wirexy[-1][0]-int(wire1[i][1:]), wirexy[-1][-1]))
        if instructions[i][0] == 'D':
            for i2 in range(int(instructions[i][1:])):
                wirexy.append((wirexy[-1][0], wirexy[-1][1]-1))
            #wirexy.append((wirexy[-1][0], wirexy[-1][1]-int(wire1[i][1:])))
        if instructions[i][0] == 'U':
            for i2 in range(int(instructions[i][1:])):
                wirexy.append((wirexy[-1][0], wirexy[-1][1]+1))
            #wirexy.append((wirexy[-1][0], wirexy[-1][1]-int(wire1[i][1:])))
    return wirexy
main()




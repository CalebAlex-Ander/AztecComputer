'''====================================
Advent of Code Day III
Pt 1 Completed on 12/23/19
Crossed Wires
====================================='''

def main():
    fileInput = open("Day3.txt")
    fileInput = fileInput.read()
    wire1, wire2 = fileInput.split("\n")
    wire1 = wire1.split(",")
    wire2 = wire2.split(",")
    
    grid1 = coordinateGrid(wire1)
    print("Gridded wire1. Gridding wire2...")
    grid2 = coordinateGrid(wire2)
    print("Gridded wire2. Finding Intersections...")

    intersections = findIntersections(grid1, grid2)
    print("Intersections found. Finding distances for each...")
    
    distances = []
    for intersection in intersections:
        distances.append(abs(intersection[0])+abs(intersection[1]))
    print("Distances found. Finding shortest...")
    
    smallestDistance = min(distances[1:])
    print(smallestDistance)

                         
        
def coordinateGrid(instructions):
    wirexy = [(0,0)]
    for i in range(len(instructions)):
        if instructions[i][0] == 'R':
            for i2 in range(int(instructions[i][1:])):
                wirexy.append((wirexy[-1][0]+1, wirexy[-1][-1]))
        if instructions[i][0] == 'L':
            for i2 in range(int(instructions[i][1:])):
                wirexy.append((wirexy[-1][0]-1, wirexy[-1][-1]))
        if instructions[i][0] == 'D':
            for i2 in range(int(instructions[i][1:])):
                wirexy.append((wirexy[-1][0], wirexy[-1][1]-1))
        if instructions[i][0] == 'U':
            for i2 in range(int(instructions[i][1:])):
                wirexy.append((wirexy[-1][0], wirexy[-1][1]+1))
    return wirexy

def findIntersections(wire1, wire2):
    intersections = []
    for i1 in wire1:
        for i2 in wire2:
            if i1 == i2:
                intersections.append(i2)
    return intersections
main()




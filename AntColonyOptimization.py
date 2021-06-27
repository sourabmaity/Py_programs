'''import copy

import cv2
import numpy as np
import pyautogui

points = []
cities_distance = []
pheromone=[]
def iteration2():

def iteration1():
    global cities_distance
    global pheromone
    for i in range(len(points)):
        n=[2 for i in range(len(points))]
        now=i
        total_dis = 0
        for j in range(len(points)-1):
            temp=[]
            n[now]=1
            ind = [i for i in range(len(n)) if n[i] == 2]
            print(ind)
            for k in ind:
                temp.append(cities_distance[now][k])
            #temp=copy.deepcopy(cities_distance[j])
            #temp.remove(0)
            temp=min(temp)
            total_dis+=temp
            n[now]=0
            now=cities_distance[now].index(temp)
            n[now]=1
        print(total_dis)


def set_cities_distance():
    global cities_distance
    global pheromone
    row_column = len(points)
    cities_distance = [[0 for i in range(row_column)] for j in range(row_column)]
    #pheromone = [[1 for i in range(row_column)] for j in range(row_column)]
    for i in range(row_column):
        temp = []
        for j in range(row_column):
            if i==j:
                temp.append(0)
            else:
                temp.append(0.5)
        pheromone.append(temp)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            cities_distance[i][j] = distance(points[i], points[j])
            cities_distance[j][i] = cities_distance[i][j]
    for row in cities_distance:
        print(row)


def distance(p1, p2):
    return int(np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2))


def draw_lines(new):
    print("len:", len(points))
    for i in points:
        cv2.line(img, new, i, [0, 150, 0], 1)
    points.append(new)
    set_cities_distance()


def click_res(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        # points.append((x,y))
        cv2.circle(img, (x, y), 2, [0, 0, 255], 2)
        draw_lines((x, y))
        cv2.imshow('ACO', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        print("Right click")
        iteration1()

img = np.zeros([512, 512, 3], dtype=np.uint8)
img.fill(255)
cv2.imshow('ACO', img)
cv2.setMouseCallback('ACO', click_res)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''import pants
import math
import random

nodes=[]
for _ in range(20):
  x=random.uniform(-10,10)
  y=random.uniform(-10,10)
  nodes.append((x,y))
#print("", nodes)
def euclidean(a,b):
  return math.sqrt(pow(a[1]-b[1],2)+pow(a[0]-b[0],2))

world=pants.World(nodes,euclidean)

solver=pants.Solver(rho=0.5,q=1,t0=0.01,limit=50,ant_count=10)

solution=solver.solve(world)
print(solution.distance)
print(solution.tour)

solutions=solver.solutions(world)
best=float("inf")
for solution in solutions:

    print(solution.distance)
    if solution.distance<best:
        best=solution.distance
        c=solution
print(best)
print(c.tour)'''

import cv2
import numpy as np
import pyautogui
import pants
import math
import random

points = []
nodes=[]

def distance(p1, p2):
    return int(np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2))

def draw_lines(new):
    #print("len:", len(points))
    for i in points:
        cv2.line(img, new, i, [0, 150, 0],1)
    points.append(new)
    #set_cities_distance()
def click_res(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        #print(x, y)
        points.append((x,y))
        nodes.append((x, y))
        cv2.circle(img, (x, y), 2, [0, 0, 255], 2)
        draw_lines((x, y))
        cv2.imshow('ACO', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        print("Right click")
        world = pants.World(nodes, distance)
        solver = pants.Solver(rho=0.5, q=1, t0=0.01, limit=50, ant_count=10)
        solutions = solver.solutions(world)
        best = float("inf")
        for solution in solutions:
            print(solution.distance)
            if solution.distance < best:
                best = solution.distance
                c = solution
        print(best)
        print(c.tour)
        c=c.tour
        for i in range(len(c)-1):
            cv2.line(img, c[i], c[i+1], [150, 0, 0], 3)
        cv2.line(img, c[0], c[len(c)-1], [150, 0, 0], 3)
        cv2.imshow('ACO', img)
        #iteration1()

img = np.zeros([512, 512, 3], dtype=np.uint8)
img.fill(255)
cv2.imshow('ACO', img)
cv2.setMouseCallback('ACO', click_res)

cv2.waitKey(0)
cv2.destroyAllWindows()
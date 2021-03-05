# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
import numpy as np
import random
from src.rrt.rrt_star import RRTStar
from src.search_space.search_space import SearchSpace
from src.utilities.plotting import Plot

X_dimensions = np.array([(0, 300), (0, 300), (0, 300)])  # dimensions of Search Space
# obstacles

num_of_obs=random.randint(500,600)
print(num_of_obs)
Obstacles_list=[]
for _ in range (num_of_obs):
    i=random.randint(0,300)
    j=random.randint(-80,80)
    k=random.randint(-80,80)
    point=(i,i-j,i-k,i+10,i-j+10,i-k+10)
    Obstacles_list.append(point)
Obstacles=np.array(Obstacles_list)
#Obstacles = np.array(
 #   [(20, 20, 20, 40, 40, 40),(20, 20, 60, 40, 40, 80), (20, 60, 20, 40, 80, 40), (60, 60, 20, 80, 80, 40),
  #   (60, 20, 20, 80, 40, 40), (60, 20, 60, 80, 40, 80), (20, 60, 60, 40, 80, 80), (60, 60, 60, 80, 80, 80),(90,90,90,95,95,95)])
x_init = (0, 0, 0)  # starting location
x_goal = (300, 300, 300)  # goal location

Q = np.array([(8, 4)])  # length of tree edges
r = 0.1  # length of smallest edge to check for intersection with obstacles
max_samples = 10000  # max number of samples to take before timing out
rewire_count = 32  # optional, number of nearby branches to rewire
prc = 0.1  # probability of checking for a connection to goal

# create Search Space
X = SearchSpace(X_dimensions, Obstacles)

# create rrt_search
rrt = RRTStar(X, Q, x_init, x_goal, max_samples, r, prc, rewire_count)
path = rrt.rrt_star()

print(path)
str_path=""
for p in range(len(path)):
    str_path += '(' + str(path[p][0]) + ','
    str_path += str(path[p][1]) + ','
    str_path += str(path[p][2]) + ')' + ' \n '
    
f = open('path.txt','w')
f.write('\n'+ str_path)
f.close()
# plot
plot = Plot("rrt_star_3d")
plot.plot_tree(X, rrt.trees)
if path is not None:
    plot.plot_path(X, path)
plot.plot_obstacles(X, Obstacles)
plot.plot_start(X, x_init)
plot.plot_goal(X, x_goal)
plot.draw(auto_open=True)

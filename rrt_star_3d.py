# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
from sklearn.cluster import DBSCAN
import numpy as np
import random
from src.rrt.rrt_star import RRTStar
from src.search_space.search_space import SearchSpace
from src.utilities.plotting import Plot
def take_first(a_list):
    return(a_list[0])
def distance(x,y,z,i,j,k):
    t=(x-i)**2+(y-j)**2+(z-k)**2
    return np.sqrt(t)
def point_generate(i,j,k,p): # point x,y,z ve küp köşegen uzaklığı
    return (i,j,k,i+p,j+p,k+p)
def cluster_generate(i,j,k,radius,p):
    point_in_cluster=[]
    for _ in range (num_of_points): # clusterdaki point sayısı kadar dönecek, noktalar merkeze en fazla r uzaklığında olacak
        point_x=random.randint(i,i+radius)
        point_y=random.randint(j,j+radius)
        point_z=random.randint(k,k+radius)
        point=point_generate(point_x,point_y,point_z,p)
        Obstacles_list.append(point)
        apoint=[point_x,point_y,point_z]    
        point_in_cluster.append(apoint)
    
    dis=[0]*len(point_in_cluster)
    for m in range(len(point_in_cluster)):
        point=point_in_cluster[m]
        d=distance(i,j,k,point[0],point[1],point[2])
        dis[m]=[d,m] # clusterdaki her noktanın merkeze uzaklığı ve o noktanın indexi
    dis.sort(reverse=True, key=take_first) # distance a göre sıralama
    
    circumfrance_list=dis[:int(np.ceil(num_of_points*0.8))] # circumfrance seçmek merkeze en uzak 10 nokta arasından r/2 den büyük olanlar

    id_list=[1]*len(circumfrance_list)
    for u in range(len(circumfrance_list)):
        if (circumfrance_list[u][0] > radius*0.6):
            id_list[u]=circumfrance_list[u][1]
    for n in range(len(id_list)):
        id=id_list[n]
        
        cir_point=point_in_cluster[id]
        circumfrance_points.append(point_generate(cir_point[0],cir_point[1],cir_point[2],p))
def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

#source = "ABABDBAAEDSBQEWBAFLSAFB"
#print(list_duplicates_of(source, 'B'))
       
def determine_cluster(Obstacles_list,circumfrance_points):
    data_list=[]
    for w in range(len(Obstacles_list)):
        obs_ls=Obstacles_list[w][:3]
        data_list.append(obs_ls)
    for q in range(len(circumfrance_points)):
        obs_lst=circumfrance_points[q][:3]
        data_list.append(obs_lst)
    data=np.array(data_list)/100
    db = DBSCAN(eps=0.7, min_samples=1).fit(data)
    labels = db.labels_
    #for x in range(9):
     #   exec("string" + str(x) + " = 'hello'")
    #len(set(labels))
    label_0,label_1,label_2,label_3,label_4=([] for i in range(5))
    labels_list=labels.tolist()
    for k in range(len(labels)):
        if (labels_list[k] == 0):
            label_0.append(k)
        if (labels_list[k] == 1):
            label_1.append(k)
        if (labels_list[k] == 2):
            label_2.append(k)
        if (labels_list[k] == 3):
            label_3.append(k)
        if (labels_list[k] == 4):
            label_4.append(k)

    print(label_0)        
def find_cluster_center(cluster_points):
    a=[]
    for i in range(len(cluster_points)):
        x=cluster_points[i][0]
        y=cluster_points[i][1]
        z=cluster_points[i][2]
        avg_x =+ x
        avg_y =+ y
        avg_z =+ z
    cluster_center_x=avg_x/len(cluster_points)
    cluster_center_y=avg_y/len(cluster_points)
    cluster_center_z=avg_z/len(cluster_points)
    a=[cluster_center_x, cluster_center_y, cluster_center_z]
    return a
def find_cluster_radius(point_in_cluster,cluster_center):
    dis=[0]*len(point_in_cluster)
    for m in range(len(point_in_cluster)):
        point=point_in_cluster[m]
        d=distance(i,j,k,point[0],point[1],point[2])
        dis[m]=[d,m] # clusterdaki her noktanın merkeze uzaklığı ve o noktanın indexi
    dis.sort(reverse=True, key=take_first) # distance a göre sıralama
    radius=dis[:0]
    return radius
X_dimensions = np.array([(0, 300), (0, 300), (0, 300)])  # dimensions of Search Space
# obstacles
radius=50
p=10
Obstacles_list=[]
center_list=[]
point_list=[]
dis=[]
num_of_points=random.randint(10,12)
circumfrance_list=[]
circumfrance_points=[]

#for _ in range (num_of_obs):
#    i=random.randint(0,300)
#    j=random.randint(-80,80)
#    k=random.randint(-80,80)
#    point=(i,i-j,i-k,i+p,i-j+p,i-k+p)
#    Obstacles_list.append(point)
#Obstacles=np.array(Obstacles_list)
num_of_clusters=random.randint(5,10)
for _ in range (num_of_clusters):#generate random centers
    center_x=random.randint(0,300)
    center_y=random.randint(0,300)
    center_z=random.randint(0,300)
    center=[center_x,center_y,center_z]
    center_list.append(center)

for center in center_list: #center list kadar cluster yaratmak
    cluster_generate(center[0],center[1],center[2],radius,p)
Obstacles=np.array(Obstacles_list)
Circumfrances=np.array(circumfrance_points)
determine_cluster(Obstacles_list,circumfrance_points)
#Obstacles = np.array(
   #[(20, 20, 20, 40, 40, 40),(20, 20, 60, 40, 40, 80), (20, 60, 20, 40, 80, 40), (60, 60, 20, 80, 80, 40),
    #(60, 20, 20, 80, 40, 40), (60, 20, 60, 80, 40, 80), (20, 60, 60, 40, 80, 80), (60, 60, 60, 80, 80, 80),(90,90,90,95,95,95)])
x_init = (0, 0, 0)  # starting location
x_goal = (300, 300, 300)  # goal location

Q = np.array([(8, 4)])  # length of tree edges
r = 1  # length of smallest edge to check for intersection with obstacles
max_samples = 100000  # max number of samples to take before timing out
rewire_count = 32  # optional, number of nearby branches to rewire
prc = 0.1  # probability of checking for a connection to goal

# create Search Space
X = SearchSpace(X_dimensions, Obstacles)

# create rrt_search
rrt = RRTStar(X, Q, x_init, x_goal, max_samples, r, prc, rewire_count)
path = rrt.rrt_star()

#print(path)
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
plot.plot_c_obstacles(X, Circumfrances)
plot.plot_start(X, x_init)
plot.plot_goal(X, x_goal)
plot.draw(auto_open=True)

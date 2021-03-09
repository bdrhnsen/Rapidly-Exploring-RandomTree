# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.
from sklearn.cluster import DBSCAN
import numpy as np
import random
from src.rrt.rrt_star import RRTStar
from src.search_space.search_space import SearchSpace
from src.utilities.plotting import Plot
from functools import partial
from collections import Counter



def take_first(a_list):
    return(a_list[0])
def take_second(a_list):
    return(a_list[1])
def distance(x,y,z,i,j,k):
    t=(x-i)**2+(y-j)**2+(z-k)**2
    return np.sqrt(t)
def recover_point(point):
    p=point[:3]
    # p[0]=p[0]+r
    # p[1]=p[1]+r
    # p[2]=p[2]+r
    return p
def point_generate(i,j,k,p): # point x,y,z ve küp köşegen uzaklığı
    return (i-p,j-p,k-p,i+p,j+p,k+p)
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

    # dis=[0]*len(point_in_cluster)
    # for m in range(len(point_in_cluster)):
    #     point=point_in_cluster[m]
    #     d=distance(i,j,k,point[0],point[1],point[2])
    #     dis[m]=[d,m] # clusterdaki her noktanın merkeze uzaklığı ve o noktanın indexi
    # dis.sort(reverse=True, key=take_first) # distance a göre sıralama

    # circumfrance_list=dis[:int(np.ceil(num_of_points*0.8))] # circumfrance seçmek merkeze en uzak 10 nokta arasından r/2 den büyük olanlar



def count_how_many_elements(labels):

    label_count=len(set(labels))
    labeling_list=[1]*label_count
    c = Counter(labels)
   #label ve o labela ait kaç tane eleman var
    for i in range(label_count):
        labeling_list[i]=c.get(i)

    return labeling_list
def determine_cluster(Obstacles_list):
    data_list=[]
    for w in range(len(Obstacles_list)):
        obs_ls=Obstacles_list[w][:3]
        data_list.append(obs_ls)

    data=np.array(data_list)/100
    db = DBSCAN(eps=0.7, min_samples=1).fit(data)
    labels = db.labels_

    labels_list=labels.tolist()
    label_count=len(set(labels))
    clustered_points=[]
    temp=labels_list[0]
    for k in range (len(Obstacles_list)): # nokta sayısı kadar dönüyor clustered point in içine [x,y,z], label şeklinde atıyorum sonrasında labellarına göre sıralıyorum
        a=[recover_point(Obstacles_list[k]), labels_list[k]]
        clustered_points.append(a)

    clustered_points.sort(key=take_second)
    counter_list=count_how_many_elements(labels)


    draw_wall(Obstacles_list,clustered_points,counter_list,labels_list,p)
#ctrl shift 7 , ctrl u k

def draw_wall(Obstacles_list,clustered_points,counter_list,labels_list,p):#clustered_list [x,y,z,label] şeklinde ve labellara göre sıralı
    #counter_list = [label labeldan kaç tane olduğu]
    a_list=[]
    temp=0

    for p in range(len(clustered_points)):
        if clustered_points[p][1]== temp:
            a_list.append(clustered_points[p][0])
        else:
            center=find_cluster_center(a_list)
            radius=find_cluster_radius(a_list,center,p)
            big_guns.append(point_generate(center[0],center[1],center[2],radius))
            temp=clustered_points[p][1]
            a_list=[]
            a_list.append(clustered_points[p][0])
        #print(a_list)
    center=find_cluster_center(a_list)
    radius=find_cluster_radius(a_list,center,p)
    big_guns.append(point_generate(center[0],center[1],center[2],radius))

    #print("temp",temp)
    #print("relative",clustered_points[p][1])


        # if k==0:
        #     temp=temp+counter_list[k]
        #     #print("ilk temp",temp)
        #     a_cluster=clustered_points[0:counter_list[0]]
        #     print(clustered_points[0][1])
        #     #print("k =0 ",a_cluster)
        # if k == (len(counter_list)-1):

        #     a_cluster=clustered_points[temp:]

        #     temp=temp+counter_list[k]
        #     #print("k = son ",a_cluster,"son temp",temp)

        # else:

        #     a_cluster=clustered_points[temp:temp+counter_list[k]]
        #     #print("k diğer",a_cluster,"diğer temp",temp)
        #     temp=temp+counter_list[k]


        #only_points=list(zip(*a_cluster))


        # center=find_cluster_center(only_points)
        # radius=find_cluster_radius(only_points,center)
        # print(center)
        # print(radius)

def find_cluster_center(cluster_points): #taking the average of points in a cluster
    a=[]
    avg_x = 0
    avg_y = 0
    avg_z = 0
    for i in range(len(cluster_points)):
        x=cluster_points[i][0]

        y=cluster_points[i][1]
        z=cluster_points[i][2]
        avg_x += x
        avg_y += y
        avg_z += z
    cluster_center_x=avg_x/len(cluster_points)
    cluster_center_y=avg_y/len(cluster_points)
    cluster_center_z=avg_z/len(cluster_points)
    a=[cluster_center_x, cluster_center_y, cluster_center_z]
    return a
def find_cluster_radius(point_in_cluster,cluster_center,p):
    dis=[0]*len(point_in_cluster)
    for m in range(len(point_in_cluster)):
        point=point_in_cluster[m]
        d=distance(cluster_center[0],cluster_center[1],cluster_center[2],point[0],point[1],point[2])
        dis[m]=[d,m] # clusterdaki her noktanın merkeze uzaklığı ve o noktanın indexi
    dis.sort(reverse=True, key=take_first) # distance a göre sıralama
    radius=dis[0][0]


    circumfrance_list=dis[:int(np.ceil(len(dis)*0.8))] # circumfrance seçmek merkeze en uzak 10 nokta arasından r/2 den büyük olanla
    id_list=[1]*len(circumfrance_list)
    for u in range(len(circumfrance_list)):
        if (circumfrance_list[u][0] > radius*0.6):
            id_list[u]=circumfrance_list[u][1]
    for n in range(len(id_list)):
        id=id_list[n]
        cir_point=point_in_cluster[id]
        circumfrance_points.append((cir_point[0],cir_point[1],cir_point[2]))





    print(circumfrance_points)
    return radius


X_dimensions = np.array([(0, 300), (0, 300), (0, 300)])  # dimensions of Search Space
# obstacles
radius=50
p=10
Obstacles_list=[]
big_guns=[]
center_list=[]
point_list=[]
dis=[]
num_of_points=3
circumfrance_list=[]
circumfrance_points=[]
drone_size=10
num_of_clusters=5





for _ in range (num_of_clusters):#generate random centers
    center_x=random.randint(0,300)
    center_y=random.randint(0,300)
    center_z=random.randint(0,300)
    center=[center_x,center_y,center_z]
    center_list.append(center)

for center in center_list: #center list kadar cluster yaratmak
    cluster_generate(center[0],center[1],center[2],radius,p)
Obstacles=np.array(Obstacles_list)
Guns=np.array(big_guns)

Circumfrances=np.array(circumfrance_points)
determine_cluster(Obstacles_list)
Guns=np.array(big_guns)


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
X = SearchSpace(X_dimensions, Guns)

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
#plot.plot_obstacles(X, Guns)
plot.plot_obstacles(X, Obstacles)
plot.plot_c_obstacles(X, Guns)
plot.plot_start(X, x_init)
plot.plot_goal(X, x_goal)
plot.draw(auto_open=True)

## Requirements
- [Python 3+](https://www.python.org/downloads/)
- [NumPy](http://www.numpy.org/)
- [Rtree](https://pypi.python.org/pypi/Rtree/)
- [Plotly](https://plot.ly/python/getting-started/) (only needed for plotting)

### Additions by bdrhnsen

Test cases for randomly generated point

Test cases for randomly generated clusters from randomly generated cluster centers

Finding cluster's points close to the circumfrance points

Clustering algorithm

Clustering the 3d point cloud, finding the center and the radius of the cluster with that creating solid objects from dense point cloud clusters

Making sure that the point is actually never near the obstacles


# How to use
This 3D path finding algorithm structure works with 6 point representation of obstacles. First 3 points represent one corners coordinates, second 3 points represent the diagonally opposite corner's coordinates
recover_point(), generate_point() functions are for using this structure

### Decrease r to obtain higher resolution but slower algorithm



###
### First I worked on generating random clusters
for this algorithm first generates cluster centers randomly and than cluster_generate() takes this centers and generates bunch of points inside a predifined or randomly generated radius

 ### Clustering the point cloud
 with the function determine_cluster() algorithm determines clusters from point cloud and labels every point of the point cloud according to their clusters assume 15 points labels=[000111222000333] obstacle_list involves 6 point representations of these labeled points indexes are the same for this points in other words with label's index value you can reach the corresponding point in the point cloud
 clustering is obtained via DBScan algorithm, this algorithm used with sklearn library


### Finding cluster center
  find_cluster_center is basically do is to take the average of the points inside a cluster and call that point is the center
### Finding cluster radius
  find_cluster_radius checks out the distance between center of cluster and every other point inside the cluster take the highest of this and call it as a radius
  also in this function I have determined the circumfrance points of each cluster in other words outermost points of the cluster so that afterward we can check out collisions
### Drawing solid objects to the places of dense point clouds
  Imagine a wall with a lot of points it will still involve voids inside of it. So we tought that we can transform dense areas in the point cloud to solid objects
### Algorithm writes the path to path.txt in the folder
 (0,0,0) Start point
 (106.21429611776344,71.35814892595091,89.70789264779327) 
 (256.28516275891604,159.07700800706624,154.78170794109664) 
 (271.2209359156651,178.51848090806106,198.00593488816747) 
 (277.9660395676152,180.84929085420882,201.62130509319329) 
 (401.4330690245277,260.66835337203236,200.07440934260305) 
 (460.0044443644424,298.20373076009486,201.22409380234296) 
 (502.85501173944687,320.8217744755939,294.5629443086615) 
 (536.7312743725813,336.6554683999527,359.9002216219722) 
 (558.3324235175052,359.0960591453908,494.1447171251188) 
 (560.1718941489172,386.3120106522683,533.5136796717535) 
 (599.8417698983674,469.7331781787355,606.0895002090638) 
 (616.9964035056961,490.4749916612772,634.8052291482487) 
 (658.5965966064321,554.1004307687786,694.2624689200721) 
 (650.9356369580811,622.5866184864578,714.3795342046307) 
 (665.8232078011285,679.1509810772092,750.3646917323962) 
 (712.4072438175909,752.1923236248156,796.6914709416856) 
 (900,900,900) end point
path look like this  
This path will be given to trajectory controller of the quadcopter it may be is sensible to smoothen the path before giving it to trajectory controller because it may be impossible for quadcopter to pull it of some manuevers 





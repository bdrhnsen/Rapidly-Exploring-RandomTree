## Requirements
- [Python 3+](https://www.python.org/downloads/)
- [NumPy](http://www.numpy.org/)
- [Rtree](https://pypi.python.org/pypi/Rtree/)
- [Plotly](https://plot.ly/python/getting-started/) (only needed for plotting)

## Usage
Define an n-dimensional Search Space, and n-dimensional obstacles within that space. Assign start and goal locations as well as the number of iterations to expand the tree before testing for connectivity with the goal, and the max number of overall iterations.

### Search Space
Assign bounds to Search Space in form: `[(x_lower, x_upper), (y_lower, y_upper), ...]`

### Start and Goal
Points represented by tuples of form: `(x, y, ...)`

### Obstacles
Axis-aligned (hyper)rectangles represented by a tuples of form `(x_lower, y_lower, ..., x_upper, y_upper, ...)`

Non-axis aligned (hyper)rectangles or other obstacle representations should also work, provided that `collision_free` and `obstacle_free` are updated to work with the new obstacles.

### Resolution
Assign resolution of edges:
- `q`: Distance away from existing vertices to probe.
- `r`: Discretization length to use for edges when sampling along them to check for collisions. Higher numbers run faster, but may lead to undetected collisions.


[MIT License](https://github.com/motion-planning/rrt-algorithms/blob/master/LICENSE)

Additions by AHMET BEDIRHAN SEN

Test cases for randomly generated point

Test cases for randomly generated clusters from randomly generated cluster centers

Finding cluster's points close to the circumfrance points

Clustering algorithm

Clustering the 3d point cloud, finding the center and the radius of the cluster with that creating solid objects from dense point cloud clusters

Making sure that the point is actually never near the obstacles



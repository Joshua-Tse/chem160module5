import math
# Function to produce distance between two list points
def dist(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)
def sqmag(a):
    return (a[0]**2+a[1]**2+a[2]**2)
def vector(a,b):
    r=dist(a,b)
    x=(a[0]-b[0])/r
    y=(a[1]-b[1])/r
    z=(a[2]-b[2])/r
    return [x,y,z]
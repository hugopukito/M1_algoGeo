import halfedge_mesh
import math

# .off are supported
# mesh = maillage 

mesh = halfedge_mesh.HalfedgeMesh("tests/data/cube_seg.off")
filename = "tests/data/cube_seg2.off"

def moyenne_angle():

    list = [] 

    for f in mesh.facets:
        st1 = f.halfedge.get_angle_normal()
        nd2 = f.halfedge.next.get_angle_normal()
        rd3 = f.halfedge.next.next.get_angle_normal()

        result = (st1 + nd2 + rd3) / 3
        list.append(result)
        
    return list

def mettre_degre(l):

    for i in l:
        print((i/math.pi)*180)

def colorier(l):

    l2 = []
    
    for i in l:
        l2.append((i-min(l))/(max(l)-min(l)))
    
    return l2



l = moyenne_angle()
print(colorier(l))



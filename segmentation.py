import halfedge_mesh
import math

# .off are supported
# mesh = maillage 

mesh = halfedge_mesh.HalfedgeMesh("tests/data/cube_seg.off")
filename = "tests/data/cube_seg2.off"
filename2 = "tests/data/cube_seg3.off"

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

def moyenne_angle_min_max(l):

    l2 = []
    
    for i in l:
      j = (i-min(l))/(max(l)-min(l))
      l2.append(truncate(j))
    
    return l2

def truncate(num):
    temp = str(num)
    temp2 = ""
    if temp == "0.0":
      temp2 = "0.000"
    elif temp == "1.0":
      temp2 = "1.000"
    else:
      for i in range(5):
        temp2 += temp[i]
    return temp2

def truncate2(num, seuil):
  if (num < seuil):
    return "1.000"
  else:
    return "0.000"

def colorier(filename, l, type):
    mesh.save_vertices(filename, l, type)

def coloriertwoClass(l):

    l2 = []

    #valeur déjà entre 0 et 1
    moyenne = 0.0
    for j in l:
      moyenne += float(j)
    moyenne = moyenne / len(l)
    
    for j in l:
      l2.append(truncate2(float(j), moyenne))

    return l2

def colorier2(filename, l, type):
    mesh.save_vertices(filename, l, type)
    

valeurs = moyenne_angle()
valeurs = moyenne_angle_min_max(valeurs)
#print(valeurs)
#colorier(filename, valeurs, "firstSeg")
valeurs2 = coloriertwoClass(valeurs)
#print(valeurs2)
colorier2(filename2, valeurs2, "TwoClassSeg")



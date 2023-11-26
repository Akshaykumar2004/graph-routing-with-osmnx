from matplotlib import pyplot as plt
import osmnx as ox

class Node():

  def __init__(self,value,x,y,name=None,amenity=None):
    self.v = value
    self.x = x
    self.y = y
    self.n = []
    self.name=name
    self.amenity=amenity

  def __str__(self): 
     return str(self.v)

class Graph():

    def __init__(self):
        self.nodes={}
        self.edges={}

    def add_node(self,value,x,y,name=None,amenity=None):
        node = Node(value,x,y,name,amenity)
        self.nodes[value] = node
        return self

    def add_edge(self,v1,v2,time=None):
        node1 = self.nodes[v1]
        node2 = self.nodes[v2]

        if (node1,node2) not in self.edges:
            node1.n.append(node2)
            self.edges[(node1,node2)] = time
            return self

        elif node1 and node2:
            print("There is already connection between",node1,node2)
            return self

        else:
            if node1:
                raise Exception('No node with value:',v2)
            else:
                raise Exception('No node with value:',v1)
        return self

    def FindShortestPathBy_nodes(self, start, end):
        if start == end:
            raise Exception('start cannot be the end')

        if not isinstance(start, Node):
            start = self.nodes[start]

        if not isinstance(end, Node):
            end = self.nodes[end]

        q = [start]
        visited = set()
        parent = {}

        visited.add(start)

        while(q!=[]):
           c = q.pop(0)
           if c == end:
                path = []
                while c != start:
                  path.append(c)
                  c = parent[c]
                path.append(start)
                path.reverse()
                return path

           for n in c.n:
              if n not in visited:
                 visited.add(n)
                 q.append(n)
                 parent[n] = c

        return None

    def calc_path_time(self,path):
      time = 0.0
      for i in range(1,len(path)):
        time += self.edges[(path[i-1],path[i])]
      return round(time/60,2)

    def FindShortestPathBy_addr(self,Graph,start,dest):
       y,x = ox.geocode(start)
       start = ox.nearest_nodes(Graph,x,y)

       y,x = ox.geocode(dest)
       dest = ox.nearest_nodes(Graph,x,y)
       print(start,dest)

       path = self.FindShortestPathBy_nodes(self.nodes[start],self.nodes[dest])
       return path

    def plot_nodes(self):
      fig = plt.figure()
      nodes = self.nodes
      for i,j in nodes.items():
        plt.scatter(j.x,j.y,color='grey')
        plt.text(j.x,j.y,i)
      plt.axis('off')
      return fig

    def plot_edges(self):
      fig = plt.figure(facecolor='black')

      nodes = self.nodes
      for i,j in nodes.items():
        plt.scatter(j.x,j.y,color='white',s=5)
        # plt.text(j.x,j.y,i)

      for i,j in self.edges:
        plt.plot([i.x,j.x],[i.y,j.y],color='#d7dddf',linewidth='0.5')

      plt.axis('off')
      return fig

    def near_poi(self,graph,start,amenity):
      x,y = ox.geocode(start)
      start = ox.nearest_nodes(graph,y,x)
      amenity = amenity.lower()
      poi_paths = []
      for i,j in self.nodes.items():
        if j.amenity == amenity:
          # print(i,j.v,j.name,j.amenity)
          # path = self.FindShortestPathBy_nodes(start,i)
          end = ox.nearest_nodes(graph,j.x,j.y)
          path = self.FindShortestPathBy_nodes(start,end)
          if path:
            poi_paths.append(path)

      s_path = poi_paths[0]
      for i in poi_paths:
        if len(i) < len(s_path):
          s_path = i

      name = s_path[len(s_path)-1].name

      return s_path,name
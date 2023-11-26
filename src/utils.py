import osmnx as ox


def find_pois_place(query):
   pois = ox.features_from_place(query,tags={"amenity":True})
   places = {}
   for i in range(len(pois)):
      ele = pois.index[i]
      if 'node' in ele:
          x,y = pois.iloc[i]['geometry'].x,pois.iloc[i]['geometry'].y
          places[ele[1]] = {"name":pois.iloc[i]['name'],"amenity":pois.iloc[i]['amenity'],'x':x,"y":y}
   return places


def find_pois_address(query,dist=1000):
   pois = ox.features_from_address(query,tags={"amenity":True},dist=dist)
   places = {}
   for i in range(len(pois)):
      ele = pois.index[i]
      if 'node' in ele:
          x,y = pois.iloc[i]['geometry'].x,pois.iloc[i]['geometry'].y
          places[ele[1]] = {"name":pois.iloc[i]['name'] if str(pois.iloc[i]['name'])!='nan' else None,
                            "amenity":pois.iloc[i]['amenity'],
                            'x':x,
                            "y":y}
   return places

def add_ox_nodes(g1 ,g2 ): #g1-my graph, g2-ox graph
  for i,j in g2.nodes.items():
    g1.add_node(i,j['x'],j['y'])
  print("succesfully uploaded the nodes.")

def add_ox_edges(g1, g2):
  for i,j,t in g2.edges(data='travel_time'):
      g1.add_edge(i,j,t)

def insert_poi(g,poi):
  for i,j in poi.items():
    g.add_node(i,j['x'],j['y'],j['name'],j['amenity'])
  print('succesfully added point of interests')
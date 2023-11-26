import osmnx as ox
from .MyGraph import Graph 
from .utils import add_ox_nodes, add_ox_edges, find_pois_address, insert_poi
import matplotlib.pyplot as plt

class App():

    def __init__(self):
        self.query = input("Enter your location(default: Rajarajeshwari nagar, Bangalore): ") or "Rajarajeshwari nagar, Bangalore"
        r = input('Enter Radius in meters(default: 2000): ') or "2000"
        self.r = int(r)
        self.ox_graph = None
        self.my_graph = None
        self.ox_init()
        self.mg_init()

    def ox_init(self): 
        graph = ox.graph_from_address(self.query, self.r)
        graph = ox.distance.add_edge_lengths(graph)
        graph = ox.speed.add_edge_speeds(graph)
        graph = ox.speed.add_edge_travel_times(graph)
        self.ox_graph = graph 

    def mg_init(self):
        mygraph = Graph()
        add_ox_nodes(mygraph, self.ox_graph)
        add_ox_edges(mygraph, self.ox_graph)
        pois = find_pois_address(self.query)
        insert_poi(mygraph, pois)
        self.my_graph = mygraph

    def find_path(self, start, end):
        try:
            path = self.my_graph.FindShortestPathBy_addr(self.ox_graph, start, end)  
            path_ids = [i.v for i in path]
            fig, ax = ox.plot_graph_route(self.ox_graph, path_ids, route_color='b', route_linewidth=6, node_size=0)
            print("It takes {} minutes to reach from \"{}\" to \"{}\".\n".format(self.my_graph.calc_path_time(path), start, end))
            plt.show()
        except Exception as e:
            print(e)

    def find_near_poi(self, start, amenity):
        try:
            path, name = self.my_graph.near_poi(self.ox_graph, start, amenity.lower())
            path_ids = [i.v for i in path]
            fig, ax = ox.plot_graph_route(self.ox_graph, path_ids, route_color='b', route_linewidth=6, node_size=0)
            print("It takes {} minutes to reach from \"{}\" to nearest \"{}\".\n".format(self.my_graph.calc_path_time(path), start, amenity))
            plt.show()
        except Exception as e:
            print(e)

    def find_near_POI(self): 
        start = input("Enter your starting point(default: Rajarajeshwari temple, Rajarajeshwari nagar, Bangalore): ") or "Rajarajeshwari temple, Rajarajeshwari nagar, Bangalore"
        amenity = input("Enter your point of interest please(default: hospital): ") or "hospital"
        self.find_near_poi(start, amenity)

    def search_route(self):  
        start = input("Enter From address(default: Rajarajeshwari temple, Rajarajeshwari nagar, Bangalore): ") or "Rajarajeshwari temple, Rajarajeshwari nagar, Bangalore"
        end = input("Enter To address(default: RV University, Bangalore): ") or "RV University, Bangalore"
        self.find_path(start, end)

    def menu(self):
        print("Please choose from the below options:\n")
        print("1: Find nearest point of interest\n")
        print("2: Search for route\n")
        print("3: Exit\n")
    
    def run(self):
        
        while True:
            self.menu()
            user_choice = input("\nEnter your choice: ")

            match user_choice:
                case '1':
                    self.find_near_POI()
                case '2':
                    self.search_route()
                case '3':
                    break
                case _:
                    print("Please enter appropriate input")
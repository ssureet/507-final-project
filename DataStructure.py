class Node:
    def __init__(self, episode, show, season, guest_star, directors, writers, air_date, viewer_count, air_month, air_year, imdb_rating, shortened_viewer):
        import pandas as pd 
        
        self.episode = int(episode) if not pd.isna(episode) else 0
        self.show = show
        self.season = int(season) if not pd.isna(season) else 0
        self.guest_star = guest_star
        self.directors = directors
        self.writers = writers
        self.air_date = air_date
        self.viewer_count = viewer_count
        self.air_month = air_month
        self.air_year = air_year
        self.imdb_rating = imdb_rating
        self.shortened_viewer = shortened_viewer
        self.episode_id = f"{show}_S{season}_E{episode}"
        self.edges = []  # List to store edges connected to this node

    def __str__(self):
        return f"Episode {self.episode_id} of {self.show}, Season {self.season}"

    def add_edge(self, edge):
        self.edges.append(edge)

    def get_similarity_score(self, other_node):
        """
        Calculate the number of shared edges (attributes) between this node and another node.
        Returns the score (number of shared edges) and a list of similarities.
        """
        shared_attributes = []
        
        guest_star1 = self.guest_star if isinstance(self.guest_star, str) else ""
        guest_star2 = other_node.guest_star if isinstance(other_node.guest_star, str) else ""
        
        guest_star1_set = set(guest_star1.split(',')) if guest_star1 else set()
        guest_star2_set = set(guest_star2.split(',')) if guest_star2 else set()

        guest_star1_set = {gs.strip() for gs in guest_star1_set if gs.strip()}  # Strip and remove empty strings
        guest_star2_set = {gs.strip() for gs in guest_star2_set if gs.strip()}  # Strip and remove empty strings

        if guest_star1_set and guest_star2_set and guest_star1_set.intersection(guest_star2_set):
            shared_attributes.append(('guest_star', guest_star1_set.intersection(guest_star2_set)))

        if set(self.directors.split(',')).intersection(set(other_node.directors.split(','))):
            shared_attributes.append(('director', set(self.directors.split(',')).intersection(set(other_node.directors.split(',')))))

        if set(self.writers.split(',')).intersection(set(other_node.writers.split(','))):
            shared_attributes.append(('writer', set(self.writers.split(',')).intersection(set(other_node.writers.split(',')))))

        if self.air_date == other_node.air_date:
            shared_attributes.append(('air_date', [self.air_date]))

        if self.air_month == other_node.air_month and self.air_year == other_node.air_year:
            shared_attributes.append(('air_month_year', [self.air_month, self.air_year]))

        if self.shortened_viewer == other_node.shortened_viewer:
            shared_attributes.append(('shortened_viewer', [self.shortened_viewer]))

        if self.imdb_rating == other_node.imdb_rating:
            shared_attributes.append(('imdb_rating', [self.imdb_rating]))

        return len(shared_attributes), shared_attributes


                

class Edge:
    def __init__(self, node1, node2, edge_type, shared_attributes):
        self.node1 = node1
        self.node2 = node2
        self.edge_type = edge_type
        self.shared_attributes = shared_attributes

    def __str__(self):
        return f"Edge between {self.node1.episode} and {self.node2.episode}, Type: {self.edge_type}, Shared: {self.shared_attributes}"

    @classmethod
    def create_edge(cls, node1, node2, edge_type, shared_attributes):
        if shared_attributes:
            return cls(node1, node2, edge_type, shared_attributes)
        return None
    

class Graph:
    def __init__(self):
        self.nodes = {}  
        self.edges = []  
    
    def add_node(self, node):
        self.nodes[node.episode_id] = node
    
    def add_edge(self, edge):
        self.edges.append(edge)
        edge.node1.add_edge(edge)
        edge.node2.add_edge(edge)
    
    def get_node(self, episode_id):
        return self.nodes.get(episode_id)
    
    def get_all_nodes(self):
        return list(self.nodes.values())
    
    def get_edges(self):
        return self.edges


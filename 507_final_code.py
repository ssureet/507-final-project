from DataStructure import Node, Edge, Graph

class GraphBuilder:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.graph = Graph()  # Create a new graph instance

    def load_data(self):
        import pandas as pd
        """Load data from the CSV file and create nodes."""
        df = pd.read_csv(self.csv_file)

        df['season'] = df['season'].fillna(0).astype(int)
        df['episode'] = df['episode'].fillna(0).astype(int)

        for _, row in df.iterrows():
            node = Node(
                show=row['show'],
                season=row['season'],
                episode=row['episode'],
                guest_star=row['guest_star'],
                directors=row['directors'],
                writers=row['writers'],
                air_date=row['air_date'],
                viewer_count=row['viewer_count'],
                air_month=row['air_month'],
                air_year=row['air_year'],
                imdb_rating=row['imdb_rating'],
                shortened_viewer=row['shortened_viewer']
            )
            self.graph.add_node(node)

    def build_graph(self):
        """Build the graph by comparing nodes and adding edges."""
        for node1 in self.graph.get_all_nodes():
            for node2 in self.graph.get_all_nodes():
                if node1 != node2:
                    self.compare_nodes_and_add_edges(node1, node2)

    def compare_nodes_and_add_edges(self, node1, node2):
        """Compare two nodes and create edges based on shared attributes."""
        shared_attributes = []

        # Compare guest stars
 
        guest_star1 = node1.guest_star if isinstance(node1.guest_star, str) else ""
        guest_star2 = node2.guest_star if isinstance(node2.guest_star, str) else ""
        
        guest_star1_set = set(guest_star1.split(',')) if guest_star1 else set()
        guest_star2_set = set(guest_star2.split(',')) if guest_star2 else set()

        guest_star1_set = {gs.strip() for gs in guest_star1_set if gs.strip()}  # Strip and remove empty strings
        guest_star2_set = {gs.strip() for gs in guest_star2_set if gs.strip()}  # Strip and remove empty strings

        if guest_star1_set and guest_star2_set and guest_star1_set.intersection(guest_star2_set):
            shared_attributes.append(('guest_star', guest_star1_set.intersection(guest_star2_set)))

        # Compare directors
        if set(node1.directors.split(',')).intersection(set(node2.directors.split(','))):
            shared_attributes.append(('director', set(node1.directors.split(',')).intersection(set(node2.directors.split(',')))))
        
        # Compare writers
        if set(node1.writers.split(',')).intersection(set(node2.writers.split(','))):
            shared_attributes.append(('writer', set(node1.writers.split(',')).intersection(set(node2.writers.split(',')))))
        
        # Compare air date (exact match)
        if node1.air_date == node2.air_date:
            shared_attributes.append(('air_date', [node1.air_date]))
        
        # Compare air month and air year (together)
        if node1.air_month == node2.air_month and node1.air_year == node2.air_year:
            shared_attributes.append(('air_month_year', [node1.air_month, node1.air_year]))
        
        # Compare shortened viewer count
        if node1.shortened_viewer == node2.shortened_viewer:
            shared_attributes.append(('shortened_viewer', [node1.shortened_viewer]))
        
        # Compare IMDb ratings (exact match)
        if node1.imdb_rating == node2.imdb_rating:
            shared_attributes.append(('imdb_rating', [node1.imdb_rating]))
        
        # If there are any shared attributes, create an edge
        if shared_attributes:
            edge = Edge.create_edge(node1, node2, 'similarity', shared_attributes)
            if edge:
                self.graph.add_edge(edge)

    def find_most_similar_episodes(self, episode_of_interest, top_n=10):
        """Find and return the most similar episodes to the given episode."""
        node_of_interest = self.graph.get_node(episode_of_interest)

        print(f"Looking for episode: {episode_of_interest}")
        
        if node_of_interest is None:
            print(f"Error: Episode {episode_of_interest} not found in the graph.")
            return

        similarity_scores = []
  
        for node in self.graph.get_all_nodes():
            if node != node_of_interest:
                score, similarities = node_of_interest.get_similarity_score(node)
                similarity_scores.append((node, score, similarities))

        similarity_scores.sort(key=lambda x: x[1], reverse=True)

        top_similar_episodes = similarity_scores[:top_n]

        for similar_node, score, similarities in top_similar_episodes:
            print(f"Episode {similar_node.episode_id}: Similarity score = {score}")
            for similarity_type, shared in similarities:
                print(f"  - {similarity_type}: {shared}")
            print()  
    
    def build_adjacency_list(self):
        """Build the adjacency list from the graph."""
        adjacency_list = {}

        for edge in self.graph.get_edges():
            episode1_id = edge.node1.episode_id
            episode2_id = edge.node2.episode_id
            
            if edge.shared_attributes and any(attribute[1] for attribute in edge.shared_attributes):

                if episode1_id not in adjacency_list:
                    adjacency_list[episode1_id] = []
                adjacency_list[episode1_id].append((episode2_id, edge.shared_attributes))

                if episode2_id not in adjacency_list:
                    adjacency_list[episode2_id] = []
                adjacency_list[episode2_id].append((episode1_id, edge.shared_attributes))

        return adjacency_list

    def find_shortest_path(self, episode1_id, episode2_id):
        """Find and display the shortest path between two episodes using Dijkstra's algorithm."""

        adjacency_list = self.build_adjacency_list()  

        if episode1_id not in adjacency_list:
            print(f"Error: Episode {episode1_id} not found in the graph.")
            return
        if episode2_id not in adjacency_list:
            print(f"Error: Episode {episode2_id} not found in the graph.")
            return

        shortest_path = {episode: (None, float('inf')) for episode in adjacency_list}  
        shortest_path[episode1_id] = (None, 0)  
        visited = set()  
        nodes_to_visit = [episode1_id]  

        print(f"Starting Dijkstra from {episode1_id} to {episode2_id}")

        while nodes_to_visit:
            current_node = nodes_to_visit.pop(0)
            current_distance = shortest_path[current_node][1]

            if current_node == episode2_id:  
                break

            for neighbor, shared_attributes in adjacency_list[current_node]:
                if neighbor not in visited:
                    new_distance = current_distance + 1 
                    if new_distance < shortest_path[neighbor][1]:
                        shortest_path[neighbor] = (current_node, new_distance)
                        nodes_to_visit.append(neighbor)
            
            visited.add(current_node)

        path = []
        current_node = episode2_id
        while current_node:
            path.append(current_node)
            current_node = shortest_path[current_node][0]
        
        path = path[::-1]  
        
        if shortest_path[episode2_id][1] == float('inf'):
            print(f"No path exists between {episode1_id} and {episode2_id}")
            return

        print(f"\nShortest path from {episode1_id} to {episode2_id}:")
        for i in range(len(path) - 1):
            current_episode = path[i]
            next_episode = path[i + 1]
            shared_attributes = []
            for edge in self.graph.get_edges():
                if edge.node1.episode_id == current_episode and edge.node2.episode_id == next_episode:
                    shared_attributes = edge.shared_attributes
                    break
            print(f"  {current_episode} -> {next_episode} (Connection: {shared_attributes})")

    def find_most_connected_episode(self):
        """Find the episode with the most edges and display its connections."""
        max_edges_count = 0
        most_connected_episode = None
        for node in self.graph.get_all_nodes():
            if len(node.edges) > max_edges_count:
                max_edges_count = len(node.edges)
                most_connected_episode = node
        
        print(f"The most connected episode is {most_connected_episode.episode_id} with {max_edges_count} connections.")
        print(f"Connections: {len(most_connected_episode.edges)}")
        
        similarity_scores = []
        for node in self.graph.get_all_nodes():
            if node != most_connected_episode:
                score, _ = most_connected_episode.get_similarity_score(node)
                similarity_scores.append((node, score))
        
        similarity_scores.sort(key=lambda x: x[1], reverse=True)
    
        top_50_similar_episodes = similarity_scores[:50]
        self.visualize_top_50_similar(most_connected_episode, top_50_similar_episodes)

    def visualize_top_50_similar(self, most_connected_episode, top_50_similar_episodes):
        """Visualize the most similar connections of the most connected episode."""
        import matplotlib.pyplot as plt
        
        top_50_episode_ids = [episode[0].episode_id for episode in top_50_similar_episodes]
        similarities = [episode[1] for episode in top_50_similar_episodes]

        
        plt.figure(figsize=(10, 10))
        plt.barh(top_50_episode_ids, similarities, color='skyblue')
        plt.xlabel('Similarity Score')
        plt.ylabel('Episode ID')
        plt.title(f'Top 50 Most Similar Episodes to {most_connected_episode.episode_id}')
        plt.gca().invert_yaxis()  
        plt.show()

    def provide_episode_statistics(self, episode_id):
        """Provide a detailed summary of the episode."""
        episode = self.graph.get_node(episode_id)
        
        if not episode:
            print(f"Episode {episode_id} not found in the graph.")
            return
        
        # Print the episode statistics
        print(f"Episode Summary for {episode_id}:")
        print(f"  - Show: {episode.show}")
        print(f"  - Season: {episode.season}")
        print(f"  - Episode: {episode.episode}")
        print(f"  - Air Date: {episode.air_date}")
        print(f"  - Viewer Count: {episode.viewer_count}")
        print(f"  - IMDb Rating: {episode.imdb_rating}")
        print(f"  - Directors: {episode.directors}")
        print(f"  - Writers: {episode.writers}")
        print(f"  - Guest Stars: {episode.guest_star}")

def main():
    #load and create data
    graph = GraphBuilder(csv_file='./Desktop/507_final_data.csv')
    graph.load_data()
    graph.build_graph()

    #find shortest path between 2 episodes
    graph.find_shortest_path('Futurama_S7_E1', 'SouthPark_S6_E5')

    #find top 5 most similar episodes
    graph.find_most_similar_episodes('TheSimpsons_S17_E4', top_n=5)

    #find most connected episode and visualize connections
    graph.find_most_connected_episode()

    #get statistics of an episode
    graph.provide_episode_statistics('Futurama_S6_E2')

if __name__ == '__main__':
    main()

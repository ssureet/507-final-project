Interactions:
1. Load data from CSV
- The user will use a function from the GraphBuilder class to load a CSV file. The file is expected to contain the following columns: 
  show,	season,	episode,	guest_star,	directors,	writers,	air_date,	viewer_count,	shortened_viewer,	air_month,	air_year, and	imdb_rating
- Prompts: input/provide path to csv file
- Response: the code loads the data and creates nodes for each episode in the graph. Each episode is represented by a Node object 
  with attributes of the episode based on the CSV data.
- Example: 
  graph = GraphBuilder(csv_file='./Desktop/507_final_data.csv')
  graph.load_data()
  graph.build_graph()
2. Find Most Similar Episodes
- The user can ask the program to find the most similar episodes to a given episode. The program compares episodes based on shared attributes 
  like guest stars, directors, writers, and IMDb ratings. The program will automatically print the top 10 similar episodes with a list of 
  similarities, but the number of similar episodes can be customized
- Prompt: the user will provide the episode id (ShowName_S{seasonnumber}_E{episode number}) of an episode of interest and optionally fill the 
  argument top_n with the desired number of similar episodes they want to receive
- Response: The program finds and displays the top N most similar episodes (default is 10). It shows the similarity score and the shared attributes between each pair of episodes. If there is not an episode with that ID, it will print "Error: Episode {episode_of_interest} not found in the graph."
- Example:
  graph.find_most_similar_episodes('TheSimpsons_S2_E4', top_n=5)
      Episode TheSimpsons_S1_E11: Similarity score = 2
        - director: {'Wes Archer'}
        - writer: {' John Swartzwelder'}
      
      Episode TheSimpsons_S2_E5: Similarity score = 2
        - air_month_year: ['November', '1990']
        - shortened_viewer: [26.1]
      
      Episode TheSimpsons_S6_E10: Similarity score = 2
        - director: {'Wes Archer'}
        - imdb_rating: [8.0]
      
      Episode TheSimpsons_S7_E18: Similarity score = 2
        - director: {'Wes Archer'}
        - imdb_rating: [8.0]
      
      Episode FamilyGuy_S2_E8: Similarity score = 1
        - imdb_rating: [8.0]
3. Find Shortest Path Between Episodes
- The user can find the shortest path between two episodes of interest based on shared attributes
- Prompt: The user will enter the episode IDs of two episodes into the find_shortest_path function from the GraphBuilder class to find the 
  shortest path between the two. If no path exists, the function will indicate that. If a path exists, it will print each step of the path and
  the connection for each step
- Example: 
  graph.find_shortest_path('FamilyGuy_S1_E1', 'FamilyGuy_S6_E5')
      Shortest path from FamilyGuy_S1_E1 to FamilyGuy_S6_E5:
      FamilyGuy_S1_E1 -> FamilyGuy_S5_E5 (Connection: [('imdb_rating', [7.6])])
      FamilyGuy_S5_E5 -> FamilyGuy_S6_E5 (Connection: [('director', {'Greg Colton'}), ('writer', {'Steve Callaghan'})])
4. Find the Most Connected Episode and Visualize the Top 50 Connections
- The user can ask the program to find the episode with the most connections (edges) to others and a visualization
- Prompt: The program will automatically find the most connected episode when the function find_most_connected_episode() is called. 
- Program Response: The program displays the episode with the highest number of connections and visualizes the top 50 most similar episodes based 
  on similarity scores.
- Example: 
  graph.find_most_connected_episode()
    The most connected episode is SouthPark_S16_E3 with 800 connections.
    Connections: 800
    {A visualization will also be in the output}
5. Show Episode Statistics
- The user can get detailed statistics for a specific episode.
- Prompt: Enter the episode ID to get a detailed summary (e.g., Futurama_S6_E2).
- Program Response: The program displays detailed information about the selected episode, such as the show, season, directors, writers, 
  guest stars, air date, viewer count, and IMDb rating.
- Example:
  graph.provide_episode_statistics('Futurama_S6_E2')
     Episode Summary for Futurama_S6_E2:
      - Show: Futurama
      - Season: 6
      - Episode: 2
      - Air Date: June 24, 2010
      - Viewer Count: 2,780,000.00
      - IMDb Rating: 7.2
      - Directors: Dwayne Carey-Hill
      - Writers: Carolyn Premish, Matt Groening
      - Guest Stars: Chris Elliot

Special Instructions:
- CSV File: Ensure the CSV file follows the expected format with the necessary columns. The program does not handle missing or untidy data, 
  so make sure the data is clean.

Required Python Packages:
- pandas: For handling and processing the CSV data.
- matplotlib: For visualizing the top 50 most similar episodes.

Network (Graph) Organization:
- Each node represents an episode of a TV show. The episode_id is a unique identifier for each episode in the format show_S{season}_E{episode} 
  (e.g., TheSimpsons_S2_E4).The attributes of each node is seen below:
      episode: The episode number.
      show: The name of the TV show.
      season: The season number.
      guest_star: A list of guest stars in the episode.
      directors: A list of directors for the episode.
      writers: A list of writers for the episode.
      air_date: The date the episode originally aired.
      viewer_count: The viewer count for the episode.
      air_month: The month the episode aired.
      air_year: The year the episode aired.
      imdb_rating: The IMDb rating of the episode.
      shortened_viewer: A shortened version of the viewer count.

Edges:
- Edges represent the connections between episodes. An edge is created if two episodes share one or more attributes. The edge contains:
    - node1 and node2: The two episodes (nodes) that the edge connects.
    - edge_type: The type of connection (e.g., "similarity").
    - shared_attributes: A list of the attributes that the two episodes share (e.g., guest stars, directors, IMDb ratings).
- The attributes that are assessed to make an edge are:
    - IMDb ratings
    - shortened viewer count
    - air month and air year (together)
    - air date (exact match)
    - writers
    - directors
    - guest stars
- The graph allows traversal between episodes via these edges, enabling the discovery of similar episodes, finding paths, and exploring 
  the most connected episodes.








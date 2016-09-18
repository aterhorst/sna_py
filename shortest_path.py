import matplotlib.pyplot as pp

import seaborn as sns

import numpy as np

# Add a dark background

sns.set_style('dark')

# Initialize figure

fig = pp.figure(figsize = (8, 8))

ax  = fig.add_subplot(1, 1, 1)

# Create force-directed layout for the graph

pos = nx.spring_layout(G)

pos_array = np.array(list(pos.values())).T # Format into a NumPy array

# Define node colors based on in-degree

node_color = np.array([len(G.predecessors(v)) for v in G], dtype=float)

# Define node sizes to be proportional to PageRank values

sizes = 1E4*np.array(list(nx.pagerank(G).values()))

# Plot each edge

for i in G:

    for j in G[i]:

        # Compute in-marker size

        # The next few lines just resize the

        # incoming markers to look decent

        # with the varying node sizes

        p = pos_array[:, j] - pos_array[:, i]

        s = -.04*(1 + .4*np.log(sizes[j]/sizes.min()))

        p = s*p/np.linalg.norm(p) + pos_array[:, j]

        # Plot markers

        ax.plot([pos_array[0, j], p[0]], [pos_array[1, j], p[1]], '-k', alpha = .5, linewidth = 2, zorder = 9)

        #Plot edges

        ax.plot(pos_array[0, [i, j]], pos_array[1, [i, j]], '-w')

# Plot nodes

ax.scatter(pos_array[0], pos_array[1], sizes, color = pp.get_cmap('coolwarm')(node_color/node_color.max()), zorder = 10)

# Remove axis ticks

pp.xticks([])

pp.yticks([])
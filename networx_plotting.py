<<<<<<< HEAD

# -*- coding: utf-8 -*-
"""
Graph visualisation with NetworkX
@author: Andrew Terhorst
"""
import networkx as nx
import matplotlib.style
import pylab

matplotlib.style.use('seaborn-dark')


kp = nx.readwrite.gexf.read_gexf('/Users/aterhorst/ownCloud/Innovation Network Analysis/Case studies/HF/knowledge.provider.net.gexf')
#ekp = nx.readwrite.gexf.read_gexf('/Users/ter053/ownCloud/Innovation Network Analysis/Case studies/HF/explicit.knowledge.net.gexf')
#tkp = nx.readwrite.gexf.read_gexf('/Users/ter053/ownCloud/Innovation Network Analysis/Case studies/HF/tacit.knowledge.net.ge


labels = dict((n,d['vertex.id']) for n,d in kp.nodes(data=True))
broker = dict((n,d['constraint']) for n,d in kp.nodes(data=True))
org = dict((n,d['employer']) for n,d in kp.nodes(data=True))
<<<<<<< HEAD
color = [org.get(node, 0.25) for node in kp.nodes()]
#broker.update((x, 1/y*200) for x, y in broker.items())

pos = nx.spring_layout(kp)

nx.draw(kp, pos, node_size = [1/broker.get(node)*200 for node in kp.nodes()], node_color = color, cmap = 'Set2')

nx.draw_networkx_labels(kp, pos, with_labels = True, labels = labels, font_size= 10);

nx.draw_networkx_edges(kp, pos, width = 0.8, arrows = True, edge_color = 'black')

pylab.savefig('/Users/aterhorst/ownCloud/Innovation Network Analysis/Case studies/HF/kp_net.pdf')


=======

pos = nx.spring_layout(kp)
nx.draw(kp, pos, node_size = [1 / v * 200 for v in broker.values()], node_color = [a for a in org.values()])
nx.draw_networkx_labels(kp, pos, with_labels = True, labels = labels, labelsfont_size= 2);
# pylab.savefig('kp_net.eps')
>>>>>>> 00e624bc46aef8eaf3ae8d265216817b2e1b285a


# -*- coding: utf-8 -*-
"""
Graph visualisation with NetworkX
@author: Andrew Terhorst
"""
import networkx as nx
import matplotlib.style
import pylab
import matplotlib.pyplot as pp

matplotlib.style.use('seaborn-dark')


kp = nx.readwrite.gexf.read_gexf('/Users/aterhorst/ownCloud/Innovation Network Analysis/Case studies/HF/knowledge.provider.net.gexf')
#ekp = nx.readwrite.gexf.read_gexf('/Users/ter053/ownCloud/Innovation Network Analysis/Case studies/HF/explicit.knowledge.net.gexf')
#tkp = nx.readwrite.gexf.read_gexf('/Users/ter053/ownCloud/Innovation Network Analysis/Case studies/HF/tacit.knowledge.net.ge


labels = dict((n,d['vertex.id']) for n,d in kp.nodes(data=True))
broker = dict((n,d['constraint']) for n,d in kp.nodes(data=True))
org = dict((n,d['employer']) for n,d in kp.nodes(data=True))
color = [org.get(node, 0.25) for node in kp.nodes()]

pos = nx.spring_layout(kp)

nx.draw(kp, pos, node_size = [1/broker.get(node)*200 for node in kp.nodes()], node_color = color, cmap = pp.get_cmap('rainbow'))

nx.draw_networkx_labels(kp, pos, with_labels = True, labels = labels, font_size= 10);

nx.draw_networkx_edges(kp, pos, width = 0.8, arrows = True, edge_color = 'black', alpha = 0.6)

pylab.savefig('/Users/aterhorst/ownCloud/Innovation Network Analysis/Case studies/HF/kp_net.pdf')


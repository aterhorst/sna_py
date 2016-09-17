# -*- coding: utf-8 -*-
"""
Graph visualisation with NetworkX

@author: Andrew Terhorst
"""
import networkx as nx
import os
import matplotlib as plt
import seaborn as sns
import numpy as np
from matplotlib.colors import ListedColormap
from pylab import figure
import matplotlib.style

matplotlib.style.use('classic')


import os
os.chdir('/Users/ter053/ownCloud/Python PhD')


kp = nx.readwrite.gexf.read_gexf('/Users/ter053/ownCloud/Innovation Network Analysis/Case studies/HF/knowledge.provider.net.gexf')
ekp = nx.readwrite.gexf.read_gexf('/Users/ter053/ownCloud/Innovation Network Analysis/Case studies/HF/explicit.knowledge.net.gexf')
tkp = nx.readwrite.gexf.read_gexf('/Users/ter053/ownCloud/Innovation Network Analysis/Case studies/HF/tacit.knowledge.net.gexf')



labels = dict((n,d['vertex.id']) for n,d in kp.nodes(data=True))
broker = dict((n,d['constraint']) for n,d in kp.nodes(data=True))
org = dict((n,d['employer']) for n,d in kp.nodes(data=True))

pos = nx.spring_layout(kp)
nx.draw(kp, pos, node_size = [1 / v * 200 for v in broker.values()], node_color = [a for a in org.values()])
nx.draw_networkx_labels(kp, pos, with_labels = True, labels = labels, labelsfont_size= 2);
# pylab.savefig('kp_net.eps')
import sys
import networkx as nx
import matplotlib.pyplot as plt
import community
from collections import OrderedDict
import matplotlib.colors as mpcolors
from collections import defaultdict
import itertools
import operator
import numpy as np




def execute(input,img):
    d={}
    
    
    #fh=open("input.txt", 'rb')
    G=nx.Graph()
    H=nx.Graph()
    data = []
    dat=[]
    v = {}
    for line in open(input):
        dat.append(tuple(line.strip().split(' ')))
    for i in dat:
        data.append(map(int, i))
 

    G.add_edges_from(data)
    H.add_edges_from(data)
#print "G----"
    #print G.nodes()
    comlist=[]
    edgesnum = nx.number_of_edges(G)

    while True:
        if edgesnum!=0:
            #   print "---"
            ncomp = nx.number_connected_components(G)
            d= nx.edge_betweenness_centrality(G)
            sorted_d = sorted(d.items(), key=operator.itemgetter(1),reverse=True)
            # print"\n Number of edges before removal"
            #print nx.number_of_edges(G)
            #print d
            highest = max(d.values())
            remove_edge=[k for k,v in d.items() if v == highest]
            G.remove_edges_from(remove_edge)
            components = nx.connected_components(G)
            l = nx.number_connected_components(G)-1
            component_map = {}
            num=0
            for nodes in components:
                for node in nodes:
                    component_map[int(node)] = num
                num=num+1
        #    print component_map
            edgesnum = nx.number_of_edges(G)
            #    print "TRY 1:"
            if edgesnum!=0:
                comlist.append([community.modularity(component_map,H),component_map])
            print comlist
 
    
    

        else:
            break
    
    dict={}
    maxlist=[]

    if len(comlist)!=0:
        for p in comlist:
            maxlist.append(p[0])
        u=max(maxlist)
        for k,v in comlist:
           if k==u:
               dict=v
        new_dict = {}
        for pair in dict.items():
            if pair[1] not in new_dict.keys():
                new_dict[pair[1]] = []
            new_dict[pair[1]].append(pair[0])
            
            #print final values
        for key,val in new_dict.iteritems():
            print val
        values = [dict.get(node) for node in H.nodes()]
        nx.draw_spring(H, cmap = plt.get_cmap('jet'), node_color =values, node_size=200, with_labels=True)
        plt.draw()
        plt.savefig(img)
    else:
        for i in sorted(G.node):
            print [i]
        values = [component_map.get(node) for node in H.nodes()]
        nx.draw_spring(H, cmap = plt.get_cmap('jet'), node_color =values, node_size=200, with_labels=True)
        plt.draw()
        plt.savefig(img)




if __name__ == "__main__":
    execute(sys.argv[1],sys.argv[2])

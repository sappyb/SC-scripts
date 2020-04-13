import configuration
from datetime import datetime
from pathlib import Path
from makeFile import MakeFileWriter
from random import randint 
import collections

class Netconfwriter(MakeFileWriter):
    
    def __init__(self, topology, speciality, jobName, netgraph, **kwargs):
        self.topology = topology
        self.speciallity = speciality
        self.jobName = jobName
        self.dump = 'nodump'
        self.config = kwargs
        self.netgraph = netgraph

    def getConfs(self, **kwargs):
        print(self.config)
   
    def setConfs(self, **kwargs):
        if kwargs is not None:
            for key, value in kwargs.items():
                newDict = self.changeConf(key, value, self.config)
                self.config = newDict
            
    def changeConf(self, key, value, confDict, **kwargs):
        d = {}
        for k, v in confDict.items():
            if isinstance(v, dict):
                d[k] = self.changeConf(key, value, v)
            else:
                if k == key:
                    d[k] = value
                else:
                    d[k] = v
        return d
    
    def makeString(self, **kwargs): 
        if not self.netgraph:                                                                                   
            self.setConfs(routing_folder='{}/{}'.format(self.config.get('OUTFILE').get('path'), self.jobName))  
        modelNet = self.config['netconfs'][self.topology][self.speciallity]['model-net']                        
        paramsDict = self.config['netconfs'][self.topology][self.speciallity]['params']                         
        params = '\n'.join(('{} = "{}";'.format(*map(str, item))                                                
                      for item in paramsDict.items()))                                                          
        if self.netgraph:                                                                                       
            params = params +'\n' + 'modelnet_order = ( "network_graph", "network_graph_router" );'+'\n'        
        print(params)                                                                                           
        modelNetValue = '\n'.join(('{} = "{}";'.format(*map(str, item)))                                        
                             for item in modelNet.items())                                                      
                                                                                                                
        return ('LPGROUPS{{\nMODELNET_GRP{{\n{}\n}}\n}}\nPARAMS{{\n{}\n}}'                                      
                           .format(modelNetValue, params)) 

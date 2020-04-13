from pathlib import Path
from ruamel.yaml import load, dump, Loader
defaultConfigPath = '/g/g92/bhowmik1/SC-scripts/defaults.yaml'
networkFiles = '/p/lustre1/bhowmik1/Result/networkFiles/dfly'
configs = {}
with open(defaultConfigPath,'r') as defConf:
	configs = load(defConf, Loader = Loader) 
#	print(defaultConfigs)
'''
modelnet = defaultConfigs['netconfs']['fat-tree']['quartz']['model-net']
print(modelnet)
params = defaultConfigs['netconfs']['fat-tree']['quartz']['params']
print(params)
'''
p = '/p/lustre1/bhowmik1/Result'
q = ['netconfs', ]
r = ['dfly']
s = ['1map', '2map', '4map', '8map']
t = ['fcfs', 'rr']
u = ['0.0625x', '0.125x', '0.25x', '0.5x', 'x', '2x', '4x', '8x', '16x'] 
for i in q:
	for j in r:
		for k in s:
			for l in t:
				for m in u:
					folderName = '{}/{}/{}/{}/{}/{}'.format(p, i, j, k, l, m)
					defaultConfigs = configs
					if j == 'ftree':
						modelnet = defaultConfigs['netconfs']['fat-tree']['quartz']['model-net']
						params = defaultConfigs['netconfs']['fat-tree']['quartz']['params']
						mnratio = 1
						if k == '1map':
							mnratio = 1
						elif k == '2map':
							mnratio = 2
						elif k == '4map':
							mnratio = 4
						elif k == '8map':
							mnratio = 8
						modelnet['repetitions'] = 128 // mnratio
						modelnet['server'] = 16 * mnratio
						params['switch_count'] = 128 // mnratio
						params['node_copy_queues'] = 1 * mnratio
						if l == 'fcfs':
							params['modelnet_scheduler'] = 'fcfs'
						elif l == 'rr':
							params['modelnet_scheduler'] = 'round-robin'
						if m == '0.0625x':
							ratio = 0.0625
							params['link_bandwidth'] = 11.9 * ratio
							params['intra_bandwidth'] = 23.8 * ratio
							params['cn_bandwidth'] = 11.9 * ratio
						elif m == '0.125x':
							ratio = 0.125
							params['link_bandwidth'] = 11.9 * ratio
							params['intra_bandwidth'] = 23.8 * ratio
							params['cn_bandwidth'] = 11.9 * ratio
						elif m == '0.25x':
							ratio = 0.25
							params['link_bandwidth'] = 11.9 * ratio
							params['intra_bandwidth'] = 23.8 * ratio
							params['cn_bandwidth'] = 11.9 * ratio
						elif m == '0.5x':
							ratio = 0.5
							params['link_bandwidth'] = 11.9 * ratio
							params['intra_bandwidth'] = 23.8 * ratio
							params['cn_bandwidth'] = 11.9 * ratio
						elif m == 'x':
							ratio = 1
							params['link_bandwidth'] = 11.9 * ratio
							params['intra_bandwidth'] = 23.8 * ratio
							params['cn_bandwidth'] = 11.9 * ratio
						elif m == '2x':
							ratio = 2
							params['link_bandwidth'] = 11.9 * ratio
							params['intra_bandwidth'] = 23.8 * ratio
							params['cn_bandwidth'] = 11.9 * ratio
						elif m == '4x':
							ratio = 4
							params['link_bandwidth'] = 11.9 * ratio
							params['intra_bandwidth'] = 23.8 * ratio
							params['cn_bandwidth'] = 11.9 * ratio
						elif m == '8x':
							ratio = 8
							params['link_bandwidth'] = 11.9 * ratio
							params['intra_bandwidth'] = 23.8 * ratio
							params['cn_bandwidth'] = 11.9 * ratio
						elif m == '16x':
							ratio = 16
							params['link_bandwidth'] = 11.9 * ratio
							params['intra_bandwidth'] = 23.8 * ratio
							params['cn_bandwidth'] = 11.9 * ratio
						paramsFinal = '\n'.join(('{} = "{}";'.format(*map(str, item)) for item in params.items()))
						modelNetValue = '\n'.join(('{} = "{}";'.format(*map(str, item))) for item in modelnet.items())
					elif j == 'dfly':
						modelnet = defaultConfigs['netconfs']['dfly']['quartz']['model-net']
						params = defaultConfigs['netconfs']['dfly']['quartz']['params']
						mnratio = 1
						interFile = ''
						intraFile = ''
						if k == '1map':
							mnratio = 1
							interFile = '{}/1map/inter.bin'.format(networkFiles)
							intraFile = '{}/1map/intra.bin'.format(networkFiles)
						elif k == '2map':
							mnratio = 2
							interFile = '{}/2map/inter.bin'.format(networkFiles)
							intraFile = '{}/2map/intra.bin'.format(networkFiles)
						elif k == '4map':
							mnratio = 4
							interFile = '{}/4map/inter.bin'.format(networkFiles)
							intraFile = '{}/4map/intra.bin'.format(networkFiles)
						elif k == '8map':
							mnratio = 8
							interFile = '{}/8map/inter.bin'.format(networkFiles)
							intraFile = '{}/8map/intra.bin'.format(networkFiles)
						modelnet['repetitions'] = 256 // mnratio
						modelnet['server'] = 8 * mnratio
						params['num_groups'] = (256 // mnratio) // 16
						params['node_copy_queues'] = 1 * mnratio
						params['inter-group-connections'] = interFile
						params['intra-group-connections'] = intraFile
						if l == 'fcfs':
							params['modelnet_scheduler'] = 'fcfs'
						elif l == 'rr':
							params['modelnet_scheduler'] = 'round-robin'
						if m == '0.0625x':
							ratio = 0.0625
							params['local_bandwidth'] = 11.9 * ratio
							params['global_bandwidth'] = 11.9 * ratio
							params['intra_bandwidth'] = 23.8 * ratio
							params['cn_bandwidth'] = 11.9 * ratio
						elif m == '0.125x':
							ratio = 0.125
							params['local_bandwidth'] = 11.9 * ratio
							params['global_bandwidth'] = 11.9 * ratio
							params['intra_bandwidth'] = 23.8 * ratio
							params['cn_bandwidth'] = 11.9 * ratio
						elif m == '0.25x':
							ratio = 0.25
							params['local_bandwidth'] = 11.9 * ratio
							params['global_bandwidth'] = 11.9 * ratio
							params['intra_bandwidth'] = 23.8 * ratio
							params['cn_bandwidth'] = 11.9 * ratio
						elif m == '0.5x':
							ratio = 0.5
							params['local_bandwidth'] = 11.9 * ratio
							params['global_bandwidth'] = 11.9 * ratio
							params['intra_bandwidth'] = 23.8 * ratio
							params['cn_bandwidth'] = 11.9 * ratio			
						elif m == 'x':							
							ratio = 1						
							params['local_bandwidth'] = 11.9 * ratio			
							params['global_bandwidth'] = 11.9 * ratio
							params['intra_bandwidth'] = 23.8 * ratio			
							params['cn_bandwidth'] = 11.9 * ratio			
						elif m == '2x':							
							ratio = 2						
							params['local_bandwidth'] = 11.9 * ratio			
							params['global_bandwidth'] = 11.9 * ratio
							params['intra_bandwidth'] = 23.8 * ratio			
							params['cn_bandwidth'] = 11.9 * ratio			
						elif m == '4x':							
							ratio = 4						
							params['local_bandwidth'] = 11.9 * ratio			
							params['global_bandwidth'] = 11.9 * ratio
							params['intra_bandwidth'] = 23.8 * ratio			
							params['cn_bandwidth'] = 11.9 * ratio			
						elif m == '8x':							
							ratio = 8						
							params['local_bandwidth'] = 11.9 * ratio			
							params['global_bandwidth'] = 11.9 * ratio
							params['intra_bandwidth'] = 23.8 * ratio			
							params['cn_bandwidth'] = 11.9 * ratio			
						elif m == '16x':						
							ratio = 16						
							params['local_bandwidth'] = 11.9 * ratio			
							params['global_bandwidth'] = 11.9 * ratio
							params['intra_bandwidth'] = 23.8 * ratio			
							params['cn_bandwidth'] = 11.9 * ratio
						paramsFinal = '\n'.join(('{} = "{}";'.format(*map(str, item)) for item in params.items()))
						modelNetValue = '\n'.join(('{} = "{}";'.format(*map(str, item))) for item in modelnet.items())

						paramsFinal = paramsFinal +'\n' + 'modelnet_order = ("dragonfly_custom","dragonfly_custom_router");'+'\n'
					print(folderName)
					print('LPGROUPS{{\nMODELNET_GRP{{\n{}\n}}\n}}\nPARAMS{{\n{}\n}}'.format(modelNetValue, paramsFinal))				
					fileName = str(Path(folderName,'conf'))
					with open(fileName, 'w') as fp:
						fp.write('LPGROUPS{{\nMODELNET_GRP{{\n{}\n}}\n}}\nPARAMS{{\n{}\n}}'.format(modelNetValue, paramsFinal))

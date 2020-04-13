from pathlib import Path
p = '/p/lustre1/bhowmik1/Result'
q = ['netconfs', 'outdirs', 'outputs', 'workloads']
r = ['dfly', 'ftree']
s = ['1map', '2map', '4map', '8map']
t = ['fcfs', 'rr']
u = ['0.0625x', '0.125x', '0.25x', '0.5x', 'x', '2x', '4x', '8x', '16x'] 
for i in q:
	for j in r:
		for k in s:
			for l in t:
				for m in u:
					folderName = '{}/{}/{}/{}/{}/{}'.format(p, i, j, k, l, m)                                         
					dirPath = Path(folderName)                                                                  
					dirPath.mkdir(parents=True, exist_ok=True)                                                  

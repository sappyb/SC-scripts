from pathlib import Path
p = '/p/lustre1/bhowmik1/Result'
q = ['workload_1', 'workload_2', 'workload_3']
r = ['dfly']
s = ['1map', '2map', '4map', '8map']
t = ['fcfs', 'rr']
u = ['0.0625x', '0.125x', '0.25x', '0.5x', 'x', '2x', '4x', '8x', '16x'] 
strHead = '#!/bin/bash\n'+ '#MSUB -l nodes=1\n'+ '#MSUB -l walltime=23:59:00\n'+ '#MSUB -q pbatch\n'+ '#MSUB -A hpcsim\n'+ '#MSUB -o /p/lustre1/bhowmik1/output-dragonfly.log\n'
rmList = []
command = []
for i in q:
	for j in r:
		for k in s:
			for l in t:
				for m in u:
					netconf = '{}/{}/{}/{}/{}/{}/conf'.format(p, 'netconfs', j, k, l, m)
					outfile="{}/{}/{}/{}/{}/{}/out.{}.all".format(p, 'outputs', j, k, l, m, i)
					outdir="{}/{}/{}/{}/{}/{}/counters.{}.job.all".format(p, 'outputs', j, k, l, m, i)
					rmList.append('rm -rf {} {}\n'.format(outdir, outfile))
					config_name="{}/workloads/{}.all".format(p, i)
					command.append('srun -N1 -n1 /g/g92/bhowmik1/installCatalystDfly/TraceR/tracer/traceR --sync=1 --nkp=256 --extramem=1000000 --max-opt-lookahead=1000000 --avl-size=21 --lp-io-dir={}  -- {} {} > {} &\n'.format(outdir, netconf, config_name, outfile))
#for i in rmList:
#	print(i)
chunks = [command[x:x+1] for x in range(0, len(command), 1)]
for i, j in enumerate(chunks):
	print('msub Job_{};'.format(i))
	with open('Job_{}'.format(i), 'w') as fp: 
		fp.write(strHead)
		for cmd in j:
			fp.write(cmd)
		fp.write('wait\n')

#print(len(command))

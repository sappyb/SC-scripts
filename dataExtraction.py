import re
import pandas as pd
p = '/p/lustre1/bhowmik1/Result'
'''
q = ['workload_1', 'workload_2', 'workload_3']
r = ['dfly', 'ftree']
s = ['1map', '2map', '4map', '8map']
t = ['fcfs', 'rr']
u = ['0.0625x', '0.125x', '0.25x', '0.5x', 'x', '2x', '4x', '8x', '16x'] 
'''
q = ['workload_1']
r = ['ftree']
s = ['1map']
t = ['fcfs']
u = ['0.0625x', '0.125x'] 
regex_time = re.compile('Job (\d+) Time (\d+.\d+) s')
regex_name = re.compile('Job (\d+) - ranks (\d+), trace folder [^\n]*/(\w+(?:-\w+)*)/(\d+)/traces.otf2, [^\n]* iters (\d+)')
workload_1_list = []
workload_2_list = []
workload_3_list = []
column_1 = []
column_2 = []
column_3 = []
for j in r:
    for k in s:
        for l in t:
            for m in u:
                jobDict = {}
                for i in q:
                    jobs = []
                    jobTime = []
                    outfile="{}/{}/{}/{}/{}/{}/out.{}.all".format(p, 'outputs', j, k, l, m, i)
                    fullDesc="{}/{}/{}/{}/{}/{}/{}".format(p, 'outputs', j, k, l, m, i)
                    print(outfile)
                    with open(outfile,'r') as fp:
                        for line in fp.readlines():
                            h = regex_name.findall(line)
                            ij = regex_time.findall(line)
                            job = ''
                            if h:
                                job = h[0][2] + h[0][1]
                                jobs.append(job)
                            if ij:
                                jobTime.append(ij[0][1])
#                            if job != '':
#                                if jobDict.get(job) == None:
#                                    jobDict[job] = int(ij[0][1])
#                            else:
#                                jobDict[job] = (jobDict[job] + int(ij[0][1]))/2
                    if i == 'workload_1':
                        fullList = []
                        fullList.append(fullDesc)
                        for pq, rs in zip(jobs, jobTime):
                            fullList.append(rs) 
                        workload_1_list.append(fullList)
                    elif i == 'workload_2':
                        workload_2_list.append([fullDesc, jobs, jobTime])
                    elif i == 'workload_3':
                        workload_3_list.append([fullDesc, jobs, jobTime])
dfObj = pd.DataFrame(workload_1_list)
print(dfObj)
print(workload_1_list)

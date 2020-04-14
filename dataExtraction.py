import re
import pandas as pd
p = '/p/lustre1/bhowmik1/Result'
q = ['workload_1', 'workload_2', 'workload_3']
r = ['dfly', 'ftree']
s = ['1map', '2map', '4map', '8map']
t = ['fcfs', 'rr']
u = ['0.0625x', '0.125x', '0.25x', '0.5x', 'x', '2x', '4x', '8x', '16x'] 
'''
q = ['workload_1', 'workload_2']
r = ['ftree']
s = ['1map']
t = ['fcfs']
u = ['0.0625x', '0.125x'] 
'''
regex_time = re.compile('Job (\d+) Time (\d+.\d+) s')
regex_name = re.compile('Job (\d+) - ranks (\d+), trace folder [^\n]*/(\w+(?:-\w+)*)/(\d+)/traces.otf2, [^\n]* iters (\d+)')
workload_1_list = []
workload_2_list = []
workload_3_list = []
column_1 = ['Location']
column_2 = ['Location']
column_3 = ['Location']
c_1 = 0
c_2 = 0
c_3 = 0
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
                                job = h[0][2] + '_' +h[0][1]
                                jobs.append(job)
                            if ij:
                                jobTime.append(ij[0][1])
                    if i == 'workload_1':
                        fullList = []
                        fullList.append(fullDesc)
                        for pq, rs in zip(jobs, jobTime):
                            if c_1 == 0:
                                column_1.append(pq)
                            fullList.append(rs) 
                        c_1 = 1
                        workload_1_list.append(fullList)
                    elif i == 'workload_2':
                        fullList = []
                        fullList.append(fullDesc)
                        for pq, rs in zip(jobs, jobTime):
                            if c_2 == 0:
                                column_2.append(pq)
                            fullList.append(rs) 
                        c_2 = 1
                        workload_2_list.append(fullList)
                    elif i == 'workload_3':
                        fullList = []
                        fullList.append(fullDesc)
                        for pq, rs in zip(jobs, jobTime):
                            if c_3 == 0:
                                column_3.append(pq)
                            fullList.append(rs) 
                        c_3 = 1
                        workload_3_list.append(fullList)
df_1 = pd.DataFrame(workload_1_list, columns = column_1)
df_2 = pd.DataFrame(workload_2_list, columns = column_2)
df_3 = pd.DataFrame(workload_3_list, columns = column_3)
df_1[['i','p','lustre1','bhowmik1','Result','outputs','Topology','Mapping','Scheduling','Bandwidth','workload']] = df_1.Location.apply( lambda x: pd.Series(str(x).split("/")))
df_1.drop(['Location','i','p','lustre1','bhowmik1','Result','outputs'], axis=1, inplace=True)
df_2[['i','p','lustre1','bhowmik1','Result','outputs','Topology','Mapping','Scheduling','Bandwidth','workload']] = df_2.Location.apply( lambda x: pd.Series(str(x).split("/")))
df_2.drop(['Location','i','p','lustre1','bhowmik1','Result','outputs'], axis=1, inplace=True)
df_3[['i','p','lustre1','bhowmik1','Result','outputs','Topology','Mapping','Scheduling','Bandwidth','workload']] = df_3.Location.apply( lambda x: pd.Series(str(x).split("/")))
df_3.drop(['Location','i','p','lustre1','bhowmik1','Result','outputs'], axis=1, inplace=True)

print(df_1)
print(df_2)
print(df_3)

df_1.to_csv('workload-1.csv')
df_2.to_csv('workload-2.csv')
df_3.to_csv('workload-3.csv')
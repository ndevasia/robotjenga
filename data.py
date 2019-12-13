import matplotlib.pyplot as plt 

avg ={1: (3.78, 5.60), \
2: (4.21, 4.08),
3: (3.08, 3.71), 
4: (2.69, 5.20),
5: (1.73, 5.84), 
6: (1.86, 4.64), 
7: (2.86, 2.84), 
8: (4.30, 6.32), 
9: (3.91, 4.72), 
10: (2.86, 4.36), 
11: (2.72, 3.63), 
12: (3.61, 5.17)}
print(avg)

a_towers = [i for i in avg.keys()]
a_block = [avg[i][0] for i in a_towers]
a_dist = [avg[i][1] for i in a_towers]
plt.stem(a_towers, a_block)
plt.show()
plt.stem(a_towers, a_dist)
plt.show()

mode = {1: (5, 10), 
2: (5, 2, 4),
3: (4, 5), 
4: (3, 5), 
5: (2, 5), 
6: (2, 3, 6),
7: (4, 3), 
8: (5, 5), 
9: (5, 5),
10: (4, 3, 5), 
11: (1, 3), 
12: (3, 4, 5)}

m_towers = [i for i in mode.keys()]
m_block = [avg[i][0] for i in m_towers]
m_dist = [avg[i][1] for i in m_towers]

plt.stem(m_towers, m_block, color = 'red')
plt.show()
plt.stem(m_towers, m_dist)
plt.show()

#print(mode)

#plt.plot(avg.keys, avg.values)
import matplotlib.pyplot as plt
data=[5,15,25,35,15,55]
plt.hist(data, bins=[0,10,20,30,40,50,60],facecolor='y' , edgecolor='red')
plt.xlabel('values')
plt.title('frequency')
plt.savefig('student.png')
plt.show()
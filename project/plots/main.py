import pandas
from matplotlib import pyplot as plt

plt.plot([0, 5, 10, 20,50,100,150,200],[74.83,76.93,75.30,75.5,64.93,46.61,25.37,14.64], label="first plot")
plt.xlabel("PERCENTAGE of POSITIVE INCR FIRING THRESH")
plt.ylabel("AVG ACC of CLASSIFICATION(TRAINING DATA)")
plt.show()

f = plt.figure(figsize=(15,10))
plt.plot([0, 5, 10, 20,50,100,150,200],[74.83,74.71,75.72,75.67,75.7,74.66,73.54,76.41], label="first plot")
#plt.axis
plt.xlabel("PERCENTAGE of NEGATIVE INCR FIRING THRESH")
plt.ylabel("AVG ACC of CLASSIFICATION(TRAINING DATA)")
plt.xlim(0, 200)
plt.ylim(70,80)

plt.show()
plt.plot([0,5,10,20,50,100,150,200],[88.0,87.0,85.0,88.0,82.0,68.0,49.0,32.0])
plt.xlabel("PERCENTAGE of POSITIVE INCR FIRING THRESH")
plt.ylabel("AVG ACC of CLASSIFICATION(TESTING DATA)")
plt.show()
plt.plot([0,5,10,20,50,100,150,200],[88,85,88,87,88,86,82,85])
plt.xlabel("PERCENTAGE of NEGATIVE INCR FIRING THRESH")
plt.ylabel("AVG ACC of CLASSIFICATION(TESTING DATA)")
plt.show()
plt.plot([1e6,1e5,1e4,1e3,1e2],[73.69,56.33,22.91,14.67,16.88])
plt.xlabel("PERCENTAGE of NEGATIVE DECR SPIKE TIMING")
plt.ylabel("AVG ACC of CLASSIFICATION(TRAINING DATA)")
plt.show()
plt.plot([1e6,1e5,1e4,1e3,1e2],[76,47,13,16,26])
plt.xlabel("PERCENTAGE of NEGATIVE DECR SPIKE TIMING")
plt.ylabel("AVG ACC of CLASSIFICATION(TEST DATA)")
plt.show()
plt.plot([1e8,1e9,1e10,1e11,1e12],[60.37,60.37,60.37,60.37,60.37])
plt.xlabel("PERCENTAGE of POSITIVE INCR SPIKE TIMING")
plt.ylabel("AVG ACC of CLASSIFICATION(TRAINING DATA)")
plt.show()
plt.plot([1e8,1e9,1e10,1e11,1e12],[79,79,79,79,79])
plt.xlabel("PERCENTAGE of POSITIVE INCR SPIKE TIMING")
plt.ylabel("AVG ACC of CLASSIFICATION(TEST DATA)")
plt.show()





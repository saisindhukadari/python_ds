import matplotlib.pyplot as plt
#line chart
#plt.plot([1,2,3],[2,4,6])
#plt.ylabel("Y-axis")
#plt.grid(True)
#plt.title("Line plot chart")
#plt.show()

#bar chart
#label=["A","B","C","D","E"]
#sales=[100,200,600,1500,1200]
#plt.bar(label,sales,color="red")
#plt.title("Sales report")
#plt.ylabel("Values of sales")
#plt.xlabel("Brands")
#plt.show()

#pie chart
#labels=["A","B","C"]
#sizes=[120,100,150]
#plt.pie(sizes,labels=labels,autopct="%1.1f%%",startangle=90)
#plt.title("Product pie report")
#plt.show()

#histogram
gender=['m','f','m','f','f']
plt.hist(gender,bins=2,color="pink",edgecolor="green")
plt.title("Gender report")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()
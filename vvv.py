importmatplotlib.pyplotasplt
x=[2018,2019,2020,2021,2022]
sales=[200,250,300,280,350]
#Correctvisualization
plt.plot(x,sales,color='blue',marker='o', linestyle='-')
plt.title("SalesGrowthOverYears")
plt.xlabel("Year")
plt.ylabel("Sales(inunits)")
plt.grid(True)
plt.show()
#Misleadingexample:truncatedy-axis
plt.plot(x,sales,color='red',marker='o')
plt.title("MisleadingSalesGrowth")
plt.ylim(250,360)
plt.show()
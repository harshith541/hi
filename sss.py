importmatplotlib.pyplotasplt
x=[1,2,3,4,5]
y=[2,4,5,7,10]
plt.plot(x,y,marker='o',color='teal', linewidth=2)
plt.title("SalesGrowthOver5Years")
plt.xlabel("Year")
plt.ylabel("Sales(inlakhs)")
plt.legend(["Sales"], loc='upperleft')
plt.annotate("HighestGrowth",xy=(5,10),xytext=(3.5,9),
arrowprops=dict(facecolor='black',arrowstyle='->'))
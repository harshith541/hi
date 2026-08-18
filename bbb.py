importmatplotlib.pyplotasplt
importnumpyasnp
x=np.arange(1,6)
y=np.array([10,15,12,18,20])
plt.figure(figsize=(8,5))
plt.plot(x,y,color='blue',marker='o', linestyle='-', linewidth=2)
plt.title("LinePlot-TrendoverCategories")
plt.show()
plt.figure(figsize=(8,5))
plt.bar(x,y,color='orange')
plt.title("BarPlot-ComparisonacrossCategories")
plt.show()
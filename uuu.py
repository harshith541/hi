importseabornassns
importmatplotlib.pyplotasplt
tips=sns.load_dataset("tips")
sns.set_palette("pastel")
sns.barplot(x="day",y="total_bill",data=tips)
plt.title("TotalBillbyDaywithPastelPalette")
plt.show()
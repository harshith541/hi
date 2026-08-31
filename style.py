importmatplotlib.pyplotasplt
importnumpyasnp
#Applyingastylesheet
plt.style.use('seaborn-v0_8-darkgrid')
#ConfiguringglobalsettingsviarcParams
plt.rcParams['figure.figsize']=[8,5]
plt.rcParams['axes.titlesize']=16
plt.rcParams['axes.labelsize']=14
plt.rcParams['lines.linewidth']=2.5
x=np.linspace(0,10,100)
y1=np.sin(x)
y2=np.cos(x)
plt.plot(x,y1, label='Sine',color='teal')
plt.plot(x,y2, label='Cosine',color='crimson')
plt.title ("SineandCosineWaveswithCustomStyle")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

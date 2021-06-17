import xarray as xr   
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap

def plotFunc(var, lat, lon):
    minlat = np.min(lat)
    minlon = np.min(lon)
    maxlat = np.max(lat)
    maxlon = np.max(lon)
    map = Basemap(projection='cyl',llcrnrlat=minlat,llcrnrlon=minlon,urcrnrlat=maxlat,urcrnrlon=maxlon,resolution='c')
    map.drawcoastlines()
    map.drawcountries()
    lons,lats=np.meshgrid(lon,lat)
    x,y = map(lons,lats)
    precip = map.contourf(x,y,var,30,cmap=cm.viridis_r)# , vmin=0,vmax=32)
    #  ticks = [0,5,10,15,20,25,30]
    cb = map.colorbar(precip,"right",size="5%")#,ticks=ticks)
    return

def makeFig(ds_list, scenList, varList):
    N = len(scenList)
    if N>4:
        print("Can't be more than 4 datasets in ds_list")
        return
    fig = plt.figure(1)
    for n in range(0,N,1):
        varName = varList[n]
        scen = scenList[n]
        ds = ds_list[n]
        var = ds[varName]
        unit = var.attrs["units"]
        if N==0:
            ax1 = fig.add_subplot(1,1,1)
            ax1.set_title(varName +", "+scen + " " + "["+unit+"]")
        elif N==1:
            ax1 = fig.add_subplot(1,2,n+1)
            ax1.set_title(varName +", "+scen + " " + "["+unit+"]")
        elif N==2:
            ax1 = fig.add_subplot(2,2,n+1)
            ax1.set_title(varName +", "+scen + " " + "["+unit+"]")
        else: #N=3
            ax1 = fig.add_subplot(2,2,n+1)
            ax1.set_title(varName +", "+scen + " " + "["+unit+"]")
        var = var[0,:,:]
        var = var
        lat = ds["lat"]
        lon = ds["lon"]
        plotFunc(var,lat,lon)

    fig.tight_layout()
    fig.subplots_adjust(hspace=None)
    fig.set_figheight(5)
    fig.set_figwidth(10)
    fig.savefig("PlotNew.png")
    
    return

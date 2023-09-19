#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import arcpy
import geopandas as gpd
import rasterio
import pandas as pd
import numpy as np
from permetrics.regression import RegressionMetric
#اگر داده کیفی بود بجای خط بالا اینو ایمپورت کن !!
#طبیعتا فرمول هاش تغیییر میکنه شاید بعذا اینو نوشتم
#from permetrics.classification import ClassificationMetrica


# In[ ]:


def interpolation(interpolation_type, df,field, method, zone, workspace , raster_address, x ,y ):
    epsg=32600+int(zone)
    shp_address=rf"{workspace}\temp.shp"

    for i, row in df.iterrows():
        
        # Drop the current row
        df_subset = df.drop(i)
        
        gdf = gpd.GeoDataFrame(df_subset, geometry=gpd.points_from_xy(df_subset[x], df_subset[y]))
        gdf.set_crs(epsg=epsg, inplace=True)

        gdf.to_file(filename=shp_address, driver="ESRI Shapefile", encoding="utf-8")
        
        if interpolation_type == "Idw":
            out_raster = arcpy.sa.Idw(shp_address, field,method)       
        elif interpolation_type == "Kriging":
            out_raster = arcpy.sa.Kriging(shp_address,method,field)
        elif interpolation_type == "Spline":
            out_raster = arcpy.sa.Spline(shp_address,field,spline_type=method,)
        else :
            return None                                 

        out_raster.save(raster_address)  
        
        with rasterio.open(raster_address) as src:
            lon, lan = src.index(row[x], row[y])
            value = src.read(1)
        
        # Add the interpolated value to the DataFrame
        col = f"{interpolation_type}_{method}_{field}"
        df.at[i, col] = value[lon, lan]
        
    return df



# In[ ]:


def Evalute(method,df,field,interpolation_columns_name) :
    observed_values=list(df[field])
    res_dict={}
    for i,col in enumerate(interpolation_columns_name):
        interpolated_values = list(df[col])
        evaluator = RegressionMetric(observed_values, interpolated_values)
        if method=="MBE":
            res=evaluator.mean_bias_error()
            res_dict[i] =[col,res]  
        elif method=="RMSE":
            res=evaluator.root_mean_squared_error()
            res_dict[i] = [col,res]
        elif method=="MAPE":
            res=evaluator.mean_percentage_error()
            res_dict[i] =[col,res]
        elif method=="R":
            res=evaluator.pearson_correlation_coefficient()
            res_dict[i] = [col,res]
        else :
            return None
    df_out=pd.DataFrame(res_dict,index=['method',f'Evalute_{method}']).transpose()
    return df_out
    


# In[ ]:


workspace= input("Insert your path: ")
gdb_name= "interpolation"
arcpy.env.overwriteOutput=True
#arcpy.CreateFileGDB_management(workspace,gdb_name)
workspace_gdb=rf"{workspace}/{gdb_name}.gdb"

arcpy.env.workspace=workspace_gdb

address_input=input('insert your excel file : ')
df=pd.read_excel(address_input)
zone=input("insert your UTM Zone ? ")
raster_address=r"C:\temp.tif"


# In[ ]:


address_model=input('insert your model file : ')
df_model=pd.read_excel(address_model)


# In[ ]:


count=False
for i, row in df_model.iterrows():
    #Idw=[1,2,3,4,5]
    #Kriging=["Spherical","Circular","Exponential","Gaussian","Linear","LinearDrift","QuadraticDrift"]
    #Spline=["REGULARIZED","TENSION"]
    
    program=input("y/n")
    if program=="n":
        break
    elif program=="y":
        interpolation_type=row["model"]
        method=row["method"]
        field=row["field"]

    x=df.columns[1];y=df.columns[2]
    
    df_final = interpolation(interpolation_type, df, field, method,zone,workspace,raster_address,x,y)
    count=True

if count :
    final_Excel=input("insert your df excel path")    
    df_final.to_excel(final_Excel,index=False)


# In[ ]:


#Evalute 
start_column=4
interpolation_columns = list(df_final.columns[start_column:])
    
MBE=Evalute("MBE",df_final,field,interpolation_columns)
RMSE=Evalute("RMSE",df_final,field,interpolation_columns)
R=Evalute("R",df_final,field,interpolation_columns)
MAPE=Evalute("MAPE",df_final,field,interpolation_columns)

df_eval=pd.DataFrame(interpolation_columns)
df_eval=df_eval.rename(columns={0:"method"})

dfs=[RMSE,MBE,R,MAPE]

for df in dfs :
    df_eval=df_eval.merge(df,on="method",how="right") 

evalute_Excel=input("insert your df ecxel path") 
df_eval.to_excel(evalute_Excel,index=False)


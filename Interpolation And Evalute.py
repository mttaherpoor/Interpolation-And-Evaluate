import arcpy
import geopandas as gpd
import rasterio
import pandas as pd
import numpy as np
from permetrics.regression import RegressionMetric
#اگر داده کیفی بود بجای خط بالا اینو ایمپورت کن !!
#طبیعتا فرمول هاش تغیییر میکنه شاید باید ایینو نوشتم
#from permetrics.classification import ClassificationMetric

def interpolation(interpolation_type, df, z_field, method, cell_size, temp_address, raster_output):
    for i, row in df.iterrows():
        # Drop the current row
        df_subset = df.drop(i)
    
        gdf = gpd.GeoDataFrame(df_subset, geometry=gpd.points_from_xy(df_subset["X_UTM"], df_subset["Y_UTM"]))
        gdf.set_crs(epsg=32639, inplace=True)
    
        gdf.to_file(filename=temp_address, driver="ESRI Shapefile", encoding="utf-8")
        
        if interpolation_type == "Idw":
            out_raster = arcpy.sa.Idw(temp_address,z_field,method,cell_size)
        elif interpolation_type == "Kriging":
            out_raster = arcpy.sa.Kriging(temp_address, z_field, method,cell_size)
        elif interpolation_type == "Spline":
            out_raster = arcpy.sa.Spline(temp_address,z_field, method,cell_size)
        else :
            return None
                                          
        out_raster.save(raster_output)   
        with rasterio.open(raster_output) as src:
            # Get the pixel coordinates of X_UTM and Y_UTM values
            pixel_coords = src.index(row["X_UTM"], row["Y_UTM"])
        
            # Read the raster value at the pixel coordinates
            value = src.read(1, window=((pixel_coords[0], pixel_coords[0] + 1), (pixel_coords[1], pixel_coords[1] + 1)))
    
        # Set the interpolated value in the DataFrame
        col = f"{interpolation_type}_{method}_{z_field}"
        df.at[i, col] = value[0, 0]
    
    return df
# df should be a pandas DataFrame with X_UTM and Y_UTM columns
# Make sure the file paths are correct

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
    

address_excel=input("insert your excel file")
df=pd.read_excel(address_excel)
interpolation_type=input("name your interpolation type :[Idw,Kriging,Spline]")
z_field=input("name your field") 
method=input("name your method of interpolation type ")
cell_size=input("name your cell_size")
temp_address=input("insert your temp address for temp.shp")
raster_output=input("insert your temp address for temp.tif")
df = interpolation(interpolation_type, df, field, method, cell_size,temp_address,raster_output)
interpolation_columns = list(df.columns[6:])
MBE=Evalute("MBE",df,"Mean_AQI",interpolation_columns)
RMSE=Evalute("RMSE",df,"Mean_AQI",interpolation_columns)
R=Evalute("R",df,"Mean_AQI",interpolation_columns)
MAPE=Evalute("MAPE",df,"Mean_AQI",interpolation_columns)

df_final=pd.DataFrame(interpolation_columns)
df_final=df_final.rename(columns={0:"method"})
dfs=[RMSE,MBE,R,MAPE]
for df in dfs :
    df_final=df_final.merge(df,on="method",how="right") 

df_final
Evalute_Excel=r"E:\university\Master\research\polution\polution LAYER\Tehran\Tehran.gdb\Evalute.xlsx"    
df_final.to_excel(Evalute_Excel,index=False)

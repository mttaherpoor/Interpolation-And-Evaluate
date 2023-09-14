# Interpolation And Evalute

## فهرست :
-  [هدف](#هدف)

- [نصب کتابخونه ها](#نصب-کتابخونه-ها)

    -[ نصب pandas](#نصب-pandas)

    -[ نصب arcpy](#نصب-arcpy)

    -[ نصب geopandas](#نصب-geopandas)

     -[ نصب rasterio](#نصب-rasterio)

     -[ نصب permetrics](#نصب-permetric)


- [ویژگی کتابخونه ها](#ویژگی-کتابخونه-ها)

     -[ توابع pandas](#توابع-pandas)

     -[ توابع arcpy](#توابع-arcpy)

     -[ توابع geopandas](#توابع-geopandas)

     -[ توابع rasterio](#توابع-rasterio)

     -[ توابع permetrics](#توابع-permetrics)

- [مثال](#مثال)

- [قدرانی](#قدرانی)

### هدف
هدف از این کد این است که برای داده های کمی و پیشبینی سایر محدوده در GIS بهترین نوع روش میان بابی را پیدا کرده و بتوان آن روش ها مورد مورد ارزیابی قرار بدهیم مانند RSME ,R , MABE , MAPE و ... 

### نصب کتابخونه ها
#### نصب  pandas
این کتابخونه بصورت پیش فرض وجود دارد 
در کد با نام **pd** شناخته می‌شود.
#### نصب arcpy
اگر یکی از نرم افزار های Arcmap , Arcgis Pro  نصب باشد بصورت پیش فرض نصب است .

#### نصب geopandas

0. نصب آناکوندا

1. تمام env هایی که clone کردید ر۱ از طریق package manager آناکوندا یا ArcGISPro پاک کنید. 

2. محیط prompt کوندا ArcGIS را از آدرس زیر باز کنید. 

***C:\Program Files\ArcGIS\Pro\bin\Python\Scripts\proenv.bat***

3. با دستور زیر از `arcgispro-py3` کلون بگیرید.

`conda create --name gisenv --clone arcgispro-py3`

نکته: به جای gisenv هر اسمی برای محیط می‌توانید قرار دهید

4. با دستور زیر محیط ساخته شده در مرحله ۳ را فعال کنید:

`activate gisenv`

5. با دستور زیر geopandas و بسته‌های مورد نیازش را نصب کنید:
```
pip install geopandas 

pip install folium

pip install matplotlib 

pip install mapclassify
```
#### نصب rasterio
0. نصب آناکوندا

1. تمام env هایی که clone کردید ر۱ از طریق package manager آناکوندا یا ArcGISPro پاک کنید. 

2. محیط prompt کوندا ArcGIS را از آدرس زیر باز کنید. 

***C:\Program Files\ArcGIS\Pro\bin\Python\Scripts\proenv.bat***

3. با دستور زیر از `arcgispro-py3` کلون بگیرید.

`conda create --name gisenv --clone arcgispro-py3`

نکته: به جای gisenv هر اسمی برای محیط می‌توانید قرار دهید

4. با دستور زیر محیط ساخته شده در مرحله ۳ را فعال کنید:

`activate gisenv`

5. 5. با دستور زیر rasterio را نصب کنید:
```
pip install rasterio 
```

#### نصب permetrics
0. نصب آناکوندا

1. تمام env هایی که clone کردید ر۱ از طریق package manager آناکوندا یا ArcGISPro پاک کنید. 

2. محیط prompt کوندا ArcGIS را از آدرس زیر باز کنید. 

***C:\Program Files\ArcGIS\Pro\bin\Python\Scripts\proenv.bat***

3. با دستور زیر از `arcgispro-py3` کلون بگیرید.

`conda create --name gisenv --clone arcgispro-py3`

نکته: به جای gisenv هر اسمی برای محیط می‌توانید قرار دهید

4. با دستور زیر محیط ساخته شده در مرحله ۳ را فعال کنید:

`activate gisenv`

5. با دستور زیر permetrics را نصب کنید:
```
git clone https://github.com/thieu1995/permetrics.git
cd permetrics
python setup.py install
```

### ویژگی کتابخونه ها

#### توابع  pandas
[ گیت هاب  pandas](https://github.com/pandas-dev/pandas)

[ سایت   pandas](https://pandas.pydata.org)

|اسم تابع|اسم ورودی ها|نوع خروجی|لینک|
|----|----------|-------------|---------|
|read_excel|ExcelFile , Sheet Name|DataFrame|[لینک](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)|
|iterrows|none|row in DataFrame|[لینک](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html#pandas.DataFrame.iterrows)|
|drop|labels , axis|DataFrame or None|[لینک](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html#pandas.DataFrame.drop)|
|at|row,column|everthing|[لینک](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.at.html#pandas.DataFrame.at)|
|DataFrame|data , index| Dataframe|[لینک](https://pandas.pydata.org/docs/reference/frame.html#dataframe)|
|columns|origin , Destination|object|[لینک](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.columns.html#pandas.DataFrame.columns)|
|rename|Dictionary|DataFrame|[لینک](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html#pandas.DataFrame.rename)|
|merge|DataFrame,on,how|DataFrame|[لینک](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html#pandas.DataFrame.merge)|
|to_excel|ExcelFile,index|Excel|[لینک](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html#pandas.DataFrame.to_excel)|


#### توابع arcpy
[ گیت هاب  arcpy](https://github.com/arcpy)

[ سایت   arcpy](https://pro.arcgis.com/en/pro-app/latest/tool-reference)

|اسم تابع|اسم ورودی ها|نوع خروجی|لینک|
|----|----------|-------------|---------|
|sa.Idw|Shapefile or feature class , z_field , method , cell_size|Raster|[لینک](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/idw.htm)|
|sa.Kriging|Shapefile or feature class , z_field , method , cell_size|Raster|[لینک](https://pro.arcgis.com/en/pro-app/3.1/tool-reference/spatial-analyst/kriging.htm)|
|sa.Spline|Shapefile or feature class , z_field , method , cell_size|Raster|[لینک](https://pro.arcgis.com/en/pro-app/3.1/tool-reference/spatial-analyst/spline.htm)|

#### توابع geopandas
[ گیت هاب  geopandas](https://github.com/geopandas)

[ سایت   geopandas](https://geopandas.org/en/stable/)

|اسم تابع|اسم ورودی ها|نوع خروجی|لینک|
|----|----------|-------------|---------|
|GeoDataFrame|data , geometry|GeoDataFrame|[لینک](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.html#geopandas.GeoDataFrame)|
|points_from_xy|Longitude , Latitude|Point|[لینک](https://geopandas.org/en/stable/gallery/create_geopandas_from_pandas.html)|
|set_crs|epsg , inplace|Int|[لینک](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.set_crs.html)|
|to_file|filename,driver,encoding|everthing|[لینک](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.to_file.html#geopandas.GeoDataFrame.to_file)|


#### توابع rasterio
[ گیت هاب  rasterio](https://github.com/rasterio)

[ سایت   rasterio](https://rasterio.readthedocs.io/en/stable/)

|اسم تابع|اسم ورودی ها|نوع خروجی|لینک|
|----|----------|-------------|---------|
|open|Raster|file|[لینک](https://rasterio.readthedocs.io/en/stable/quickstart.html#opening-a-dataset-in-reading-mode)|
|index|Longitude , Latitude|tuple|[لینک](https://rasterio.readthedocs.io/en/stable/quickstart.html#spatial-indexing)|
|read|1 , window|array|[لینک](https://rasterio.readthedocs.io/en/stable/topics/reading.html)|

#### توابع permetrics
[ گیت هاب  permetrics](https://github.com/thieu1995/permetrics)

[ سایت   permetrics](https://permetrics.readthedocs.io/)

|اسم تابع|اسم ورودی ها|نوع خروجی|لینک|
|----|----------|-------------|---------|
|RegressionMetric|y_true , y_pred |RegressionMetric|[لینک](https://rasterio.readthedocs.io/en/stable/quickstart.html#opening-a-dataset-in-reading-mode)|
|mean_bias_error|None|double|[لینک](https://permetrics.readthedocs.io/en/latest/pages/regression/MBE.html)|
|root_mean_squared_error|None|double|[لینک](https://permetrics.readthedocs.io/en/latest/pages/regression/RMSE.html)|
|mean_percentage_error|None|double|[لینک](https://permetrics.readthedocs.io/en/latest/pages/regression/MPE.html)|
|pearson_correlation_coefficient|None|double|[لینک](https://permetrics.readthedocs.io/en/latest/pages/regression/R.html)|

### مثال

### قدرانی

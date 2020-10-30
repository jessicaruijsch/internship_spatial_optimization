# go to working directory
cd /Volumes/SSD_Jessica/Internship/Translate/
# reproject land use map to degrees and clip to correct extent
gdalwarp -t_srs EPSG:4326 -te -61.6666667 -18.1665169 -50.1668245 -7.2500000 mt_2017_v3_1.tif mt_2017_v3_1_reprojection.tif
# change pixel size of potential yield map
gdal_translate -tr 0.001893913403992 -0.001893913403992 -of AAIGrid -r average sugarcane.asc sugarcane_new.asc
gdal_translate -tr 0.001893913403992 -0.001893913403992 -of AAIGrid -r average soy.asc soy_new.asc
gdal_translate -tr 0.001893913403992 -0.001893913403992 -of AAIGrid -r average cotton.asc cotton_new.asc
gdal_translate -tr 0.001893913403992 -0.001893913403992 -of AAIGrid -r average grass.asc grass_new.asc


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 11:22:27 2020

@author: jessicaruijsch

# --------------------------------------------------
# initialization
# --------------------------------------------------  

Rules:
- A data cell must have exactly one class (between 1 and 13)
- Water, urban area and no data (11, 12, 15) cannot be changed 
- Cerrado, forest, secondary vegetation (1, 3, 13), can be turned into agriculture, but not the other way around
- Combine different soy classes (5, 6, 7, 8, 9) into one class of soy (5)
- Cotton, pasture, soy, sugarcane (2, 4, 5, 10) can be interchanged and replace forest

Initialization rules:
- random variation with constrains
- 70% of the initial map stays, 30% random classes with constrains:
    - water, urban area and no data (8, 9, 10) cannot be changed
    - cerrao, forest, secondary vegetation (1, 2, 3) can be turned into agriculture
    - cotton, pasture, soy, sugarcane (4, 5, 6, 7) can be changed
    

Reclassify:
1 = forest                #10773e
2 = cerrado               #b3cc33  
3 = secondary_vegetation  #0cf8c1
4 = soy                   #a4507d
5 = sugarcane             #877712
6 = fallow_cotton         #be94e8
7 = pasture               #eeefce
8 = water                 #1b5ee4
9 = urban                 #614040
10 = no_data              #00000000
    
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import pickle
import matplotlib.patches as mpatches

default_directory = "/Users/jessicaruijsch/Documents/Internship/study_project_jessica/input_data"

# --------------------------------------------------
# read data
# --------------------------------------------------  

# read data from tiff file
landuse_original = plt.imread(default_directory + "/Landuse_maps/mt_2017_v3_1_reprojection.tif")

# plot original landuse map
cmap = ListedColormap(["#b3cc33","#be94e8","#10773e","#eeefce","#e4a540",
                        "#a4507d","#c948a2","#be5b1d","#f09cde","#877712",
                        "#614040","#1b5ee4","#0cf8c1","#00000000","#00000000"])

legend_landuse = [mpatches.Patch(color="#b3cc33",label = 'Cerrado'),
                  mpatches.Patch(color="#be94e8",label = 'Fallow/cotton'),
                  mpatches.Patch(color="#10773e",label = 'Forest'),
                  mpatches.Patch(color="#eeefce",label = 'Pasture'),
                  mpatches.Patch(color="#e4a540",label = 'Soy/corn'),
                  mpatches.Patch(color="#a4507d",label = 'Soy/cotton'),
                  mpatches.Patch(color="#c948a2",label = 'Soy/fallow'),
                  mpatches.Patch(color="#be5b1d",label = 'Soy/millet'),
                  mpatches.Patch(color="#f09cde",label = 'Soy/sunflower'),
                  mpatches.Patch(color="#877712",label = 'Sugarcane'),
                  mpatches.Patch(color="#614040",label = 'Urban area'),
                  mpatches.Patch(color="#1b5ee4",label = 'Water'),
                  mpatches.Patch(color="#0cf8c1",label = 'Secondary vegetation'),
                  mpatches.Patch(color="#00000000",label = 'No data')]

# plt.rc('font', family='serif')
# plt.figure(figsize=(9,5))
# plt.imshow(landuse_original,interpolation='none',cmap=cmap,vmin = 0.5, vmax = 15.5)
# # plt.title('Landuse map original')
# plt.xlabel('Column #')
# plt.ylabel('Row #')
# plt.legend(handles=legend_landuse,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# plt.imsave(default_directory + "/Landuse_maps/MatoGrosso_2017_original.tif",landuse_original,format='tiff',cmap=cmap)
# plt.savefig(default_directory + "/Landuse_maps/MatoGrosso_2017_original.png",dpi=150)
# plt.show()

# plot original landuse map
f1, ax1 = plt.subplots(1)
cmap1 = ListedColormap(["#b3cc33","#be94e8","#10773e","#eeefce",
                       "#e4a540","#a4507d","#c948a2","#be5b1d",
                       "#f09cde","#877712","#614040","#1b5ee4",
                       "#0cf8c1","#00000000","#00000000"])

legend_landuse = [mpatches.Patch(color="#b3cc33",label = 'Cerrado'),
                  mpatches.Patch(color="#be94e8",label = 'Fallow/cotton'),
                  mpatches.Patch(color="#10773e",label = 'Forest'),
                  mpatches.Patch(color="#eeefce",label = 'Pasture'),
                  mpatches.Patch(color="#e4a540",label = 'Soy/corn'),
                  mpatches.Patch(color="#a4507d",label = 'Soy/cotton'),
                  mpatches.Patch(color="#c948a2",label = 'Soy/fallow'),
                  mpatches.Patch(color="#be5b1d",label = 'Soy/millet'),
                  mpatches.Patch(color="#f09cde",label = 'Soy/sunflower'),
                  mpatches.Patch(color="#877712",label = 'Sugarcane'),
                  mpatches.Patch(color="#614040",label = 'Urban area'),
                  mpatches.Patch(color="#1b5ee4",label = 'Water'),
                  mpatches.Patch(color="#0cf8c1",label = 'Secondary veg.'),
                  mpatches.Patch(color="#00000000",label = 'No data')]

im1 = plt.imshow(landuse_original,interpolation='none',
           cmap=cmap1,vmin = 0.5, vmax = 15.5)
ax1.set_title('Landuse map original')
ax1.set_xlabel('Column #')
ax1.set_ylabel('Row #') 
ax1.legend(handles=legend_landuse,bbox_to_anchor=(1.05, 1), loc=2, 
           borderaxespad=0.)
plt.imsave(default_directory +     
           "/Landuse_maps/MatoGrosso_2017_original.tif",
           landuse_original,format='tiff',cmap=cmap1)
plt.show()


# --------------------------------------------------
# reclassify
# --------------------------------------------------  
legend_landuse = [mpatches.Patch(color="#10773e",label = 'Forest'),
          mpatches.Patch(color="#b3cc33",label = 'Cerrado'),
          mpatches.Patch(color="#0cf8c1",label = 'Secondary vegetation'),
          mpatches.Patch(color="#a4507d",label = 'Soy'),
          mpatches.Patch(color="#877712",label = 'Sugarcane'),
          mpatches.Patch(color="#be94e8",label = 'Fallow/cotton'),
          mpatches.Patch(color="#eeefce",label = 'Pasture'),
          mpatches.Patch(color="#1b5ee4",label = 'Water'),
          mpatches.Patch(color="#614040",label = 'Urban'),
          mpatches.Patch(color="#00000000",label = 'No data')]

# reduce the number of classes by combining some of the agricultural classes
# create empty map
rows = landuse_original.shape[0]
cols = landuse_original.shape[1]
landuse_reclass = np.zeros((rows,cols),dtype= 'uint8')

# reclassify landuse map
landuse_reclass[landuse_original == 1] = 2
landuse_reclass[landuse_original == 2] = 6
landuse_reclass[landuse_original == 3] = 1
landuse_reclass[landuse_original == 4] = 7
landuse_reclass[landuse_original == 5] = 4
landuse_reclass[landuse_original == 6] = 4
landuse_reclass[landuse_original == 7] = 4
landuse_reclass[landuse_original == 8] = 4
landuse_reclass[landuse_original == 9] = 4
landuse_reclass[landuse_original == 10] = 5
landuse_reclass[landuse_original == 11] = 9
landuse_reclass[landuse_original == 12] = 8
landuse_reclass[landuse_original == 13] = 3
landuse_reclass[landuse_original == 15] = 10

# plot reclassified landuse map
cmap = ListedColormap(["#10773e","#b3cc33", "#0cf8c1", "#a4507d", "#877712","#be94e8","#eeefce","#1b5ee4","#614040","#00000000"])
plt.rc('font', family='serif')
plt.figure(figsize=(9,5))
plt.imshow(landuse_reclass,interpolation='None',cmap=cmap,vmin=0.5,vmax=10.5)
# plt.title('Landuse map reclassified')
plt.xlabel('Column #')
plt.ylabel('Row #')
plt.legend(handles=legend_landuse,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.imsave(default_directory + "/Landuse_maps/MatoGrosso_2017_reclassified.tif",landuse_reclass,format='tiff',cmap=cmap,vmin=0.5,vmax=10.5)
plt.savefig(default_directory + "/Landuse_maps/MatoGrosso_2017_reclassified.png",dpi=150)
plt.show()

# --------------------------------------------------
# crop map 
# --------------------------------------------------  

# get initial land use map with combined soy classes
# read land use map and crop area
landuse_map = landuse_reclass[2800:2900,1700:1800] 
np.save(default_directory + "/Landuse_maps/landuse_map_in.npy",landuse_map)

# plot reclassified landuse map
cmap = ListedColormap(["#10773e","#b3cc33", "#0cf8c1", "#a4507d", "#877712","#be94e8","#eeefce","#1b5ee4","#614040","#00000000"])
plt.rc('font', family='serif')
plt.figure(figsize=(9,5))
plt.imshow(landuse_map,interpolation='None',cmap=cmap,vmin=0.5,vmax=10.5)
# plt.title('Landuse map reclassified cropped')
plt.xlabel('Column #')
plt.ylabel('Row #')
plt.legend(handles=legend_landuse,bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.imsave(default_directory + "/Landuse_maps/MatoGrosso_2017_reclassified_cropped.tif",landuse_map,format='tiff',cmap=cmap,vmin=0.5,vmax=10.5)
plt.savefig(default_directory + "/Landuse_maps/MatoGrosso_2017_reclassified_cropped.png",dpi=150)
plt.show()

# --------------------------------------------------
# read potential yield maps needed for the objective functions
# --------------------------------------------------  

# read potential yield maps from asc file
sugarcane_pot_yield = np.loadtxt(default_directory + "/Objectives/sugarcane_new.asc", skiprows=6)[2800:2900,1700:1800]
soy_pot_yield = np.loadtxt(default_directory + "/Objectives/soy_new.asc", skiprows=6)[2800:2900,1700:1800]
cotton_pot_yield = np.loadtxt(default_directory + "/Objectives/cotton_new.asc", skiprows=6)[2800:2900,1700:1800]
pasture_pot_yield = np.loadtxt(default_directory + "/Objectives/grass_new.asc", skiprows=6)[2800:2900,1700:1800]

with open(default_directory + "/Objectives/sugarcane_potential_yield_example.pkl", 'wb') as output:
    pickle.dump(sugarcane_pot_yield, output, pickle.HIGHEST_PROTOCOL)

with open(default_directory + "/Objectives/soy_potential_yield_example.pkl", 'wb') as output:
    pickle.dump(soy_pot_yield, output, pickle.HIGHEST_PROTOCOL)

with open(default_directory + "/Objectives/cotton_potential_yield_example.pkl", 'wb') as output:
    pickle.dump(cotton_pot_yield, output, pickle.HIGHEST_PROTOCOL)

with open(default_directory + "/Objectives/pasture_potential_yield_example.pkl", 'wb') as output:
    pickle.dump(pasture_pot_yield, output, pickle.HIGHEST_PROTOCOL)




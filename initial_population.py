#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 09:13:52 2020

@author: root
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# make initial population for genetic algorithm
def initialize_spatial(pop_size,default_directory):
    all_landusemaps = []
    landuse_map_in = np.load(default_directory + "/Landuse_maps/landuse_map_in.npy")
    
    rows = landuse_map_in.shape[0]
    cols = landuse_map_in.shape[1]
    
    # iterate to get multiple realisations for the initial population
    for i in range(1,pop_size+1):
        
        #use uniform distribution to select 30% of the cells    
        landuse_map_ini = np.zeros((rows,cols),dtype='uint8')
        random_map = np.random.uniform(0.0,1.0,(rows,cols))
        random_map_mw = np.zeros((rows,cols))
        
        # take window average of of random map
        # to create larger patches
        for x in range(0,cols):
            for y in range(0,rows):
                if x == 0 or y == 0 or x == cols-1 or y == rows-1:
                    random_map_mw[x,y] = 1.0            
                else:
                    random_map_mw[y,x] = random_map[y-1:y+2,x-1:x+2].mean()
        
        
        # 70% of the map remains the current land use
        landuse_map_ini = np.where(random_map_mw>=0.3,landuse_map_in,landuse_map_ini)
            
        # 30% of the map will become new
        # urban, water and no data will remain the same
        landuse_map_ini = np.where(landuse_map_in >= 8,landuse_map_in,landuse_map_ini)
            
        # other land use types can change into 4, 5, 6 or 7        
        #choose which land cover type
        # 30% of the map will become new
        # urban, water and no data will remain the same
        landuse_map_ini = np.where(landuse_map_ini == 0,np.random.randint(low=3, high=8,size=(rows,cols)), landuse_map_ini)
        #patchmap, genome =compute_genome.create_patch_ID_map(landuse_map_ini,0,[8,9],'True')

        all_landusemaps.append(landuse_map_ini)
    return np.array(all_landusemaps)


## default_directory = 
##
## maps = initialize_spatial(3, default_directory)
##
## f, axes = plt.subplots(1,3)
## cmap = ListedColormap(["#10773e","#b3cc33", "#0cf8c1", "#a4507d",
##                       "#877712","#be94e8","#eeefce","#1b5ee4",
##                       "#614040","#00000000"])
## for amap, ax in zip(maps, axes):
##     im = ax.imshow(amap,interpolation='none', cmap=cmap,vmin = 0.5, vmax = 10.5)
##    
## plt.colorbar(im, orientation='horizontal')
## plt.show()

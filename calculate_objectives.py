#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 09:13:27 2020

@author: root

# --------------------------------------------------
# calculate objectives 
# --------------------------------------------------  

1. maximize agricultural yield
2. minimize co2 emission
3. maximize clustering

https://webarchive.iiasa.ac.at/Research/LUC/GAEZv3.0/

"""
import numpy as np
from compute_genome import create_patch_ID_map

# calculate the total yield for sugarcane, soy, cotton and pasture
def calculate_tot_yield(landuse_map_in, sugarcane_map,soy_map,cotton_map,pasture_map,cellarea):
    all_yields = []
    for land_use_map in landuse_map_in:
        # rows = land_use_map.shape[0]
        # cols = land_use_map.shape[1]
    
        # sugarcane
        # create empty map
        # yield_sugarcane =  np.zeros((rows,cols),dtype= 'uint8')
        # the actual yield is the potential yield where there is sugarcane multiplied by the cellarea, everywhere else 0
        yield_sugarcane = np.where(land_use_map == 5, sugarcane_map*cellarea, 0) # yield in tonnes
        # total yield is equalt to the sum of the entire map
        tot_yield_sugarcane = np.sum(yield_sugarcane)
        
        # soy
        # yield_soy =  np.zeros((rows,cols),dtype= 'uint8')
        yield_soy = np.where(land_use_map == 4, soy_map*cellarea, 0) # yield in tonnes
        tot_yield_soy = np.sum(yield_soy)
        
        # cotton
        # yield_cotton =  np.zeros((rows,cols),dtype= 'uint8')
        yield_cotton = np.where(land_use_map == 6, cotton_map*cellarea, 0) # yield in tonnes
        tot_yield_cotton = np.sum(yield_cotton)
        
        # pasture
        # yield_pasture =  np.zeros((rows,cols),dtype= 'uint8')
        yield_pasture = np.where(land_use_map == 7, pasture_map*cellarea, 0) # yield in tonnes
        tot_yield_pasture = np.sum(yield_pasture)
        
        # total yield agriculture is equal tot the sum of the different crops
        tot_yield = tot_yield_sugarcane + tot_yield_soy + tot_yield_cotton + tot_yield_pasture
        all_yields.append(tot_yield)
    return(np.array(all_yields))

# --------------------------------------------------
# minimize CO2 emissions 
# --------------------------------------------------  

# CO2 emissions based related to carbon stock
# maximize above ground biomass
# calculate for each land use the above ground biomass
# add all land uses

def calculate_above_ground_biomass(landuse_map_in,cellarea):
    #multiply each land use type with a certain value to calculate above ground biomass
    # calculate the total are of each land use type
    all_emissions = []
    for land_use_map in landuse_map_in:
        forest_area = np.count_nonzero(land_use_map == 1)*cellarea
        cerrado_area = np.count_nonzero(land_use_map == 2)*cellarea
        secveg_area = np.count_nonzero(land_use_map == 3)*cellarea
        pasture_area = np.count_nonzero(land_use_map == 4)*cellarea
        sugarcane_area = np.count_nonzero(land_use_map ==5)*cellarea
        
        # total above ground biomass (tonneS) --> multiply area of land use type (ha) with the above ground biomass (tonnes/ha)
        above_ground_biomass = (forest_area*300 + cerrado_area*48 + secveg_area*150 + pasture_area*6.2*0.7 + sugarcane_area*16)
        all_emissions.append(above_ground_biomass)
    return(np.array(all_emissions))

"""                               
sources https://www.ipcc-nggip.iges.or.jp/public/2006gl/vol4.html
        https://www-sciencedirect-com.proxy.library.uu.nl/science/article/pii/S0378112711002325
        https://link-springer-com.proxy.library.uu.nl/article/10.1007/s41050-019-00012-3
 
                                        above ground biomass (tonnes d.m. ha-1)
1 = forest                #10773e       300 (tb 4.7 - tropical rain forest)
2 = cerrado               #b3cc33       48 (from article)
3 = secondary_vegetation  #0cf8c1       150 (half from forest)
4 = soy                   #a4507d       0 (harvested)
5 = sugarcane             #877712       16 (harvested)
6 = fallow_cotton         #be94e8       0 (harvested)
7 = pasture               #eeefce       6.2*0.7 (tb 6.4 - tropical moist grassland, 30% is eaten)
8 = water                 #1b5ee4       0 (no biomass)
9 = urban                 #614040       0 (no biomass)
10 = no_data              #00000000

"""

# --------------------------------------------------
# maximize clustering
# --------------------------------------------------  

# want to maximize clustering --> economical benefits
# minimize number of clusters

def calculate_landuse_patches(landuse_map_in):
    patches_out, genom_out = create_patch_ID_map(landuse_map_in,0,[0],"True")
    number_of_patches = patches_out.max()
    
    return(number_of_patches)










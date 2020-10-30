#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 09:26:20 2020

@author: root
"""

import numpy as np
import time

#-------------------------------------------------------------------------------------  
#   Determine the coordinates of neighboring cells of cell (col, row)
#-------------------------------------------------------------------------------------

def getNbh(col, row, ncols, nrows, four_neighbours):
    """Determine the neighboring cells of the cell (col,row) and
       return the coordinates as arrays separated in nbhs_col and nbhs_row.
       The combination of the elements gives the coordinates of the neighbouring cells.
       
       input:
           col and row are coordinates of the reviewed element
           ncols, nrows are numbers of rows and columns in the map
           four_neighbours if True than 4 neighboring cells are scanned else 8
    """
    
    # assuming that a cell in the center has 8 neighbouring cells
    if four_neighbours == 'False':
        # cell is no edge cell
        if col > 0 and row > 0 and row < nrows -1 and col < ncols -1:
            nbhs_col = [x + col for x in[-1, -1, -1,  0, 0,  1, 1, 1]]
            nbhs_row = [x + row for x in[-1,  0,  1, -1, 1, -1, 0, 1]]
        # cell is a left edge element but no corner element
        elif col == 0 and row > 0 and row < nrows -1:
            nbhs_col= [x + col for x in[0, 1, 1, 0, 1]]
            nbhs_row= [x + row for x in[-1, -1, 0, 1, 1]]   
        # cell is a right edge element but no corner element
        elif col == ncols -1 and row > 0 and row < nrows -1:
            nbhs_col= [x + col for x in[-1, -1, -1,  0, 0]]
            nbhs_row= [x + row for x in[-1,  0,  1, -1, 1]]
        # cell is an upper edge element but no corner element
        elif row == 0 and col > 0 and col < ncols -1:
            nbhs_col= [x + col for x in[-1, -1,  0, 1, 1 ]]
            nbhs_row= [x + row for x in[ 0,  1, 1, 0, 1 ]]
        # cell is a bottom edge element but no corner element    
        elif row == nrows -1 and col > 0 and col < ncols -1:
            nbhs_col= [x + col for x in[-1, -1,  0,  1, 1 ]]
            nbhs_row= [x + row for x in[ -1, 0, -1, -1, 0 ]] 
        # cell is in the left upper corner
        elif col == 0 and row == 0:
            nbhs_col= [x + col for x in[ 0, 1, 1]]
            nbhs_row= [x + row for x in[ 1, 0, 1]]
        # cell is in the left bottom corner
        elif col == 0 and row == nrows -1:
            nbhs_col= [x + col for x in[ 0,  1,  1]]
            nbhs_row= [x + row for x in[ -1, 0, -1]] 
        # cell is in the right upper corner
        elif col == ncols -1 and row == 0:
            nbhs_col= [x + col for x in[ -1, -1, 0]]
            nbhs_row= [x + row for x in[  0,  1, 1]]
        # cell is in the right bottom corner
        else:
            nbhs_col= [x + col for x in[ -1, -1, 0 ]]
            nbhs_row= [x + row for x in[ -1,  0, -1]] 
            
    # assuming that a cell in the center has 4 neighbouring cells
    elif four_neighbours == 'True':
        # cell is no edge cell
        if col > 0 and row > 0 and row < nrows -1 and col < ncols -1:
            nbhs_col = [x + col for x in[-1,  0, 0, 1]]
            nbhs_row = [x + row for x in[ 0, -1, 1, 0]]
        # cell is a left edge element but no corner element
        elif col == 0 and row > 0 and row < nrows -1:
            nbhs_col= [x + col for x in[0, 1, 0]]
            nbhs_row= [x + row for x in[-1, 0, 1]]   
        # cell is a right edge element but no corner element
        elif col == ncols -1 and row > 0 and row < nrows -1:
            nbhs_col= [x + col for x in[-1,  0, 0]]
            nbhs_row= [x + row for x in[ 0, 1, -1]]        
        # cell is an upper edge element but no corner element
        elif row == 0 and col > 0 and col < ncols -1:
            nbhs_col= [x + col for x in[-1, 0, 1]]
            nbhs_row= [x + row for x in[ 0, 1, 0]]
        # cell is an bottom edge element but no corner element    
        elif row == nrows -1 and col > 0 and col < ncols -1:
            nbhs_col= [x + col for x in[-1, 0,  1]]
            nbhs_row= [x + row for x in[ 0, -1, 0]] 
        # cell is in the left upper corner
        elif col == 0 and row == 0:
            nbhs_col= [x + col for x in[ 0, 1]]
            nbhs_row= [x + row for x in[ 1, 0]]
        # cell is in the left bottom corner
        elif col == 0 and row == nrows -1:
            nbhs_col= [x + col for x in[ 0,  1]]
            nbhs_row= [x + row for x in[ -1, 0]] 
        # cell is in the right upper corner
        elif col == ncols -1 and row == 0:
            nbhs_col= [x + col for x in[ -1, 0]]
            nbhs_row= [x + row for x in[  0, 1]]
        # cell is in the right bottom corner
        else:
            nbhs_col= [x + col for x in[ -1, 0 ]]
            nbhs_row= [x + row for x in[  0, -1]]

    # else:
    #     msg = "Error: ini input for four_neighbours is not correct. Please check."
    #     WriteLogMsg(msg) 
    #     raise SystemError("Error: ini input for four_neighbours is not correct")
    #     req.close_window

    return [nbhs_row, nbhs_col]

#-------------------------------------------------------------------------------------  
#   Determination of patch elements
#-------------------------------------------------------------------------------------

def determine_patch_elements(row, col, map, patch_map, patch_ID, cls, four_neighbours):
    """This recursive function scans all patch elements 
       and returns the coordinates of these elements.
       
       input:
           col and row are coordinates of the parent element
           map is the original ascii map
           patch_map is a map with patch_IDs for each patch element
           patch_ID is the ID of the new patch
           cls is the land use index of the patch
           four_neighbours if True than 4 neighboring cells are scanned else 8
    """
    # determine coordinates of neighboring cells
    new_nbhs_row, new_nbhs_col  = getNbh(col, row, map.shape[1], map.shape[0], four_neighbours)
    # stack for patch elements whose neighboring cells should be determined
    nbhs_row = []
    nbhs_col = []
    for i in range(len(new_nbhs_row)):
        # add new neighboring cells to nbhs_row/col if new cells belong to cls and are not jet marked as patch element
        # the cell is no patch element if it has another land use id
        if map[new_nbhs_row[i], new_nbhs_col[i]] == cls and patch_map[new_nbhs_row[i], new_nbhs_col[i]] == 0:
            nbhs_row.append(new_nbhs_row[i])     
            nbhs_col.append(new_nbhs_col[i])  
    while len(nbhs_row) > 0:
        # cells could be double in nbhs_row/col
        if patch_map[nbhs_row[0], nbhs_col[0]] == 0:
            # mark all patch elements in patch_map with patch_ID
            patch_map[nbhs_row[0], nbhs_col[0]] = patch_ID                                            
            # get coordinates of neighboring cells of this cell
            new_nbhs_row, new_nbhs_col  = getNbh(nbhs_col[0], nbhs_row[0], map.shape[1], map.shape[0], four_neighbours)
            for i in range(len(new_nbhs_row)):
                # add new neighboring cells to nbhs_row/col if new cells belong to cls and are not jet marked as patch element
                if map[new_nbhs_row[i], new_nbhs_col[i]] == cls and patch_map[new_nbhs_row[i], new_nbhs_col[i]] == 0:
                    nbhs_row.append(new_nbhs_row[i])     
                    nbhs_col.append(new_nbhs_col[i])
        # delete this checked neighboring cell of the array    
        del nbhs_row[0]
        del nbhs_col[0]

    return patch_map


#-------------------------------------------------------------------------------------  
#   Determine patch elements of a patch ID map and check equality of land use index
#-------------------------------------------------------------------------------------

def create_patch_ID_map(map, NODATA_value, static_elements, four_neighbours=True):
    """This function clusters the cells of the original map into patches
        and returns a patch ID map as a 2 dimensional array and the start individual as vector.
    
        input: 
            map is the original map represented as 2d numpy array
            NODATA_value is the NODATA_value of the original map
            static_elements are the land use indices excluded from the optimization
            four_neighbours if True than 4 neighboring cells are scanned else 8
    """

   
    patches= np.zeros([map.shape[0], map.shape[1]], int)
    ids = 0
    NoData = int(NODATA_value)
    genom = []
    # loop over all cells
    for row in range(0, map.shape[0]):
        for col in range(0, map.shape[1]):
            # patchID = 0 used for static_elements
            # map element was not scanned before as patch element and is not a static element or the NODATA_value
            if patches[row,col]==0 and static_elements.count(map[row, col])==0 and map[row,col]!=NoData:
                cls = map[row, col]
                # increment scanned patch ID
                ids += 1
                # mark this cell as scanned patch element 
                patches[row, col] = ids
                determine_patch_elements(row,col, map, patches, ids, cls, four_neighbours) 
                # add the map cell value to the individual vector
                genom.append(cls)     
    return patches, genom   
import numpy as np
import os, sys
import gmsh


# ========================================================= #
# ===  make__geometry                                   === #
# ========================================================= #

def make__geometry():

    scale   = 1.0e-6
    inpFile = "model/model.step"
    
    gmsh.option.setNumber( "Geometry.OCCScaling", scale )
    gmsh.model.occ.importShapes( inpFile )
    
    return()

    


# ========================================================= #
# ===   実行部                                          === #
# ========================================================= #

if ( __name__=="__main__" ):
    

    # ------------------------------------------------- #
    # --- [1] initialization of the gmsh            --- #
    # ------------------------------------------------- #
    gmsh.initialize()
    gmsh.option.setNumber( "General.Terminal", 1 )
    gmsh.option.setNumber( "Mesh.Algorithm"  , 1 )
    gmsh.option.setNumber( "Mesh.Algorithm3D", 1 )
    gmsh.option.setNumber( "Mesh.SubdivisionAlgorithm", 1 )
    gmsh.model.add( "model" )
    
    
    # ------------------------------------------------- #
    # --- [2] Modeling                              --- #
    # ------------------------------------------------- #

    make__geometry()
    
    gmsh.model.occ.synchronize()
    gmsh.model.occ.removeAllDuplicates()
    gmsh.model.occ.synchronize()


    # ------------------------------------------------- #
    # --- [3] Mesh settings                         --- #
    # ------------------------------------------------- #
    
    # meshFile = "dat/mesh.conf"
    # physFile = "dat/phys.conf"
    # import nkGmshRoutines.assign__meshsize as ams
    # meshes = ams.assign__meshsize( meshFile=meshFile, physFile=physFile )
    
    gmsh.option.setNumber( "Mesh.CharacteristicLengthMin", 0.1 )
    gmsh.option.setNumber( "Mesh.CharacteristicLengthMax", 0.1 )
    

    # ------------------------------------------------- #
    # --- [4] post process                          --- #
    # ------------------------------------------------- #
    gmsh.model.occ.synchronize()
    gmsh.model.mesh.generate(3)
    gmsh.write( "msh/model.msh" )

    flag__bdf_output = True
    if ( flag__bdf__output ):
        gmsh.option.setNumber( "Mesh.SaveElementTagType", 2 )
        gmsh.option.setNumber( "Mesh.BdfFieldFormat"    , 0 )
        gmsh.write( "msh/model.bdf" )
    
    gmsh.finalize()
    




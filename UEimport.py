import os
import unreal_engine as ue
from unreal_engine import FVector
from unreal_engine.classes import AlembicImportFactory
from unreal_engine.classes import MaterialFactoryNew
from unreal_engine.structs import SkeletalMaterial, MeshUVChannelInfo
from unreal_engine.classes import PyFbxFactory
from unreal_engine.structs import AbcConversionSettings, AbcSamplingSettings, AbcMaterialSettings

abc = "//MOMODISK/library/Assets/3D/character/crowd/football/costume/jersey/mod/jersey.abc"
fbx = "//MOMODISK/library/Assets/3D/character/crowd/football/costume/jersey/mod/jersey.fbx"
#abc = "C:/Users/l3ox/Desktop/Kaiju_Assets/Slicer/slicer.abc"
#fbx = "C:/Users/l3ox/Desktop/Kaiju_Assets/Slicer/slicer1.fbx"

factory = AlembicImportFactory()
factory.bShowOption = False
factory.ImportSettings.ImportType = 0
factory.ImportSettings.SamplingSettings = AbcSamplingSettings(bSkipEmpty = True)
factory.ImportSettings.MaterialSettings = AbcMaterialSettings(bCreateMaterials = True)
factory.ImportSettings.ConversionSettings = AbcConversionSettings(Preset = 2, Scale = FVector(10,-10,10), Rotation = FVector(-90,0,0))


fbx_factory = PyFbxFactory()
fbx_factory.ImportUI.bImportMaterials = False
fbx_factory.ImportUI.bImportTextures = False
asset = factory.factory_import_object(abc, '/Game/Meshes')
#asset = fbx_factory.factory_import_object(fbx, '/Game/Meshes')

material_factory = MaterialFactoryNew()
materialFront = material_factory.factory_create_new('/Game/MTL_front_MASTER')
materialSide = material_factory.factory_create_new('/Game/MTL_side_MASTER')

#asset = (ue.get_asset('/Game/Meshes/jersey.jersey'))

#print (asset.properties())

print (asset.properties)

asset.save_package()
materialFront.save_package()
materialSide.save_package()
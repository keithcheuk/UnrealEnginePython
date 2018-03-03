import os
import unreal_engine as ue
from unreal_engine import FVector, FRawMesh
from unreal_engine.classes import AlembicImportFactory, PyFbxFactory, MaterialFactoryNew, StaticMesh
from unreal_engine.structs import SkeletalMaterial, MeshUVChannelInfo, StaticMaterial
from unreal_engine.structs import AbcConversionSettings, AbcSamplingSettings, AbcMaterialSettings

abc = "//MOMODISK/library/Assets/3D/character/crowd/football/costume/jersey/mod/jersey.abc"

factory = AlembicImportFactory()
factory.bShowOption = False
factory.ImportSettings.ImportType = 0
factory.ImportSettings.SamplingSettings = AbcSamplingSettings(bSkipEmpty = True)
factory.ImportSettings.MaterialSettings = AbcMaterialSettings(bCreateMaterials = True)
factory.ImportSettings.ConversionSettings = AbcConversionSettings(Preset = 2, Scale = FVector(10,-10,10), Rotation = FVector(90,0,0))

asset = factory.factory_import_object(abc, '/Game/Meshes')

#material_factory = MaterialFactoryNew()
materialFront = ue.get_asset("/Game/MTL_front_MASTER.MTL_front_MASTER")
materialSide = ue.get_asset("/Game/MTL_side_MASTER.MTL_side_MASTER")


asset = (ue.get_asset('/Game/Meshes/jersey.jersey'))
material = [StaticMaterial(MaterialInterface=materialFront, MaterialSlotName="MTL_front_srf", UVChannelData=MeshUVChannelInfo(bInitialized=True)),StaticMaterial(MaterialInterface=materialSide, MaterialSlotName="MTL_side_srf", UVChannelData=MeshUVChannelInfo(bInitialized=True))]
asset.StaticMaterials = material

asset.save_package()
materialFront.save_package()
materialSide.save_package()
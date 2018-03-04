import unreal_engine as ue
from unreal_engine import FSlateIcon, FSlateStyleSet, FLinearColor
from unreal_engine.structs import SlateBrush, SlateColor, Vector2D

# this code must be in ue_site.py, extenders must be  registered during editor startup phase !!!

# we create a new StyleSet to register a new Icon

# this generates the menu entries
def open_menu(menu):
   #menu.begin_section('test1', 'test2')
   menu.add_menu_entry('Import assets', 'Import assets base from a json file', lambda: ue.log('Import assets'))
   menu.add_menu_entry('Build materials', 'Create and assign materials based on shading group', lambda: ue.log('Build materials'))
   menu.end_section()



ue.add_menu_bar_extension('Dneg', open_menu)


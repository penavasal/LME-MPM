# Recorded script from Mayavi2
from numpy import array
try:
    engine = mayavi.engine
except NameError:
    from mayavi.api import Engine
    engine = Engine()
    engine.start()
if len(engine.scenes) == 0:
    engine.new_scene()
# ------------------------------------------- 
module_manager = engine.scenes[0].children[0].children[0].children[0]
module_manager.scalar_lut_manager.lut_mode = 'jet'
module_manager.vector_lut_manager.lut_mode = 'jet'
scene = engine.scenes[0]
scene.scene.background = (1.0, 1.0, 1.0)
module_manager.scalar_lut_manager.title_text_property.shadow_offset = array([ 1, -1])
module_manager.scalar_lut_manager.title_text_property.shadow_offset = array([ 1, -1])
module_manager.scalar_lut_manager.title_text_property.color = (0.5254901960784314, 0.5254901960784314, 0.5254901960784314)
module_manager.scalar_lut_manager.label_text_property.shadow_offset = array([ 1, -1])
module_manager.scalar_lut_manager.label_text_property.shadow_offset = array([ 1, -1])
module_manager.scalar_lut_manager.label_text_property.color = (0.5254901960784314, 0.5254901960784314, 0.5254901960784314)
module_manager.vector_lut_manager.title_text_property.shadow_offset = array([ 1, -1])
module_manager.vector_lut_manager.title_text_property.shadow_offset = array([ 1, -1])
module_manager.vector_lut_manager.title_text_property.color = (0.5254901960784314, 0.5254901960784314, 0.5254901960784314)
module_manager.vector_lut_manager.label_text_property.shadow_offset = array([ 1, -1])
module_manager.vector_lut_manager.label_text_property.shadow_offset = array([ 1, -1])
module_manager.vector_lut_manager.label_text_property.color = (0.5254901960784314, 0.5254901960784314, 0.5254901960784314)
surface = engine.scenes[0].children[0].children[0].children[0].children[0]
surface.actor.property.ambient_color = (0.5254901960784314, 0.5254901960784314, 0.5254901960784314)
surface.actor.property.color = (0.5254901960784314, 0.5254901960784314, 0.5254901960784314)
surface.actor.property.diffuse_color = (0.5254901960784314, 0.5254901960784314, 0.5254901960784314)
surface.actor.property.specular_color = (0.5254901960784314, 0.5254901960784314, 0.5254901960784314)
from mayavi.modules.axes import Axes
axes = Axes()
engine.add_filter(axes, module_manager)
from mayavi.modules.outline import Outline
outline = Outline()
engine.add_filter(outline, module_manager)
module_manager.scalar_lut_manager.title_text_property.shadow_offset = array([ 1, -1])
module_manager.scalar_lut_manager.title_text_property.color = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
module_manager.scalar_lut_manager.label_text_property.shadow_offset = array([ 1, -1])
module_manager.scalar_lut_manager.label_text_property.color = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
module_manager.vector_lut_manager.title_text_property.shadow_offset = array([ 1, -1])
module_manager.vector_lut_manager.title_text_property.color = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
module_manager.vector_lut_manager.label_text_property.shadow_offset = array([ 1, -1])
module_manager.vector_lut_manager.label_text_property.color = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
surface.actor.property.ambient_color = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
surface.actor.property.diffuse_color = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
surface.actor.property.specular_color = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
surface.actor.property.color = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
scene.scene.foreground = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
axes.property.reference_count = 8
axes.property.color = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
axes.label_text_property.shadow_offset = array([ 1, -1])
axes.label_text_property.color = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
axes.title_text_property.shadow_offset = array([ 1, -1])
axes.title_text_property.color = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
outline.actor.property.ambient_color = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
outline.actor.property.diffuse_color = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
outline.actor.property.specular_color = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
outline.actor.property.color = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
# outline.outline_filter.input_connection = <tvtk.tvtk_classes.algorithm_output.AlgorithmOutput object at 0x7fe85690d890>
outline.manual_bounds = True
outline.bounds = array([-1.9,  1. , -1. ,  1. , -1. ,  1. ])
outline.bounds = array([-1.9,  1. , -1. ,  1. , -1. ,  1. ])
outline.bounds = array([-1.9,  1.9, -1. ,  1. , -1. ,  1. ])
outline.bounds = array([-1.9,  1.9, -1. ,  1. , -1. ,  1. ])
outline.bounds = array([-1.9,  1.9, -1.9,  1. , -1. ,  1. ])
outline.bounds = array([-1.9,  1.9, -1.9,  1. , -1. ,  1. ])
outline.bounds = array([-1.9,  1.9, -1.9,  1.9, -1. ,  1. ])
outline.bounds = array([-1.9,  1.9, -1.9,  1.9, -1. ,  1. ])
axes.axes.bounds = array([-1.9       ,  1.9       , -1.9       ,  1.9       , -0.38162462,
        0.38162462])
axes.axes.ranges = array([0., 0., 0., 0., 0., 0.])
axes.axes.position = array([0., 0.])
axes.axes.position2 = array([0.5, 0.5])
axes.axes.render_time_multiplier = 0.9187323287721842
axes.axes.reference_count = 2
axes.axes.x_axis_visibility = False
axes.axes.bounds = array([-1.9       ,  1.9       , -1.9       ,  1.9       , -0.38162462,
        0.38162462])
axes.axes.ranges = array([0., 0., 0., 0., 0., 0.])
axes.axes.position = array([0., 0.])
axes.axes.position2 = array([0.5, 0.5])
axes.axes.y_axis_visibility = False
axes.axes.bounds = array([-1.9       ,  1.9       , -1.9       ,  1.9       , -0.38162462,
        0.38162462])
axes.axes.ranges = array([0., 0., 0., 0., 0., 0.])
axes.axes.position = array([0., 0.])
axes.axes.position2 = array([0.5, 0.5])
axes.axes.z_axis_visibility = False

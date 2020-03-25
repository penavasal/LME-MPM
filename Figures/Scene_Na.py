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
from mayavi.modules.outline import Outline
outline = Outline()
module_manager = engine.scenes[0].children[0].children[0].children[0]
engine.add_filter(outline, module_manager)
# outline.outline_filter.input_connection = <tvtk.tvtk_classes.algorithm_output.AlgorithmOutput object at 0x7f82116ed770>
outline.manual_bounds = True
outline.bounds = array([-1.9,  1. , -1. ,  1. , -1. ,  1. ])
outline.bounds = array([-1.9,  1. , -1. ,  1. , -1. ,  1. ])
outline.bounds = array([-1.9,  1.9, -1. ,  1. , -1. ,  1. ])
outline.bounds = array([-1.9,  1.9, -1. ,  1. , -1. ,  1. ])
outline.bounds = array([-1.9,  1.9, -1.9,  1. , -1. ,  1. ])
outline.bounds = array([-1.9,  1.9, -1.9,  1. , -1. ,  1. ])
outline.bounds = array([-1.9,  1.9, -1.9,  1.9, -1. ,  1. ])
outline.bounds = array([-1.9,  1.9, -1.9,  1.9, -1. ,  1. ])
outline.bounds = array([-1.9,  1.9, -1.9,  1.9,  0. ,  1. ])
outline.bounds = array([-1.9,  1.9, -1.9,  1.9,  0. ,  1. ])
outline.bounds = array([-1.9,  1.9, -1.9,  1.9,  0. ,  4. ])
outline.bounds = array([-1.9,  1.9, -1.9,  1.9,  0. ,  4. ])
scene = engine.scenes[0]
scene.scene.camera.position = [7.734688192344844, 7.734688192344844, 8.19470485206996]
scene.scene.camera.focal_point = [0.0, 0.0, 0.4600166597251145]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.0, 0.0, 1.0]
scene.scene.camera.clipping_range = [5.48912328832708, 21.372954126716014]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [9.358972712737263, 9.358972712737263, 9.818989372462378]
scene.scene.camera.focal_point = [0.0, 0.0, 0.4600166597251145]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.0, 0.0, 1.0]
scene.scene.camera.clipping_range = [8.27433317044172, 24.22849759171234]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [11.32435698241209, 11.32435698241209, 11.784373642137204]
scene.scene.camera.focal_point = [0.0, 0.0, 0.4600166597251145]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.0, 0.0, 1.0]
scene.scene.camera.clipping_range = [11.644437127800437, 27.683705184357894]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [11.285209998748872, 12.65860272193102, 10.31531957783844]
scene.scene.camera.focal_point = [0.0, 0.0, 0.4600166597251145]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.34972300899173736, -0.36121029772995894, 0.8644194223845274]
scene.scene.camera.clipping_range = [11.79392135655436, 27.75634264747815]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
outline.bounds = array([-2. ,  1.9, -1.9,  1.9,  0. ,  4. ])
outline.bounds = array([-2. ,  1.9, -1.9,  1.9,  0. ,  4. ])
outline.bounds = array([-2. ,  1. , -1.9,  1.9,  0. ,  4. ])
outline.bounds = array([-2. ,  1. , -1.9,  1.9,  0. ,  4. ])
outline.bounds = array([-2. ,  1. ,  2. ,  1.9,  0. ,  4. ])
outline.bounds = array([-2. ,  1. ,  2. ,  1.9,  0. ,  4. ])
outline.bounds = array([-2. ,  1. , -2. ,  1.9,  0. ,  4. ])
outline.bounds = array([-2. ,  1. , -2. ,  1.9,  0. ,  4. ])
outline.bounds = array([-2.,  1., -2.,  2.,  0.,  4.])
outline.bounds = array([-2.,  1., -2.,  2.,  0.,  4.])
outline.bounds = array([-2.,  2., -2.,  2.,  0.,  4.])
outline.bounds = array([-2.,  2., -2.,  2.,  0.,  4.])
scene.scene.camera.position = [14.09863282258635, 11.638715398746106, 7.565791747369913]
scene.scene.camera.focal_point = [0.0, 0.0, 0.4600166597251145]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.2277629002861263, -0.2913455237585558, 0.9291080922256059]
scene.scene.camera.clipping_range = [12.20161926662119, 27.73127014587667]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.isometric_view()
scene.scene.camera.position = [9.373459642682972, 9.142861079853224, 4.772144362186732]
scene.scene.camera.focal_point = [0.0, 0.0, 2.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.1423020719551314, -0.15072640003679408, 0.9782799561726825]
scene.scene.camera.clipping_range = [6.9199908989090675, 21.553728550343116]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [7.844416705478202, 10.523361108043742, 4.619625222017861]
scene.scene.camera.focal_point = [0.0, 0.0, 2.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.13539598263480004, -0.14312689514549143, 0.9803992144898772]
scene.scene.camera.clipping_range = [7.0095159737936665, 21.441034925928104]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [7.159905626471528, 11.022345647156047, 4.526279204273884]
scene.scene.camera.focal_point = [0.0, 0.0, 2.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.13256998532437972, -0.13881915801772793, 0.981404320531728]
scene.scene.camera.clipping_range = [7.092442688315036, 21.336647277749194]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [9.086904655801014, 8.756026769207187, 6.460784432878764]
scene.scene.camera.focal_point = [0.0, 0.0, 2.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.2331864474566941, -0.23830418859123387, 0.9427805653609966]
scene.scene.camera.clipping_range = [6.618091666705066, 21.933757483343598]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [9.835980462477727, 8.563899538576292, 5.008579697835728]
scene.scene.camera.focal_point = [0.0, 0.0, 2.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.03858273470358503, -0.2914685581117161, 0.9558019942514611]
scene.scene.camera.clipping_range = [6.8843087966704815, 21.598644965472186]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.isometric_view()
scene.scene.camera.position = [7.108648521965442, 10.933533299965266, 5.010548875705875]
scene.scene.camera.focal_point = [0.0, 0.0, 2.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.16493593463034487, -0.16071303761861722, 0.9731225292875569]
scene.scene.camera.clipping_range = [6.990089865929438, 21.465488393365195]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [9.378436678099986, 9.354880530672203, 3.9156133469527097]
scene.scene.camera.focal_point = [0.0, 0.0, 2.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.1079923776998377, -0.0943900287102755, 0.989660633166142]
scene.scene.camera.clipping_range = [7.110165571389918, 21.314337819406106]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-0.6545384629077908, 13.365158661751591, 1.7126811699796767]
scene.scene.camera.focal_point = [0.0, 0.0, 2.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.10487830434936152, 0.016239934408636893, 0.9943524555243005]
scene.scene.camera.clipping_range = [8.99602392222061, 18.940430699390525]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-1.884945142715888, 13.159188971571856, 0.44399030121430855]
scene.scene.camera.focal_point = [0.0, 0.0, 2.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.07488670271133047, 0.1276696053127928, 0.9889855679615861]
scene.scene.camera.clipping_range = [8.314129795080795, 19.798794914709596]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [-1.0218868637725338, 13.276432269127795, 0.6470283801154983]
scene.scene.camera.focal_point = [0.0, 0.0, 2.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.07846553695940639, 0.10704569028106826, 0.9911530556386949]
scene.scene.camera.clipping_range = [8.596284724628664, 19.44361999083148]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.y_plus_view()
scene.scene.z_minus_view()
scene.scene.y_plus_view()
scene.scene.z_plus_view()
scene.scene.camera.position = [1.686229429315586, -11.921823151059355, 7.84510066892618]
scene.scene.camera.focal_point = [0.0, 0.0, 2.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.040845385694582716, 0.4445064699521219, 0.8948439264129606]
scene.scene.camera.clipping_range = [7.465746931423072, 20.866734147605726]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.x_plus_view()
scene.scene.camera.position = [7.5657929475939385, 11.024166423238276, 1.3958721077544376]
scene.scene.camera.focal_point = [0.0, 0.0, 2.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.013462422989473546, 0.045499451562632964, 0.9988736472020634]
scene.scene.camera.clipping_range = [7.542783880715128, 20.769760500381253]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [8.44884029985033, 10.342812873159188, 2.8841709233751525]
scene.scene.camera.focal_point = [0.0, 0.0, 2.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.06423034984868539, -0.03279539538506854, 0.9973960718790968]
scene.scene.camera.clipping_range = [7.399532593502094, 20.95008435689809]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [8.567187280453322, 10.27531509325342, 2.399550496558743]
scene.scene.camera.focal_point = [0.0, 0.0, 2.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.046801768895762125, 0.00017973733903850486, 0.9989041806513357]
scene.scene.camera.clipping_range = [7.52852062638914, 20.78771499891703]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [8.533294379273237, 9.381402826156181, 6.279089484149097]
scene.scene.camera.focal_point = [0.0, 0.0, 2.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.24667003433154763, -0.20741677264376884, 0.9466425812253094]
scene.scene.camera.clipping_range = [6.650780665705396, 21.892608768521423]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [9.301781416554862, 9.44456968294456, 3.848081368863794]
scene.scene.camera.focal_point = [0.0, 0.0, 2.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.13499112476094915, -0.06057266103017348, 0.9889936041105106]
scene.scene.camera.clipping_range = [7.12637135144532, 21.2939380811955]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [9.862366900119035, 9.038948013587913, 2.4117969140166053]
scene.scene.camera.focal_point = [0.0, 0.0, 2.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.056510132137121916, 0.01617873754711193, 0.9982709318703149]
scene.scene.camera.clipping_range = [7.507390236474731, 20.814313806321763]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [4.788630943246559, 12.407597502894658, 3.502989241094505]
scene.scene.camera.focal_point = [0.0, 0.0, 2.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.23020875741560323, -0.028981220868407584, 0.9727096261712128]
scene.scene.camera.clipping_range = [7.689940375382978, 20.584520792268926]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [4.788630943246559, 12.407597502894658, 3.502989241094505]
scene.scene.camera.focal_point = [0.0, 0.0, 2.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.03450830363256062, -0.1070477197021888, 0.9936548508848355]
scene.scene.camera.clipping_range = [7.689940375382978, 20.584520792268926]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [3.9575462340880647, 10.254212812309634, 3.242139868673145]
scene.scene.camera.focal_point = [0.0, 0.0, 2.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.03450830363256062, -0.1070477197021888, 0.9936548508848355]
scene.scene.camera.clipping_range = [5.390281009471066, 18.226789220147115]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [3.901229802839403, 10.108293943218607, 3.2244640462373084]
scene.scene.camera.focal_point = [0.0, 0.0, 2.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.03450830363256062, -0.1070477197021888, 0.9936548508848355]
scene.scene.camera.clipping_range = [5.234450193251559, 18.067023282305904]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [3.901229802839403, 10.108293943218607, 3.2244640462373084]
scene.scene.camera.focal_point = [0.0, 0.0, 2.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.03255062292081545, -0.10780140556122347, 0.9936394285184601]
scene.scene.camera.clipping_range = [5.234450193251559, 18.067023282305904]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [3.8574615696619294, 10.145227765644114, 3.0590137020997457]
scene.scene.camera.focal_point = [-0.04376823317747491, 0.03693382242550536, 1.834549655862438]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.03255062292081545, -0.10780140556122347, 0.9936394285184601]
scene.scene.camera.clipping_range = [5.234450193251559, 18.067023282305904]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.background = (1.0, 1.0, 1.0)
module_manager.scalar_lut_manager.title_text_property.shadow_offset = array([ 1, -1])
module_manager.scalar_lut_manager.title_text_property.color = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
module_manager.scalar_lut_manager.label_text_property.shadow_offset = array([ 1, -1])
module_manager.scalar_lut_manager.label_text_property.color = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
module_manager.vector_lut_manager.title_text_property.shadow_offset = array([ 1, -1])
module_manager.vector_lut_manager.title_text_property.color = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
module_manager.vector_lut_manager.label_text_property.shadow_offset = array([ 1, -1])
module_manager.vector_lut_manager.label_text_property.color = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
surface = engine.scenes[0].children[0].children[0].children[0].children[0]
surface.actor.property.ambient_color = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
surface.actor.property.diffuse_color = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
surface.actor.property.specular_color = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
surface.actor.property.color = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
scene.scene.foreground = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
outline.actor.property.ambient_color = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
outline.actor.property.diffuse_color = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
outline.actor.property.specular_color = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)
outline.actor.property.color = (0.5450980392156862, 0.5450980392156862, 0.5450980392156862)

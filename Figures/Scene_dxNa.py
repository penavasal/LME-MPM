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
scene = engine.scenes[0]
scene.scene.camera.position = [12.405354476130022, 12.405354476130022, 12.405354476130022]
scene.scene.camera.focal_point = [0.0, 0.0, 0.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.0, 0.0, 1.0]
scene.scene.camera.clipping_range = [15.574096976424016, 28.98128583252587]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [10.252359071181836, 10.252359071181836, 10.252359071181836]
scene.scene.camera.focal_point = [0.0, 0.0, 0.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [0.0, 0.0, 1.0]
scene.scene.camera.clipping_range = [11.88229052088975, 25.19625194124579]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [9.945049557847135, 11.27617527668267, 9.448622121496244]
scene.scene.camera.focal_point = [0.0, 0.0, 0.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.3759940360636462, -0.37748496147533483, 0.8462467658458346]
scene.scene.camera.clipping_range = [11.808094532000167, 25.289649404646994]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [8.219049221361265, 9.319153121225344, 7.808778612806812]
scene.scene.camera.focal_point = [0.0, 0.0, 0.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.3759940360636462, -0.37748496147533483, 0.8462467658458346]
scene.scene.camera.clipping_range = [8.757014816682595, 22.161522221770895]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [6.792602662282036, 7.701779439029209, 6.453536043641991]
scene.scene.camera.focal_point = [0.0, 0.0, 0.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.3759940360636462, -0.37748496147533483, 0.8462467658458346]
scene.scene.camera.clipping_range = [6.235461332949065, 19.576293145013793]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [8.000317194605252, 8.36154171834617, 3.631050784516862]
scene.scene.camera.focal_point = [0.0, 0.0, 0.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.2169908055051164, -0.20668223889975093, 0.9540426837671504]
scene.scene.camera.clipping_range = [6.066847261093487, 19.788543521897317]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
scene.scene.camera.position = [6.611832392235745, 6.910365056484438, 3.000868416956084]
scene.scene.camera.focal_point = [0.0, 0.0, 0.0]
scene.scene.camera.view_angle = 30.0
scene.scene.camera.view_up = [-0.2169908055051164, -0.20668223889975093, 0.9540426837671504]
scene.scene.camera.clipping_range = [3.98291876214016, 17.65199056589971]
scene.scene.camera.compute_view_plane_normal()
scene.scene.render()
module_manager = engine.scenes[0].children[0].children[0].children[0]
module_manager.scalar_lut_manager.lut_mode = 'jet'
module_manager.vector_lut_manager.lut_mode = 'jet'
scene.scene.background = (1.0, 1.0, 1.0)
module_manager.scalar_lut_manager.title_text_property.shadow_offset = array([ 1, -1])
module_manager.scalar_lut_manager.title_text_property.color = (0.5254901960784314, 0.5254901960784314, 0.5254901960784314)
module_manager.scalar_lut_manager.label_text_property.shadow_offset = array([ 1, -1])
module_manager.scalar_lut_manager.label_text_property.color = (0.5254901960784314, 0.5254901960784314, 0.5254901960784314)
module_manager.vector_lut_manager.title_text_property.shadow_offset = array([ 1, -1])
module_manager.vector_lut_manager.title_text_property.color = (0.5254901960784314, 0.5254901960784314, 0.5254901960784314)
module_manager.vector_lut_manager.label_text_property.shadow_offset = array([ 1, -1])
module_manager.vector_lut_manager.label_text_property.color = (0.5254901960784314, 0.5254901960784314, 0.5254901960784314)
surface = engine.scenes[0].children[0].children[0].children[0].children[0]
surface.actor.property.ambient_color = (0.5254901960784314, 0.5254901960784314, 0.5254901960784314)
surface.actor.property.diffuse_color = (0.5254901960784314, 0.5254901960784314, 0.5254901960784314)
surface.actor.property.specular_color = (0.5254901960784314, 0.5254901960784314, 0.5254901960784314)
surface.actor.property.color = (0.5254901960784314, 0.5254901960784314, 0.5254901960784314)
axes = engine.scenes[0].children[0].children[0].children[0].children[1]
axes.property.reference_count = 8
axes.property.color = (0.5254901960784314, 0.5254901960784314, 0.5254901960784314)
axes.label_text_property.shadow_offset = array([ 1, -1])
axes.label_text_property.color = (0.5254901960784314, 0.5254901960784314, 0.5254901960784314)
axes.title_text_property.shadow_offset = array([ 1, -1])
axes.title_text_property.color = (0.5254901960784314, 0.5254901960784314, 0.5254901960784314)
outline = engine.scenes[0].children[0].children[0].children[0].children[2]
outline.actor.property.ambient_color = (0.5254901960784314, 0.5254901960784314, 0.5254901960784314)
outline.actor.property.diffuse_color = (0.5254901960784314, 0.5254901960784314, 0.5254901960784314)
outline.actor.property.specular_color = (0.5254901960784314, 0.5254901960784314, 0.5254901960784314)
outline.actor.property.color = (0.5254901960784314, 0.5254901960784314, 0.5254901960784314)
scene.scene.foreground = (0.5254901960784314, 0.5254901960784314, 0.5254901960784314)
camera_light = engine.scenes[0].scene.light_manager.lights[0]
camera_light.elevation = 0.0
camera_light.azimuth = 0.0
camera_light1 = engine.scenes[0].scene.light_manager.lights[1]
camera_light1.elevation = 0.0
camera_light1.azimuth = 0.0
camera_light1.intensity = 1.0
camera_light1.activate = False
camera_light2 = engine.scenes[0].scene.light_manager.lights[2]
camera_light2.elevation = 0.0
camera_light2.azimuth = 0.0
camera_light2.intensity = 1.0
camera_light2.activate = False
scene.scene.light_manager.light_mode = 'vtk'
camera_light1.activate = True
camera_light2.activate = True
camera_light.elevation = 45.0
camera_light.azimuth = 45.0
camera_light1.elevation = -30.0
camera_light1.azimuth = -60.0
camera_light1.intensity = 0.6
camera_light2.elevation = -30.0
camera_light2.azimuth = 60.0
camera_light2.intensity = 0.5
scene.scene.light_manager.light_mode = 'raymond'
camera_light.elevation = 44.3525
camera_light.elevation = 41.8825
camera_light.elevation = 40.6475
camera_light.elevation = 38.1775
camera_light.elevation = 36.952
camera_light.elevation = 32.012
camera_light.elevation = 30.777
camera_light.elevation = 29.541999999999994
camera_light.elevation = 28.307000000000002
camera_light.elevation = 27.0815
camera_light.elevation = 25.8465
camera_light.elevation = 27.0815
camera_light.elevation = 32.012
camera_light.elevation = 34.482
camera_light.elevation = 36.952
camera_light.elevation = 39.4125
camera_light.elevation = 41.8825
camera_light.elevation = 43.11749999999999
camera_light.elevation = 48.048
camera_light.elevation = 49.283
camera_light.elevation = 57.9185
camera_light.elevation = 59.15350000000001
camera_light.elevation = 60.38850000000001
camera_light.elevation = 59.15350000000001
camera_light.elevation = 57.9185
camera_light.elevation = 59.15350000000001
camera_light.elevation = 60.38850000000001
camera_light.elevation = 61.62350000000001
camera_light.elevation = 67.789
camera_light.elevation = 69.024
camera_light.elevation = 70.259
camera_light.elevation = 71.494
camera_light.elevation = 73.964
camera_light.elevation = 75.199
camera_light.elevation = 81.3645
camera_light.elevation = 82.5995
camera_light.elevation = 90.0
camera_light.elevation = 88.765
camera_light.elevation = 85.0695
camera_light.elevation = 83.8345
camera_light.elevation = 82.5995
camera_light.elevation = 81.3645
camera_light.elevation = 80.12950000000001
camera_light.elevation = 78.8945
camera_light.elevation = 77.6595
camera_light.elevation = 73.964
camera_light.azimuth = 44.45
camera_light.azimuth = 43.35
camera_light.azimuth = 42.25
camera_light.azimuth = 41.150000000000006
camera_light.azimuth = 40.050000000000004
camera_light.azimuth = 37.86
camera_light.azimuth = 36.760000000000005
camera_light.azimuth = 35.660000000000004
camera_light.azimuth = 33.46
camera_light.azimuth = 32.36
camera_light.azimuth = 31.259999999999998
camera_light.azimuth = 30.160000000000004
camera_light.azimuth = 29.07
camera_light.azimuth = 30.160000000000004
camera_light.azimuth = 35.660000000000004
camera_light.azimuth = 37.86
camera_light.azimuth = 49.949999999999996
camera_light.azimuth = 52.14
camera_light.azimuth = 63.129999999999995
camera_light.azimuth = 64.23
camera_light.azimuth = 71.92
camera_light.azimuth = 73.02
camera_light.azimuth = 84.01
camera_light.azimuth = 85.11
camera_light.azimuth = 95.0
camera_light.azimuth = 93.9
camera_light.azimuth = 90.6
camera_light.azimuth = 88.41000000000001
camera_light.azimuth = 86.21000000000001
camera_light.azimuth = 85.11
camera_light.azimuth = 81.81
camera_light.azimuth = 80.71
camera_light.azimuth = 78.52000000000001
camera_light.azimuth = 77.42
camera_light.azimuth = 76.32000000000001
camera_light.azimuth = 75.22
camera_light.azimuth = 73.02
camera_light.azimuth = 71.92
camera_light.azimuth = 70.82
camera_light.azimuth = 69.72999999999999
camera_light.azimuth = 68.63
camera_light.azimuth = 67.53
camera_light.azimuth = 63.129999999999995
camera_light.azimuth = 62.03
camera_light.azimuth = 60.93000000000001
outline.bounds = array([-2.        ,  2.        , -2.        ,  2.        , -1.        ,
        0.95918367])
outline.bounds = array([-2.        ,  2.        , -2.        ,  2.        , -1.        ,
        0.95918367])
outline.bounds = array([-2.,  2., -2.,  2., -1.,  1.])
outline.bounds = array([-2.,  2., -2.,  2., -1.,  1.])
axes.axes.bounds = array([-2.        ,  2.        , -2.        ,  2.        , -0.95918367,
        0.95918367])
axes.axes.ranges = array([-2.        ,  2.        , -2.        ,  2.        , -0.95918367,
        0.95918367])
axes.axes.position = array([0., 0.])
axes.axes.position2 = array([0.5, 0.5])
axes.axes.render_time_multiplier = 0.8565976078613765
axes.axes.x_axis_visibility = False
axes.axes.bounds = array([-2.        ,  2.        , -2.        ,  2.        , -0.95918367,
        0.95918367])
axes.axes.ranges = array([-2.        ,  2.        , -2.        ,  2.        , -0.95918367,
        0.95918367])
axes.axes.position = array([0., 0.])
axes.axes.position2 = array([0.5, 0.5])
axes.axes.z_axis_visibility = False
axes.axes.bounds = array([-2.        ,  2.        , -2.        ,  2.        , -0.95918367,
        0.95918367])
axes.axes.ranges = array([-2.        ,  2.        , -2.        ,  2.        , -0.95918367,
        0.95918367])
axes.axes.position = array([0., 0.])
axes.axes.position2 = array([0.5, 0.5])
axes.axes.y_axis_visibility = False
axes.axes.bounds = array([-2.        ,  2.        , -2.        ,  2.        , -1.        ,
        0.95918367])
axes.axes.ranges = array([-2.        ,  2.        , -2.        ,  2.        , -0.95918367,
        0.95918367])
axes.axes.position = array([0., 0.])
axes.axes.position2 = array([0.5, 0.5])
axes.axes.bounds = array([-2.        ,  2.        , -2.        ,  2.        , -1.        ,
        0.95918367])
axes.axes.bounds = array([-2.,  2., -2.,  2., -1.,  1.])
axes.axes.ranges = array([-2.        ,  2.        , -2.        ,  2.        , -0.95918367,
        0.95918367])
axes.axes.position = array([0., 0.])
axes.axes.position2 = array([0.5, 0.5])
axes.axes.render_time_multiplier = 0.8579723641610134
axes.axes.bounds = array([-2.,  2., -2.,  2., -1.,  1.])

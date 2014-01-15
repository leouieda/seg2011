"""
Set the view angle for all 3D plots
"""

size = (1100,700)
extent = [0,5000,0,5000,-1500,0]
ranges = [0,5,0,5,1.5,0]
    
def set(scene):
    scene.scene.camera.position = [5377.2383083185423, -4930.6087682500784, 4094.0809781064681]
    scene.scene.camera.focal_point = [2486.4918785408981, 1857.6635149318067, -1119.6733958620262]
    scene.scene.camera.view_angle = 30.0
    scene.scene.camera.view_up = [-0.12522480450371129, 0.57023927025396637, 0.81187802224055239]
    scene.scene.camera.clipping_range = [3015.0798335640284, 17232.434698622368]

    scene.scene.camera.compute_view_plane_normal()
    scene.scene.render()

def bbox(mlab):    
    w, e, s, n, b, t = extent
    p = mlab.pipeline.builtin_surface()
    p.source = 'outline'
    p.data_source.bounds = [w, e, n, n, b, t]
    p.data_source.generate_faces = 1
    su = mlab.pipeline.surface(p)
    su.actor.property.color = (0,0,0)
    su.actor.property.opacity = 0.05
    p = mlab.pipeline.builtin_surface()
    p.source = 'outline'
    p.data_source.bounds = [w, e, s, n, b, b]
    p.data_source.generate_faces = 1
    su = mlab.pipeline.surface(p)
    su.actor.property.color = (0,0,0)
    su.actor.property.opacity = 0.1
    

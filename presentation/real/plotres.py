import cPickle as pickle
try:
    from enthought.mayavi import mlab
except:
    from mayavi import mlab
from fatiando import vis
import fatiando.mesh
import view

def set_view(scene):
    scene.scene.camera.position = [-8566.0876939537393, -6038.9356883043183, 7776.3999627344283]
    scene.scene.camera.focal_point = [2451.3349609375, 3308.64501953125, 871.30499267578125]
    scene.scene.camera.view_angle = 30.0
    scene.scene.camera.view_up = [0.32263937892484157, 0.28619600793553562, 0.90221708929101718]
    scene.scene.camera.clipping_range = [8249.7338626025085, 25825.744453944932]
    scene.scene.camera.compute_view_plane_normal()
    scene.scene.render()

extent = view.extent
ranges = view.ranges

with open("res.pickle") as f:
	res = pickle.load(f)
with open("mesh.pickle") as f:
	mesh = fatiando.mesh.vfilter(pickle.load(f),0,999)
with open("seeds.pickle") as f:
    seeds = pickle.load(f)

scene = mlab.figure(size=(1200,800))
scene.scene.background = (1, 1, 1)
view.bbox(mlab)

engine = mlab.get_engine()

surfs = []

surfs.append(vis.plot_prism_mesh(res, style='surface', xy2ne=True))
engine.scenes[0].children[-1].children[0].children[0].children[0].scalar_lut_manager.data_range = [0,1000]

surfs.append(vis.plot_prism_mesh(mesh, style='surface', xy2ne=True))
engine.scenes[0].children[-1].children[0].children[0].children[0].scalar_lut_manager.lut_mode = "Greys"

surfs.append(vis.plot_prism_mesh(seeds, style='surface', xy2ne=True))
engine.scenes[0].children[-1].children[0].children[0].children[0].scalar_lut_manager.lut_mode = "Greys"
engine.scenes[0].children[-1].children[0].children[0].children[0].scalar_lut_manager.data_range = [0,1000]

o = mlab.outline(color=(0,0,0), extent=extent)
o.actor.property.line_width = 1

a = mlab.axes(surfs[0], nb_labels=7, extent=extent, ranges=ranges, color=(0,0,0))
a.label_text_property.color = (0,0,0)
a.title_text_property.color = (0,0,0)
a.property.line_width = 1
a.axes.label_format = "%-#.1f"
a.axes.x_label, a.axes.y_label, a.axes.z_label = "y (km)", "x (km)", "h (km)"

mlab.show()

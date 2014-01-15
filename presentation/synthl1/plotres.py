import cPickle as pickle
import numpy
from enthought.mayavi import mlab
from fatiando import vis, mesh
import view

with open("res.pickle") as f:
	res = pickle.load(f)
with open("seeds.pickle") as f:
	seeds = pickle.load(f)
with open("model.pickle") as f:
	model = pickle.load(f)

extent = view.extent
ranges = view.ranges

scene = mlab.figure(size=view.size)
scene.scene.background = (1, 1, 1)

p = vis.plot_prism_mesh(res, style='surface', xy2ne=True)
p.actor.property.line_width = 2
mlab.get_engine().scenes[0].children[-1].children[0].children[0].children[0].scalar_lut_manager.data_range = [0,1200]

p = vis.plot_prism_mesh(seeds, style='surface', xy2ne=True)
p.actor.property.line_width = 2
mlab.get_engine().scenes[0].children[-1].children[0].children[0].children[0].scalar_lut_manager.data_range = [0,1200]

p = vis.plot_prism_mesh(model, style='surface', xy2ne=True)
p.actor.property.line_width = 2

p = vis.plot_prism_mesh(mesh.vfilter(model,1100,1201), style='wireframe', xy2ne=True)
p.actor.property.color = (0,0,0)
p.actor.property.line_width = 3

mlab.outline(color=(0,0,0), extent=extent)

a = mlab.axes(p, nb_labels=5, extent=extent, ranges=ranges, color=(0,0,0))
a.label_text_property.color = (0,0,0)
a.title_text_property.color = (0,0,0)
a.property.line_width = 1
a.axes.label_format = "%-#.1f"
a.axes.x_label, a.axes.y_label, a.axes.z_label = "Y (km)", "X (km)", "Z (km)"

view.bbox(mlab)

view.set(scene)
mlab.show()

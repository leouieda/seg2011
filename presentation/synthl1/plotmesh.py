import cPickle as pickle
import numpy
from enthought.mayavi import mlab
from fatiando import vis, mesh
import view

x1, x2 = 0, 5000
y1, y2 = 0, 5000
z1, z2 = 0, 1500
pmesh = mesh.prism_mesh(x1=x1, x2=x2, y1=y1, y2=y2, z1=z1, z2=z2,
                                nx=50, ny=50, nz=15)
mesh.fill(numpy.zeros(pmesh.size), pmesh)


extent = view.extent
ranges = view.ranges

scene = mlab.figure(size=view.size)
scene.scene.background = (1, 1, 1)

p = vis.plot_prism_mesh(pmesh, style='surface', xy2ne=True)
p.actor.property.line_width = 2

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

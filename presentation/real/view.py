"""
Set the view angle for all 3D plots
"""
import cPickle as pickle

size = (600,600)
resolution = [8*x for x in size]

with open('extent.pickle') as f:
    extent = pickle.load(f)

ranges = [x*0.001 for x in extent]
    
profiles = [5550, 1750, 1350, 1100, 1000]
    
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
    
def bbox_top(mlab):    
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
    p.data_source.bounds = [e, e, s, n, b, t]
    p.data_source.generate_faces = 1
    su = mlab.pipeline.surface(p)
    su.actor.property.color = (0,0,0)
    su.actor.property.opacity = 0.2
    

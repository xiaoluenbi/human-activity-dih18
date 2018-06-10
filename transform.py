import dtcwt
import dtcwt.registration as registration
import numpy as np

transform2d = dtcwt.Transform2d()

#warped_src = registration.warp(src, reg, method='bilinear')
#vxs, vys = registration.velocityfield(reg, ref.shape[:2], method='bilinear')
#vxs = vxs*ref.shape[1]
#vys = vys*ref.shape[0]
#figure()
#X, Y = np.meshgrid(np.arange(ref.shape[1]), np.arange(ref.shape[0]))
#imshow(ref, cmap=cm.gray, clim=(0,1))
#step = 8

#quiver(X[::step,::step], Y[::step,::step],vxs[::step,::step], vys[::step,::step],color='g', angles='xy', scale_units='xy', scale=0.25)




def transform_dtcwt(ref,src):
	ref_t = transform2d.forward(ref, nlevels=6)
	src_t = transform2d.forward(src, nlevels=6)
	reg = registration.estimatereg(src_t, ref_t)
	vxs, vys = registration.velocityfield(reg, ref.shape[:2], method='bilinear')
	vxs = vxs*ref.shape[1]
	vys = vys*ref.shape[0]
	mesh=np.abs(vxs + 1j*vys)
	return mesh

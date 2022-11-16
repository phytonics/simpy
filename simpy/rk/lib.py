import np
from np.linalg import norm


"""
Brief Summary of Runge Kutta Method:

You analytically solve for the delta x in terms of delta t.


"""


def step(f, x, t, dt, **kwargs):
	"""
	One Step of 4th Order Runge-Kutta Method
	"""
	k = dt
	k1 = k * f(t, x, **kwargs)
	k2 = k * f(t + k/2, x + k1/2, **kwargs)
	k3 = k * f(t + k/2, x + k2/2, **kwargs)
	k4 = k * f(t + k, x + k3, **kwargs)
	return x + 1 / 6. * (k1 + 2 * k2 + 2 * k3 + k4)


def rk(f, t, x0, **kwargs):
	"""
	4th Order Runge-Kutta Method
	"""
	dts = t[1:] - t[:-1]
	if type(x0) == np.ndarray:
		x = np.zeros((len(t), *x0.shape))
	else: x = np.zeros((len(t), len(x0)))
	x[0] = x0
	for cnt, dt in enumerate(dts):
		x[cnt+1] = step(f, x[cnt], t[cnt], dt, **kwargs)
	return x

"""
An example of how to parallelize the step function: make x a matrix
in the following form:
[[x11 x12 x13 x14 x15 ...x1n]
 [x21 x22 x23 x24 x25 ...x2n]
 ...
 [xm1 xm2 xm3 xm4 xm5 ...xmn]
 [v11 v12 v13 v14 v15 ...v1n]
 [v21 v22 v23 v24 v25 ...v2n]
 ...
 [vm1 vm2 vm3 vm4 vm5 ...vmn]]

where xij is the position of object i in dimension j, and vij is velocity.

Denote this matrix as z.
"""

if __name__ == "__main__":
	"""
	n-body gravitational sim
	"""
        def zdot(t, z, G, m):
                n_bodies = z.shape[0] // 2
                assert n_bodies == len(m)
                ndim = z.shape[1]

                x = z[:n_bodies]
                # Outer Product to get all Pairs
                m_pairs = (m * m.reshape(-1, 1))[~np.eye(n_bodies, dtype=bool)].reshape(n_bodies, n_bodies-1)
                r_pairs = (x - x.reshape(n_bodies, 1, ndim))[~np.eye(n_bodies, dtype=bool)].reshape(n_bodies, n_bodies-1, ndim)

                
                F = (((G * m_pairs) / (norm(r, axis=2)**3)).reshape(n_bodies, n_bodies, 1) * r).sum(axis=1)
                return F
                






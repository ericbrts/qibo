from qibo import set_backend
from qibo.gates import PS, BS, PhotonicH
from qibo.models import PhotonicCircuit

pc = PhotonicCircuit(4)
pc.add(PhotonicH((0, 1)))
pc.add(PhotonicH((2, 3)))
pc.add(PS(0, 0.8))
pc.add(PhotonicH((0, 1)))

print(pc.summary())

set_backend("slos")
res = pc((1, 1, 1, 1), 1000)
print(res)

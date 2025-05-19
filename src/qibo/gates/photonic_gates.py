from .abstract import Gate, ParametrizedGate
import perceval as pcvl


class PhotonicGate:
    def __init__(self, wires: tuple[int, ...]):
        self._pcvl: pcvl.AComponent
        self._wires = wires

    @property
    def wires(self):
        return self._wires

    @property
    def photonic_component(self):
        return self._pcvl


class PS(ParametrizedGate, PhotonicGate):
    def __init__(self, wire: int, phi):
        if isinstance(phi, str):
            ParametrizedGate.__init__(self, trainable=True)
            self.parameter_names = phi
            self._pcvl = pcvl.PS(pcvl.Parameter(phi))
        else:
            ParametrizedGate.__init__(self, trainable=False)
            self._pcvl = pcvl.PS(phi)
        PhotonicGate.__init__(self, (wire,))
        self.control_qubits = (wire,)
        self.name = "Phase shifter"


class BS(ParametrizedGate, PhotonicGate):
    def __init__(self, wires: tuple[int, int], theta):
        if len(wires) != 2:
            raise ValueError("only 2 wires for a beam splitter in photonics")
        if isinstance(theta, str):
            ParametrizedGate.__init__(self, trainable=True)
            self.parameter_names = theta
            self._pcvl = pcvl.BS(pcvl.Parameter(theta))
        else:
            ParametrizedGate.__init__(self, trainable=False)
            self._pcvl = pcvl.BS(theta)
        PhotonicGate.__init__(self, tuple(wires))
        self.control_qubits = tuple(wires)
        self.name = "Beam splitter"


class PhotonicH(Gate, PhotonicGate):
    def __init__(self, wires: tuple[int, int]):
        super().__init__()
        if len(wires) != 2:
            raise ValueError("only 2 wires for H in photonics")
        self._pcvl = pcvl.BS.H()
        PhotonicGate.__init__(self, tuple(wires))
        self.control_qubits = tuple(wires)
        self.name = "Photonic H"

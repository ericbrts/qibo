from .abstract import Backend
from perceval import Experiment, Processor, BasicState, probs_to_samples


class PhotonicBackend(Backend):
    @property
    def qubits(self):  # pragma: no cover
        """Return the qubit names of the backend. If :class:`SimulationBackend`, return None."""
        raise NotImplementedError

    @property
    def connectivity(self):  # pragma: no cover
        """Return the available qubit pairs of the backend. If :class:`SimulationBackend`, return None."""
        raise NotImplementedError

    @property
    
    def natives(self):  # pragma: no cover
        """Return the native gates of the backend. If :class:`SimulationBackend`, return None."""
        raise NotImplementedError

    
    def set_precision(self, precision):  # pragma: no cover
        raise NotImplementedError

    
    def set_device(self, device):  # pragma: no cover
        raise NotImplementedError

    
    def set_threads(self, nthreads):  # pragma: no cover
        raise NotImplementedError

    
    def cast(self, x, copy=False):  # pragma: no cover
        raise NotImplementedError

    
    def is_sparse(self, x):  # pragma: no cover
        raise NotImplementedError

    
    def to_numpy(self, x):  # pragma: no cover
        raise NotImplementedError

    
    def compile(self, func):  # pragma: no cover
        raise NotImplementedError

    
    def zero_state(self, nqubits):  # pragma: no cover
        raise NotImplementedError

    
    def zero_density_matrix(self, nqubits):  # pragma: no cover
        raise NotImplementedError

    
    def identity_density_matrix(self, nqubits, normalize: bool = True):  # pragma: no cover
        raise NotImplementedError

    
    def plus_state(self, nqubits):  # pragma: no cover
        """Generate :math:`|+++\\cdots+\\rangle` state vector as an array."""
        raise NotImplementedError

    
    def plus_density_matrix(self, nqubits):  # pragma: no cover
        raise NotImplementedError

    
    def matrix(self, gate):  # pragma: no cover
        raise NotImplementedError

    
    def matrix_parametrized(self, gate):  # pragma: no cover
        raise NotImplementedError

    
    def matrix_fused(self, gate):  # pragma: no cover
        raise NotImplementedError

    
    def apply_gate(self, gate, state, nqubits):  # pragma: no cover
        raise NotImplementedError

    
    def apply_gate_density_matrix(self, gate, state, nqubits):  # pragma: no cover
        raise NotImplementedError

    
    def apply_gate_half_density_matrix(self, gate, state, nqubits):  # pragma: no cover
        raise NotImplementedError

    
    def apply_channel(self, channel, state, nqubits):  # pragma: no cover
        raise NotImplementedError

    
    def apply_channel_density_matrix(self, channel, state, nqubits):  # pragma: no cover
        raise NotImplementedError

    
    def collapse_state(
            self, state, qubits, shot, nqubits, normalize=True
    ):  # pragma: no cover
        raise NotImplementedError

    
    def collapse_density_matrix(self, state, qubits, shot, nqubits, normalize=True):  # pragma: no cover
        raise NotImplementedError

    
    def reset_error_density_matrix(self, gate, state, nqubits):  # pragma: no cover
        raise NotImplementedError

    
    def thermal_error_density_matrix(self, gate, state, nqubits):  # pragma: no cover
        raise NotImplementedError

    
    def execute_circuit(self, circuit, initial_state=None, nshots=None):  # pragma: no cover
        raise NotImplementedError

    
    def execute_circuits(self, circuits, initial_states=None, nshots=None):  # pragma: no cover
        raise NotImplementedError

    
    def execute_circuit_repeated(self, circuit, nshots, initial_state=None):  # pragma: no cover
        raise NotImplementedError

    
    def execute_distributed_circuit(self, circuit, initial_state=None, nshots=None):  # pragma: no cover
        raise NotImplementedError

    
    def calculate_symbolic(self, state, nqubits, decimals=5, cutoff=1e-10, max_terms=20):  # pragma: no cover
        raise NotImplementedError

    
    def calculate_symbolic_density_matrix(self, state, nqubits, decimals=5, cutoff=1e-10, max_terms=20):  # pragma: no cover
        raise NotImplementedError

    
    def calculate_probabilities(self, state, qubits, nqubits):  # pragma: no cover
        raise NotImplementedError

    
    def calculate_probabilities_density_matrix(self, state, qubits, nqubits):  # pragma: no cover
        raise NotImplementedError

    
    def set_seed(self, seed):  # pragma: no cover
        raise NotImplementedError

    
    def sample_shots(self, probabilities, nshots):  # pragma: no cover
        raise NotImplementedError

    
    def aggregate_shots(self, shots):  # pragma: no cover
        raise NotImplementedError

    
    def samples_to_binary(self, samples, nqubits):  # pragma: no cover
        raise NotImplementedError

    
    def samples_to_decimal(self, samples, nqubits):  # pragma: no cover
        raise NotImplementedError

    
    def calculate_frequencies(self, samples):  # pragma: no cover
        raise NotImplementedError

    
    def update_frequencies(self, frequencies, probabilities, nsamples):  # pragma: no cover
        raise NotImplementedError

    
    def sample_frequencies(self, probabilities, nshots):  # pragma: no cover
        raise NotImplementedError

    
    def calculate_vector_norm(self, state, order=2):  # pragma: no cover
        raise NotImplementedError

    
    def calculate_matrix_norm(self, state, order="nuc"):  # pragma: no cover
        raise NotImplementedError

    
    def calculate_overlap(self, state1, state2):  # pragma: no cover
        raise NotImplementedError

    
    def calculate_overlap_density_matrix(self, state1, state2):  # pragma: no cover
        raise NotImplementedError

    
    def calculate_eigenvalues(
            self, matrix, k: int = 6, hermitian: bool = True
    ):  # pragma: no cover
        raise NotImplementedError

    
    def calculate_eigenvectors(self, matrix, k: int = 6, hermitian: bool = True):  # pragma: no cover
        raise NotImplementedError

    
    def calculate_expectation_state(self, hamiltonian, state, normalize):  # pragma: no cover
        raise NotImplementedError

    
    def calculate_expectation_density_matrix(self, hamiltonian, state, normalize):  # pragma: no cover
        raise NotImplementedError

    
    def calculate_matrix_exp(self, a, matrix, eigenvectors=None, eigenvalues=None):  # pragma: no cover
        raise NotImplementedError

    
    def calculate_matrix_power(self, matrix, power, precision_singularity: float = 1e-14):  # pragma: no cover
        raise NotImplementedError

    
    def calculate_singular_value_decomposition(self, matrix):  # pragma: no cover
        raise NotImplementedError

    
    def calculate_jacobian_matrix(
            self, circuit, parameters, initial_state=None, return_complex: bool = True
    ):  # pragma: no cover
        raise NotImplementedError

    
    def assert_allclose(self, value, target, rtol=1e-7, atol=0.0):  # pragma: no cover
        raise NotImplementedError


class SlosBackend(PhotonicBackend):

    def __init__(self):
        super().__init__()
        self.name = "slos"

    def execute_circuit(self, circuit: Experiment, initial_state=None, nshots=None):
        experiment = circuit
        if initial_state is not None:
            experiment.with_input(BasicState(initial_state))
        p = Processor("SLOS", experiment)
        distrib = p.probs()
        distrib["results"] = probs_to_samples(distrib["results"], nshots)
        return distrib



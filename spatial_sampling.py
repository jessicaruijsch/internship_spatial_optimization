import numpy as np
from pymoo.model.sampling import Sampling
import initial_population

class SpatialSampling(Sampling):
    """
    Randomly sample points in the real space by considering the lower and upper bounds of the problem.
    """

    def __init__(self, var_type=np.float,default_dir=None) -> None:
        super().__init__()
        self.var_type = var_type
        self.default_dir = default_dir

    def _do(self, problem, n_samples, **kwargs):
        landusemaps_np = initial_population.initialize_spatial(n_samples, self.default_dir)
        return landusemaps_np

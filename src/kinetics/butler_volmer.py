import importlib
import math

constants = importlib.import_module("utils.electrochemistry_constants")


class ButlerVolmer(object):
    def bv_multi_electron(self, i0, alpha_a, alpha_c, overpotential, temperature, z):
        """
        Return electrode current density as a function of exchange current density,
        charge transfer coefficients, overpotential, temperature and electrons involved
        in the reaction.

        Arguments:
            i0: float
            alpha_a: float
            alpha_c: float
            overpotential: float
            temperature: float
            z: int

        Returns:
            i: float

        """
        f = constants.F / (constants.R * temperature)
        i = i0 * (
            math.exp(f * overpotential * alpha_a * z)
            - math.exp(-f * overpotential * alpha_c * z)
        )
        return i

    def tafel_approximation(self):
        pass

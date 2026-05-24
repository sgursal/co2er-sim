import math

from src.utils.electrochemistry_constants import Constants


class ButlerVolmer(object):
    def multi_electron(self, i0, alpha_a, alpha_c, overpotential, temperature, z):
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
        f = Constants.FARADAY_CONSTANT / (Constants.GAS_CONSTANT * temperature)
        i = i0 * (
            math.exp(f * overpotential * alpha_a * z)
            - math.exp(-f * overpotential * alpha_c * z)
        )
        return i

    def tafel_approximation(self):
        pass

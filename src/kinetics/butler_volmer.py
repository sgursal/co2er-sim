import numpy as np

from src.utils.electrochemistry_constants import FARADAY_CONSTANT, GAS_CONSTANT


def compute_current_density(
    overpotential: float,
    exchange_current_density: float,
    anodic_transfer_coefficient: float,
    cathodic_transfer_coefficient: float,
    temperature: float,
    n_electrons: int = 2,
) -> float:
    """
    Compute electrode current density using the Butler-Volmer equation.

    Parameters
    ----------
    overpotential : float
        Electrode overpotential eta in V. Negative for reduction.
    exchange_current_density : float
        Exchange current density j0 in A/m².
    anodic_transfer_coefficient : float
        Anodic charge transfer coefficient alpha_a. Dimensionless.
    cathodic_transfer_coefficient : float
        Cathodic charge transfer coefficient alpha_c. Dimensionless.
    temperature : float
        Electrolyte temperature T in K.
    n_electrons : int, optional
        Electrons transferred per reaction event. Default 2 for CO2->CO.

    Returns
    -------
    float
        Net current density j in A/m². Negative indicates reduction.
    """
    thermal_voltage = (GAS_CONSTANT * temperature) / FARADAY_CONSTANT

    anodic_exponent = (
        anodic_transfer_coefficient * n_electrons * overpotential / thermal_voltage
    )
    cathodic_exponent = (
        -cathodic_transfer_coefficient * n_electrons * overpotential / thermal_voltage
    )
    net_current_density = float(
        exchange_current_density * (np.exp(anodic_exponent) - np.exp(cathodic_exponent))
    )

    return net_current_density


def compute_tafel_current_density(
    overpotential: float,
    exchange_current_density: float,
    cathodic_transfer_coefficient: float,
    temperature: float,
    n_electrons: int = 2,
) -> float:
    """
    Compute cathodic current density using the Tafel approximation.

    Valid at large cathodic overpotentials where the anodic term is negligible.

    Parameters
    ----------
    overpotential : float
        Electrode overpotential eta in V. Must be negative.
    exchange_current_density : float
        Exchange current density j0 in A/m².
    cathodic_transfer_coefficient : float
        Cathodic charge transfer coefficient alpha_c. Dimensionless.
    temperature : float
        Electrolyte temperature T in K.
    n_electrons : int, optional
        Electrons transferred per reaction event. Default 2.

    Returns
    -------
    float
        Cathodic current density in A/m².
    """
    thermal_voltage = GAS_CONSTANT * temperature / FARADAY_CONSTANT
    cathodic_exponent = (
        -cathodic_transfer_coefficient * n_electrons * overpotential / thermal_voltage
    )
    cathodic_current_density = float(
        -exchange_current_density * np.exp(cathodic_exponent)
    )

    return cathodic_current_density

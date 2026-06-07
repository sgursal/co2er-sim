from dataclasses import dataclass


@dataclass
class ReactorResults:
    # Electrical
    current_density_total: float  # A/m²
    current_density_co2r: float  # A/m²
    current_density_her: float  # A/m²

    # Selectivity
    faradaic_efficiency_co2r: float  # dimensionless, 0 to 1
    faradaic_efficiency_her: float  # dimensionless, 0 to 1

    # Transport
    co2_surface_concentration: float  # mol/m³
    surface_ph: float  # dimensionless

    # Thermodynamics
    equilibrium_potential: float  # V
    overpotential: float  # V

    # Energy
    energy_consumption_kwh_per_mol: float  # kWh/mol product

    # Convergence
    converged: bool
    iterations: int

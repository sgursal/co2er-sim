from dataclasses import dataclass


@dataclass
class ReactorConfig:
    # Electrical
    cell_voltage: float  # V

    # Thermal
    temperature: float  # K

    # Feed composition
    co2_bulk_concentration: float  # mol/m³
    pressure: float  # Pa

    # Electrolyte
    bulk_ph: float  # dimensionless
    electrolyte_conductivity: float  # S/m

    # Electrode geometry
    electrode_area: float  # m²
    boundary_layer_thickness: float  # m

    # CO2R catalyst parameters
    j0_co2r: float  # A/m²
    alpha_a_co2r: float  # dimensionless
    alpha_c_co2r: float  # dimensionless
    n_electrons_co2r: int  # dimensionless

    # HER catalyst parameters
    j0_her: float  # A/m²
    alpha_a_her: float  # dimensionless
    alpha_c_her: float  # dimensionless

    # Bubble correction
    bubble_correction: bool = False

    # Solver settings
    max_iterations: int = 100
    convergence_tolerance: float = 1e-6

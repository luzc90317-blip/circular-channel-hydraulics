# Hydraulic Calculations Module

class HydraulicCalculations:
    def __init__(self, diameter, flow_rate):
        self.diameter = diameter  # Diameter of the pipe in meters
        self.flow_rate = flow_rate  # Flow rate in cubic meters per second

    def calculate_velocity(self):
        # Calculate the velocity of the fluid in the pipe
        area = (3.14159 / 4) * (self.diameter ** 2)
        return self.flow_rate / area

    def calculate_reynolds_number(self, viscosity):
        # Calculate the Reynolds number
        velocity = self.calculate_velocity()
        return (self.diameter * velocity) / viscosity

    def calculate_friction_factor(self, roughness):
        # Calculate the Darcy-Weisbach friction factor (for simplicity, using the Colebrook equation)
        from scipy.optimize import fsolve
        def colebrook(f):
            return 1 / (f ** 0.5) + 2.0 * roughness / self.diameter * (1 / (f ** 0.5))

        f_initial_guess = 0.02
        friction_factor = fsolve(colebrook, f_initial_guess)[0]
        return friction_factor

    def calculate_pressure_loss(self, length, roughness):
        # Calculate the pressure loss due to friction in the pipe
        friction_factor = self.calculate_friction_factor(roughness)
        velocity = self.calculate_velocity()
        density = 1000  # Assume water with density of 1000 kg/m^3
        return (friction_factor * length * density * (velocity ** 2)) / (2 * self.diameter)
solid_point = 0
gas_point = 100


def state_checker(temperature):
    if temperature <= solid_point:
        return "Solid"
    elif solid_point < temperature < gas_point:
        return "liquid"
    else:
        return "Gas"

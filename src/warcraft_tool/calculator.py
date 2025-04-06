
def convert_strength_to_attack_power(strength:int):

    # for paladin
    attack_power = strength * 2 - 20
    return attack_power

def calculate_actual_damage(multiplier, attack_power):

    if isinstance(multiplier, str) and multiplier.endswith('%'):
        multiplier = int(multiplier.replace('%','')) / 100

    return int(multiplier*attack_power)
    
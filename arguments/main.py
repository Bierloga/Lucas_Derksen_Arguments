# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def greet(name, template = None):
    if template == None:
        return f'Hello, {name}!'
    if template != None:
        template = template.replace("<name>", f'{name}')
        return f'{template}'

def force(mass, body="earth"):
    bodies = {
        "sun": 274,
        "mercury": 3.7,
        "venus": 8.8,
        "earth": 9.8,
        "mars": 3.7,
        "jupiter": 24.9,
        "neptune": 11.1,
        "saturn": 10.4,
        "uranus": 8.8,
        "moon": 1.6,
        "pluto": 0.6
    }
    return mass*bodies[body]

def pull(m1, m2, d):
    return 6.674*(10**-11)*((m1*m2)/(d**2))





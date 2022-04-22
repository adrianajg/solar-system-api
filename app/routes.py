from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, gravity):
        self.id = id
        self.name = name
        self.description = description
        self.gravity = gravity
    
planets = [
    Planet(1, "Mercury", "Smallest and closest to sun", 3.7),
    Planet(2, "Venus", "Brightest object in the Earth's night sky", 8.8),
    Planet(3, "Earth", "Big blue ball, lots of water", 9.8),
    Planet(4, "Mars", "Baren red rock", 3.7),
    Planet(5, "Jupiter", "Enormous gas giant", 24.8),
    Planet(6, "Saturn", "Pretty rings", 10.4),
    Planet(7, "Uranus", "Unfortunately named", 8.9),
    Planet(8, "Neptune", "Smallest gas giant", 11.2),
    Planet(9, "Pluto", "Not really a planet", 0.6)
]

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.route("", methods = ["GET"])
def handle_planets():
    planets_response = []
    for planet in planets:
        planets_response.append(dict(
            id=planet.id,
            name=planet.name,
            description=planet.description,
            gravity=planet.gravity
        ))

    return jsonify(planets_response)
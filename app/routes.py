from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request

# class Planet:
#     def __init__(self, id, name, description, gravity):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.gravity = gravity

#     def to_dict(self):
#         return dict(
#             id=self.id,
#             name=self.name,
#             description=self.description,
#             gravity=self.gravity,
#         )
    
# planets = [
#     Planet(1, "Mercury", "Smallest and closest to sun", 3.7),
#     Planet(2, "Venus", "Brightest object in the Earth's night sky", 8.8),
#     Planet(3, "Earth", "Big blue ball, lots of water", 9.8),
#     Planet(4, "Mars", "Baren red rock", 3.7),
#     Planet(5, "Jupiter", "Enormous gas giant", 24.8),
#     Planet(6, "Saturn", "Pretty rings", 10.4),
#     Planet(7, "Uranus", "Unfortunately named", 8.9),
#     Planet(8, "Neptune", "Smallest gas giant", 11.2),
#     Planet(9, "Pluto", "Not really a planet", 0.6)
# ]

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

# GET /planets
@planets_bp.route("", methods = ["GET"])
def read_all_planets():
    all_planets = Planet.query.all()
    result_list = [planet.to_dict() for planet in all_planets]

    return make_response(jsonify(result_list), 200)

def get_valid_planet(id):
    try:
        id = int(id)
    except ValueError:
        abort(make_response(jsonify(dict(details=f"invalid id: {id}")), 400))

    planet = Planet.query.get(id)
    
    if not planet:
        abort(make_response(jsonify(dict(details=f"planet id {id} not found")), 404))    

    return planet

@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    if "name" and "description" and "gravity" not in request_body:
        return make_response(f"Invalid request", 400)

    new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        gravity=request_body["gravity"]
                        )
    
    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} successfully created", 201)


# GET /planets/id
@planets_bp.route("/<id>", methods=("GET",))
def get_planet(id):
    planet = validate_planet(id)
    return jsonify(planet.to_dict())

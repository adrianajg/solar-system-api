from app import db
from app.models.planet import Planet
from flask import Blueprint, jsonify, abort, make_response, request
from .routes_helper import error_message

planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

def make_planet_safely(data_dict):
    try:
        return Planet.from_dict(data_dict)
    except KeyError as err:
        error_message(f"Missing key: {err}", 400)

def replace_planet_safely(planet, data_dict):
    try:
        planet.replace_details(data_dict)
    except KeyError as err:
        error_message(f"Missing key: {err}", 400)

def get_planet_record_by_id(id):
    try:
        id = int(id)
    except ValueError:
        error_message(f"Invalid id {id}", 400)

    planet = Planet.query.get(id)

    if planet:
        return planet
    
    error_message(f"No planet with id {id} found", 404)

# GET /planets
@planets_bp.route("", methods = ["GET"])
def read_all_planets():
    name_param = request.args.get("name")

    if name_param:
        planets = Planet.query.filter_by(name=name_param.capitalize())
        
    else:
        planets = Planet.query.all()

    result_list = [planet.to_dict() for planet in planets]

    if not result_list:
        return jsonify("No planets found with that name."), 200
    return jsonify(result_list)


# CREATE /planets
@planets_bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()

    planet = make_planet_safely(request_body)

    db.session.add(planet)
    db.session.commit()

    return jsonify(f"Planet {planet.name} successfully created"), 201


# GET /planets/id
@planets_bp.route("/<id>", methods=("GET",))
def read_planet_by_id(id):
    planet = get_planet_record_by_id(id)
    return jsonify(planet.to_dict())

# UPDATE /planets/id
@planets_bp.route("/<id>", methods=["PUT"])
def replace_planet_by_id(id):
    planet = get_planet_record_by_id(id)
    request_body = request.get_json()

    replace_planet_safely(planet, request_body)
    
    db.session.commit()

    return jsonify(f"Planet #{planet.id} successfully updated. \
    Planet: {planet.to_dict()}")

@planets_bp.route("/<id>", methods = ["DELETE"])
def delete_planet_by_id(id):
    planet = get_planet_record_by_id(id)

    db.session.delete(planet)
    db.session.commit()

    return jsonify(f"Planet #{planet.id} successfully deleted.")

@planets_bp.route("/<id>", methods = ["PATCH"])
def update_planet_with_id(id):
    planet = get_planet_record_by_id(id)
    request_body = request.get_json()
    planet_keys = request_body.keys()

    if "name" in planet_keys:
        planet.name = request_body["name"]
    if "description" in planet_keys:
        planet.description = request_body["description"]
    if "gravity" in planet_keys:
        planet.gravity = request_body["gravity"]

    db.session.commit()
    return jsonify(planet.to_dict())

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

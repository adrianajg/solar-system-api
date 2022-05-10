from app import db

class Moon(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    size = db.Column(db.Float, nullable=False)
    description = db.Column(db.String, nullable=False)
    gravity = db.Column(db.Float, nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    planet = db.relationship("Planet", back_populates="moons")

    def to_dict(self):
        planet_name = self.planet.name if self.planet else ""

        moon_dict = dict(
            id = self.id,
            name = self.name,
            description = self.description,
            size = self.size,
            gravity = self.gravity,
            planet=planet_name
        )
        return moon_dict

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            name = data_dict["name"],
            description = data_dict["description"],
            gravity = data_dict["gravity"],
            size = data_dict["size"]
            
        )

    def replace_details(self, data_dict):
        self.name = data_dict["name"]
        self.description = data_dict["description"]
        self.gravity = data_dict["gravity"]
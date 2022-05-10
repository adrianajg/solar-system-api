from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    gravity = db.Column(db.Float, nullable=False)
    moons = db.relationship("Moon", back_populates="planet")

    def to_dict(self):
        moons_info = [moon.to_dict() for moon in self.moons]

        planet_dict = dict(
            id = self.id,
            name = self.name,
            description = self.description,
            gravity = self.gravity,
            moons = moons_info
        )
        return planet_dict

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            name = data_dict["name"],
            description = data_dict["description"],
            gravity = data_dict["gravity"]
        )

    def replace_details(self, data_dict):
        self.name = data_dict["name"]
        self.description = data_dict["description"]
        self.gravity = data_dict["gravity"]
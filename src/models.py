from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    birth_year = db.Column(db.String(250), unique=True, nullable=False)
    eye_color = db.Column(db.String(250), unique=True, nullable=False)
    gender = db.Column(db.String(250), unique=True, nullable=False)
    hair_color = db.Column(db.String(250), unique=True, nullable=False)
    height = db.Column(db.String(250), unique=True, nullable=False)
    homeworld_id = db.Column(db.Integer, db.ForeignKey('planets.id'), nullable=False)
    homeworld = db.relationship("Planets")
    mass = db.Column(db.String(250), unique=True, nullable=False)
    skin_color = db.Column(db.String(250), unique=True, nullable=False)
    url = db.Column(db.String(250), unique=True, nullable=False)
    created = db.Column(db.String(250), unique=True, nullable=False)
    edited = db.Column(db.String(250), unique=True, nullable=False)

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            # do not serialize the password, its a security breach
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    diameter = db.Column(db.String(250), unique=True, nullable=False)
    rotation_period = db.Column(db.String(250), unique=True, nullable=False)
    orbital_period = db.Column(db.String(250), unique=True, nullable=False)
    gravity = db.Column(db.String(250), unique=True, nullable=False)
    population = db.Column(db.String(250), unique=True, nullable=False)
    climate = db.Column(db.String(250), unique=True, nullable=False)
    tarrain = db.Column(db.String(250), unique=True, nullable=False)
    usrface_water = db.Column(db.String(250), unique=True, nullable=False)
    url = db.Column(db.String(250), unique=True, nullable=False)
    created = db.Column(db.String(250), unique=True, nullable=False)
    edited = db.Column(db.String(250), unique=True, nullable=False)

    def __repr__(self):
        return f'<Planets {self.name}-{self.id}> '

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            # do not serialize the password, its a security breach
        }


class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    model = db.Column(db.String(250), unique=True, nullable=False)
    vehicle_class = db.Column(db.String(250), unique=True, nullable=False)
    manufacturer = db.Column(db.String(250), unique=True, nullable=False)
    lenght = db.Column(db.String(250), unique=True, nullable=False)
    cost_in_credits = db.Column(db.String(250), unique=True, nullable=False)
    crew = db.Column(db.String(250), unique=True, nullable=False)
    passengers = db.Column(db.String(250), unique=True, nullable=False)
    max_atmosphering_speed = db.Column(db.String(250), unique=True, nullable=False)
    cargo_capacity = db.Column(db.String(250), unique=True, nullable=False)
    consumables = db.Column(db.String(250), unique=True, nullable=False)
    url = db.Column(db.String(250), unique=True, nullable=False)
    created = db.Column(db.String(250), unique=True, nullable=False)
    edited = db.Column(db.String(250), unique=True, nullable=False)

    def __repr__(self):
        return '<Vehicles %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            # do not serialize the password, its a security breach
        }
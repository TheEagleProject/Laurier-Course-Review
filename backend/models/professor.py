from backend import db
class Professor(db.Model):
    __tablename__ = 'professors'
    id = db.Column(db.Integer, primary_key=True)
    professor_name = db.Column(db.String(256), unique = True, nullable = False)
    department = db.Column(db.String(256), nullable = False)

    reviews = db.relationship('Review', backref='professor', lazy=True)

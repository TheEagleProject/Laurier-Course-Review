from backend import db
class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    course_code = db.Column(db.String(256), unique = True, nullable = False)
    course_name = db.Column(db.String(256), nullable = False)
    department = db.Column(db.String(256), nullable = False)

    reviews = db.relationship('Review', backref='courseCode', lazy=True)

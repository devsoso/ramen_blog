from app import db

class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True, default='')
    thumbnail = db.Column(db.String, nullable=True, default='')

    def __repr__(self):
        return '<Store name={}>'.format(self.name)

    def row2dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'thumbnail': self.thumbnail
        }


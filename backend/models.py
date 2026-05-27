from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Loan(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def to_dict(self):

        return {
            "id": self.id,
            "customer": self.customer,
            "amount": self.amount,
            "status": self.status
        }
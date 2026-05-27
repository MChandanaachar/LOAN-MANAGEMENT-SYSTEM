from flask import jsonify, request
from models import db, Loan
   
from flask_jwt_extended import (
    create_access_token,
    jwt_required
)

def register_routes(app):

 # ADMIN LOGIN
    @app.route('/login', methods=['POST'])
    def login():

        data = request.json

        username = data.get("username")
        password = data.get("password")

        # SIMPLE ADMIN LOGIN
        if username == "admin" and password == "admin123":

            token = create_access_token(identity=username)

            return jsonify({
                "message": "Login Successful",
                "token": token
            })

        return jsonify({
            "error": "Invalid username or password"
        }), 401

    # HOME ROUTE
    @app.route('/')
    def home():
        return "Loan API Working"


    # GET ALL LOANS + FILTER
    @app.route('/loans', methods=['GET'])
    def get_loans():

        status = request.args.get("status")

        if status:
            loans = Loan.query.filter_by(status=status).all()
        else:
            loans = Loan.query.all()

        return jsonify([loan.to_dict() for loan in loans])


    # ADD LOAN
    @jwt_required()
    @app.route('/loans', methods=['POST'])
    def add_loan():

        data = request.json

        # VALIDATION
        if not data.get("customer"):
            return jsonify({
                "error": "Customer name is required"
            }), 400

        if data.get("amount", 0) <= 0:
            return jsonify({
                "error": "Amount must be greater than 0"
            }), 400

        if not data.get("status"):
            return jsonify({
                "error": "Status is required"
            }), 400


        new_loan = Loan(
            customer=data["customer"],
            amount=data["amount"],
            status=data["status"]
        )

        db.session.add(new_loan)
        db.session.commit()

        return jsonify({
            "message": "Loan Added Successfully",
            "loan": new_loan.to_dict()
        }), 201


    # UPDATE LOAN
    @jwt_required()
    @app.route('/loans/<int:id>', methods=['PUT'])
    def update_loan(id):

        loan = Loan.query.get(id)

        if not loan:
            return jsonify({
                "error": "Loan Not Found"
            }), 404

        data = request.json

        if data.get("amount", 0) <= 0:
            return jsonify({
                "error": "Invalid loan amount"
            }), 400

        loan.customer = data["customer"]
        loan.amount = data["amount"]
        loan.status = data["status"]

        db.session.commit()

        return jsonify({
            "message": "Loan Updated Successfully",
            "loan": loan.to_dict()
        })


    # DELETE LOAN
    @jwt_required()
    @app.route('/loans/<int:id>', methods=['DELETE'])
    def delete_loan(id):

        loan = Loan.query.get(id)

        if not loan:
            return jsonify({
                "error": "Loan Not Found"
            }), 404

        db.session.delete(loan)
        db.session.commit()

        return jsonify({
            "message": "Loan Deleted Successfully"
        })


    # HANDLE SERVER ERROR
    @app.errorhandler(500)
    def internal_error(error):

        return jsonify({
            "error": "Internal Server Error"
        }), 500
 


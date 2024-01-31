
# Import Flask, its render_template function, and other modules
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask app
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cakes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Cake model
class Cake(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255))
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(255))

# Define the CartItem model
class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cake_id = db.Column(db.Integer, db.ForeignKey('cake.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Create the database tables
db.create_all()

# Route for the homepage
@app.route('/')
def index():
    cakes = Cake.query.all()
    return render_template('index.html', cakes=cakes)

# Route for displaying all cakes
@app.route('/shop')
def shop():
    cakes = Cake.query.all()
    return render_template('shop.html', cakes=cakes)

# Route for adding a cake to the cart
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    cake_id = request.form['cake_id']
    quantity = int(request.form['quantity'])

    # Check if the cake is already in the cart
    cart_item = CartItem.query.filter_by(cake_id=cake_id).first()
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = CartItem(cake_id=cake_id, quantity=quantity)
        db.session.add(cart_item)

    # Save changes to the database
    db.session.commit()

    return redirect(url_for('cart'))

# Route for displaying the cart
@app.route('/cart')
def cart():
    cart_items = CartItem.query.all()
    return render_template('cart.html', cart_items=cart_items)

# Route for updating the quantity of a cake in the cart
@app.route('/update_cart', methods=['POST'])
def update_cart():
    cake_id = request.form['cake_id']
    quantity = int(request.form['quantity'])

    # Get the cart item
    cart_item = CartItem.query.get(cake_id)

    # Update the quantity
    cart_item.quantity = quantity

    # Save changes to the database
    db.session.commit()

    return redirect(url_for('cart'))

# Route for removing a cake from the cart
@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    cake_id = request.form['cake_id']

    # Get the cart item
    cart_item = CartItem.query.get(cake_id)

    # Delete the cart item
    db.session.delete(cart_item)

    # Save changes to the database
    db.session.commit()

    return redirect(url_for('cart'))

# Route for the checkout page
@app.route('/checkout')
def checkout():
    cart_items = CartItem.query.all()
    return render_template('checkout.html', cart_items=cart_items)

# Route for placing an order
@app.route('/place_order', methods=['POST'])
def place_order():
    # Get the user information and shipping address
    name = request.form['name']
    address = request.form['address']
    city = request.form['city']
    zip_code = request.form['zip_code']

    # Create a new order
    order = Order(name=name, address=address, city=city, zip_code=zip_code)
    db.session.add(order)

    # Add the cart items to the order
    cart_items = CartItem.query.all()
    for cart_item in cart_items:
        order_item = OrderItem(order_id=order.id, cake_id=cart_item.cake_id, quantity=cart_item.quantity)
        db.session.add(order_item)

    # Empty the cart
    CartItem.query.delete()

    # Save changes to the database
    db.session.commit()

    return render_template('order_confirmation.html', order=order)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

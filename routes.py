from flask import render_template, request, redirect, url_for
from app import app, db
from models import RestaurantReview

@app.route('/')
def index():
    return render_template('index.html')




@app.route('/view')
def view():
    return render_template('view.html')

@app.route('/donaldrev')
def donaldrev():
    reviews = RestaurantReview.query.order_by(RestaurantReview.time_created.desc()).all()
    return render_template('donaldrev.html', reviews=reviews)

@app.route('/add_review', methods=['GET', 'POST'])
def add_review():
    if request.method == 'POST':
        new_review = RestaurantReview(
            Restaurant_name=request.form['Restaurant_name'],
            review=request.form['review'],
            rating=float(request.form['rating'])
        )
        
        db.session.add(new_review)
        db.session.commit()
        
        return redirect(url_for('index'))
    
    return render_template('add_review.html')
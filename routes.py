
from flask import render_template, request, redirect, url_for
from app import app, db
from models import RestaurantReview

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    # Query all reviews from the database, ordered by time_created (newest first)
    reviews = RestaurantReview.query.order_by(RestaurantReview.time_created.desc()).all()
    return render_template('data.html', reviews=reviews)

@app.route('/add_review', methods=['GET', 'POST'])
def add_review():
    if request.method == 'POST':
        new_review = RestaurantReview(
            movie_name=request.form['restaurant_name'],
            review=request.form['review'],
            rating=float(request.form['rating'])
        )


        
        db.session.add(new_review)
        db.session.commit()

        
        return redirect(url_for('data'))
    
    return render_template('add_review.html')

@app.route('/edit_review/<int:review_id>', methods=['GET', 'POST'])
def edit_review(review_id):
    review = RestaurantReview.query.get_or_404(review_id)

        
 
    if request.method == 'POST':
        review.movie_name = request.form['restaurant_name']
        review.review = request.form['review']
        review.rating = float(request.form['rating'])
        
        db.session.commit()
        return redirect(url_for('data'))
    
    return render_template('edit_review.html', review=review)

@app.route('/delete_review/<int:review_id>', methods=['POST'])
def delete_review(review_id):
    review = RestaurantReview.query.get_or_404(review_id)
    db.session.delete(review)
    db.session.commit()
    return redirect(url_for('data'))










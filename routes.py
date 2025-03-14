
from flask import render_template, request, redirect, url_for
from sqlalchemy import func
from app import app, db
from models import RestaurantReview






@app.route('/')
def index():
    average_rating = db.session.query(func.avg(RestaurantReview.rating)).scalar()
    if average_rating is not None:
        average_rating = round(average_rating, 1)

    return render_template('index.html', average_rating=average_rating)


@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/data')
def data():
    # Query all reviews from the database, ordered by time_created (newest first)
    reviews = RestaurantReview.query.order_by(RestaurantReview.time_created.desc()).filter(RestaurantReview.restaurant_name=="mcdonalds").all()
    return render_template('data.html', reviews=reviews)

@app.route('/datas')
def datas():
    # Query all reviews from the database, ordered by time_created (newest first)
    reviews = RestaurantReview.query.order_by(RestaurantReview.time_created.desc()).filter(RestaurantReview.restaurant_name=="dairy queen").all()
    return render_template('datas.html', reviews=reviews)


@app.route('/dataa')
def dataa():
    # Query all reviews from the database, ordered by time_created (newest first)
    reviews = RestaurantReview.query.order_by(RestaurantReview.time_created.desc()).filter(RestaurantReview.restaurant_name=="pizza hut").all()
    return render_template('dataa.html', reviews=reviews)


@app.route('/add_review', methods=['GET', 'POST'])
def add_review():
    if request.method == 'POST':
        new_review = RestaurantReview(
            restaurant_name=request.form['Restaurant_name'],
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
        review.restaurant_name = request.form['restaurant_name']
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



  








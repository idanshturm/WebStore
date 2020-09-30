"""Logged-in page routes."""
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import current_user, login_required, logout_user, login_user
from .forms import LoginForm, SignupForm, SearchForm, InsertForm
from .models import db, Prod




# Blueprint Configuration
main_bp = Blueprint(
    'main_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@main_bp.route('/', methods=['GET'])
@login_required
def dashboard():
    """Logged-in User Dashboard."""
    return render_template(
        'dashboard.jinja2',
        title='Flask-Login Tutorial.',
        template='dashboard-template',
        current_user=current_user,
        body="You are now logged in!"
    )


@main_bp.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login'))


@main_bp.route('/insert', methods=['GET' , 'POST'])
@login_required
def insert():

    form = InsertForm()

    if form.validate_on_submit():
        existing_Product = Prod.query.filter_by(name=form.name.data).first()
        if existing_Product is None:
              
            nameProd = Prod(
            name=form.name.data,
            price=form.price.data,
            amount=form.amount.data
            )
                           
            db.session.add(nameProd)
            flash('Product successfully added') 
            db.session.commit()
         
        else:
            existing_Product.price=form.price.data
            existing_Product.amount=int(existing_Product.amount)+int(form.amount.data)

            flash('Product successfully updated')
            db.session.commit()

          
    return render_template(
    'insertpage.jinja2',
    form=form,
    title='insert product.',
    template='insert product',
    body="insert your product."
    )


@main_bp.route('/search', methods=['GET' , 'POST'])
@login_required
def search():

    form = SearchForm()

    if form.validate_on_submit():
        existing_Product = Prod.query.filter_by(name=form.name.data).first()
        if existing_Product is None:
            flash('out of stock')

        else:
            flash('you serach for ' +  existing_Product.name)
            flash('cost ' +  existing_Product.price)
            flash('amount ' +  existing_Product.amount)

    
    return render_template(
    'searchpage.jinja2',
    form=form,
    title='search product.',
    template='search product',
    body="search your product."
)
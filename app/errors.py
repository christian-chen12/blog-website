from flask import render_template
from app import app, db

# created a custom error page for 404 errors(from 404.html)
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# created a custom error page for 500 errors(from 500.html)
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
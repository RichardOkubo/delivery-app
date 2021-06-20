from flask import Blueprint, current_app, render_template, redirect

from delivery.ext.auth.form import UserForm
from delivery.ext.auth.models import User
from delivery.ext.db import db

bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    print("entrei na funcao main")
    current_app.logger.debug("Entrei na funcao main")
    return render_template("index.html")


@bp.route("/sobre")
def about():
    return render_template("about.html")


@bp.route("/cadastro", methods=["GET", "POST"])
def signup():
    form = UserForm()

    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        # forçar login
        return redirect("/")

    return render_template("userform.html", form=form)


@bp.route("/restaurantes")
def restaurants():
    return render_template("restaurants.html")

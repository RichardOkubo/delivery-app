import os

from flask import current_app as app
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename

from delivery.ext.auth.models import User
from delivery.ext.db import db

ALG = "pbkdf2:sha256"


def create_user(email: str, password: str, admin: bool=False) -> User:
    user = User(
        email=email,
        passwd=generate_password_hash(password, ALG),
        admin=admin
    )
    db.session.add(user)
    # TODO(RichardOkubo): Tratar 'exception' caso 'user' já exista 
    db.session.commit()
    return user


def save_user_foto(filename, filestorage):
    """Save user foto in './uploads/foo/...'."""
    filename = os.path.join(
        app.config["UPLOAD_FOLDER"],
        secure_filename(filename)
    )
    # TODO(RichardOkubo):
    # 1) verificar se existe o diretório
    # 2) criar o diretório caso não exista
    filestorage.save(filename)

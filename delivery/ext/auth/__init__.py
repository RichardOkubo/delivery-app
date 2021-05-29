from delivery.ext.auth import models  # noqa
from delivery.ext.auth.commands import list_users, add_user


def init_app(app):
    # TODO(RichardOkubo): Initialize flask-simplelogin + JWT
    app.cli.command()(list_users)
    app.cli.command()(add_user)

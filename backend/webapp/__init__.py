# Project: webapp
# File: \__init__.py
# Created at: Thursday, November 14th 2019, 13:36:12 +03:00
# Author: Tamara A. Repina (4ertovo4ka@gmail.com)
# -----
# Last Modified: Sunday, September 22nd 2024, 14:42:00 +03:00
# Modified By: Tamara A. Repina (4ertovo4ka@gmail.com>)
# Last version: <<projectversion>>
# -----
# Copyright 2024 Tamara A. Repina
# License: GNU Affero General Public License v3.0 https://www.gnu.org/licenses/agpl.txt


from flask import Flask
from flask_login import LoginManager, current_user, login_required
from flask_migrate import Migrate

from webapp.config import get_settings
from webapp.user.views import blueprint as user_blueprint
from webapp.profile.views import blueprint as profile_blueprint
from webapp.vacancy.views import blueprint as vacancy_blueprint
from webapp.statistic.views import blueprint as statistic_blueprint

from webapp.db import db
from webapp.user.models import User


setting = get_settings()


def create_app():

    app = Flask(__name__)
    app.config['FLASK_ENV'] = setting.ENVIRONMENT
    app.config["SECRET_KEY"] = setting.SECRET_KEY
    app.config["SQLALCHEMY_DATABASE_URI"] = setting.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = setting.SQLALCHEMY_TRACK_MODIFICATIONS
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    app.register_blueprint(user_blueprint)
    app.register_blueprint(profile_blueprint)
    app.register_blueprint(vacancy_blueprint)
    app.register_blueprint(statistic_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Привет админ!'
        else:
            return 'Ты не админ!'

    return app

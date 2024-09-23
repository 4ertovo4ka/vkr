# Project: webapp
# File: \db.py
# Created at: Thursday, November 14th 2019, 13:36:12 +03:00
# Author: Tamara A. Repina (4ertovo4ka@gmail.com)
# -----
# Last Modified: Friday, September 20th 2024, 04:50:58 +03:00
# Modified By: Tamara A. Repina (4ertovo4ka@gmail.com>)
# Last version: <<projectversion>>
# -----
# Copyright 2024 Tamara A. Repina
# License: GNU Affero General Public License v3.0 https://www.gnu.org/licenses/agpl.txt


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(engine_options={'pool_size': 20, 'max_overflow': 30})

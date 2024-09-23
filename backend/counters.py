# Project: backend
# File: \counters.py
# Created at: Thursday, November 14th 2019, 13:36:12 +03:00
# Author: Tamara A. Repina (4ertovo4ka@gmail.com)
# -----
# Last Modified: Friday, September 20th 2024, 01:06:58 +03:00
# Modified By: Tamara A. Repina (4ertovo4ka@gmail.com>)
# Last version: <<projectversion>>
# -----
# Copyright 2024 Tamara A. Repina
# License: GNU Affero General Public License v3.0 https://www.gnu.org/licenses/agpl.txt


from webapp.model import Skill, Category, db, User, Vacancy, ProfessionalArea
from sqlalchemy import or_
from backend.webapp import create_app

app = create_app()


def count_skills():
    with app.app_context():
        vacancies = Vacancy.query.all()
        skills = Skill.query.all()
        for skill in skills:
            skill.count = 0
            db.session.commit()

        for vacancy in vacancies:
            for skill in skills:
                if skill.name.lower() in vacancy.vacancy_text_clean.lower():
                    skill.count += 1
                    db.session.commit()
    return False


def count_areas():
    with app.app_context():
        vacancies = Vacancy.query.all()
        areas = ProfessionalArea.query.all()
        # for area in areas:
        # area.count = 0
        # db.session.commit()

        for vacancy in vacancies:
            for area in areas:
                if vacancy.vacancy_prof_area == area.id:
                    area.count += 1
                    db.session.commit()
    return False


count_skills()

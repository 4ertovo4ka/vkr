# Project: vacancy
# File: \views.py
# Created at: Thursday, November 14th 2019, 13:36:12 +03:00
# Author: Tamara A. Repina (4ertovo4ka@gmail.com)
# -----
# Last Modified: Friday, September 20th 2024, 11:20:32 +03:00
# Modified By: Tamara A. Repina (4ertovo4ka@gmail.com>)
# Last version: <<projectversion>>
# -----
# Copyright 2024 Tamara A. Repina
# License: GNU Affero General Public License v3.0 https://www.gnu.org/licenses/agpl.txt


from flask import Flask, render_template, flash, redirect, url_for, request
from flask import Blueprint
from flask_login import current_user, login_required
from sqlalchemy import or_


from webapp.vacancy.models import Vacancy, Skill, Category, ProfessionalArea
from webapp.user.models import User
from webapp.profile.models import Favourite
from webapp.db import db

blueprint = Blueprint('vacancy', __name__)


@blueprint.route('/', methods=['GET', 'POST'])
def index():
    title = "Вакансии для разработчиков"
    page = request.args.get('page', 1, type=int)
    vacancies = Vacancy.query.filter(
        Vacancy.vacancy_prof_area != None).paginate(page=page, per_page=20)
    skills = Skill.query.all()
    categories = Category.query.all()
    areas = ProfessionalArea.query.all()

    if current_user.is_authenticated:
        favourite = Favourite.query.filter(
            Favourite.user_id == current_user.id).all()
        favourite_vacancy = []
        for favour in favourite:
            favourite_vacancy.append(favour.vacancy_id)
        return render_template('vacancy/index.html', page_title=title, vacancies=vacancies, favourite=favourite_vacancy,
                               skills=skills, categories=categories, areas=areas)
    else:
        return render_template('vacancy/index.html', page_title=title, vacancies=vacancies,  skills=skills,
                               categories=categories, areas=areas)


@blueprint.route('/search', methods=['GET'])
def search():
    title = "Вакансии для разработчиков"
    page = request.args.get('page', 1, type=int)
    areas = ProfessionalArea.query.all()
    skills = Skill.query.all()
    categories = Category.query.all()

    areas_page = [int(item) for item in request.args.getlist('areas')]
    skills_page = [int(item) for item in request.args.getlist('skills')]

    if request.method == 'GET':
        print(areas_page)
        print(skills_page)

        if areas_page:
            # Формируем список условий для областей
            area_conditions = [Vacancy.vacancy_prof_area ==
                               area_page for area_page in areas_page]

        else:
            # Если нет выбранных областей, выводим все вакансии
            area_conditions = [Vacancy.vacancy_prof_area != None]

        # Проверяем, есть ли выбранные навыки
        if skills_page:
            # Получаем имена навыков, которые выбрал пользователь
            skills_names = Skill.query.filter(Skill.id.in_(skills_page)).all()

            # Формируем список условий для навыков
            skill_conditions = [Vacancy.vacancy_text_clean.ilike(
                f'%{skill.name}%') for skill in skills_names]

            # Применяем фильтрацию по областям и навыкам
            vacancies = Vacancy.query.filter(
                or_(*area_conditions)).filter(or_(*skill_conditions))
        else:
            # Если навыков нет, применяем только фильтрацию по областям
            vacancies = Vacancy.query.filter(or_(*area_conditions))

        # Применяем пагинацию
        vacancies = vacancies.paginate(page=page, per_page=20)

        if current_user.is_authenticated:
            favourite = Favourite.query.filter(
                Favourite.user_id == current_user.id).all()
            favourite_vacancy = []
            for favour in favourite:
                favourite_vacancy.append(favour.vacancy_id)
            return render_template('vacancy/index.html',
                                   page_title=title,
                                   vacancies=vacancies,
                                   favourite=favourite_vacancy,
                                   skills=skills,
                                   categories=categories,
                                   areas=areas,
                                   areas_page=areas_page,
                                   skills_page=skills_page)
        else:
            return render_template('vacancy/index.html',
                                   page_title=title,
                                   vacancies=vacancies,
                                   skills=skills,
                                   categories=categories,
                                   areas=areas,
                                   areas_page=areas_page,
                                   skills_page=skills_page)

    return False

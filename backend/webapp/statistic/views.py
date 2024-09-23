# Project: statistic
# File: \views.py
# Created at: Thursday, November 14th 2019, 13:36:12 +03:00
# Author: Tamara A. Repina (4ertovo4ka@gmail.com)
# -----
# Last Modified: Friday, September 20th 2024, 11:35:59 +03:00
# Modified By: Tamara A. Repina (4ertovo4ka@gmail.com>)
# Last version: <<projectversion>>
# -----
# Copyright 2024 Tamara A. Repina
# License: GNU Affero General Public License v3.0 https://www.gnu.org/licenses/agpl.txt


import json
import os

from flask import Flask, render_template, request, Blueprint
from webapp.statistic.funcs_statistic import set_json_statistic, get_words_stat
from ast import literal_eval
from collections import defaultdict

blueprint = Blueprint('statistic', __name__)


@blueprint.route('/statistic', methods=['GET'])
def statistic():
    title = 'Статистика вакансий'

    # url = 'https://hh.ru/vacancy/34309601'

    # statistic = set_json_statistic()
    # update_vacancies = copy_vacancies()
    # words_stat = get_words_stat()

    vacancies_path = os.path.abspath(
        'backend/data/statistic/vacancies_stat.json')

    words_path = os.path.abspath(
        'backend/data/statistic/words_stat.json')

    with open(vacancies_path, mode='r', encoding='utf8') as vs:
        vacstat = json.load(vs)
        languages = vacstat['languages']
        prof_areas = vacstat['profession_vacancies']
        area_exp = vacstat['areas_experience']

    with open(words_path, mode='r', encoding='utf8') as ws:
        words_stat = json.load(ws)

    return render_template('statistic/statistic.html', page_title=title, prof_areas=prof_areas, area_exp=area_exp,
                           languages=languages, words_stat=words_stat)

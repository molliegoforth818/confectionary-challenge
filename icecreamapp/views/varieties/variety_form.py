import sqlite3
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from icecreamapp.models import Variety, model_factory
from ..connection import Connection


def get_varieties():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Variety)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            v.id,
            v.name,
            v.country_of_origin 
        FROM icecreamapp_variety v
        """)

        return db_cursor.fetchall()


def variety_form(request):

    if request.method == 'GET':
        varieties = get_varieties()
        template = 'variety/variety_form.html'
        context = {
            'all_varieties': varieties
        }
        return render(request, template, context)
    
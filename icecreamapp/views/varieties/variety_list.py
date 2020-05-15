import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from icecreamapp.models import Variety, model_factory
from ..connection import Connection


def variety_list(request):
    if request.method == 'GET':
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

           
            all_varieties = db_cursor.fetchall()
            
            template = 'variety/variety_list.html'
            context = {
                'varieties': all_varieties
             }

            return render(request, template, context)

    elif request.method == 'POST':
            form_data = request.POST

            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
              INSERT INTO icecreamapp_variety
        (
           'name', country_of_origin
        )
        VALUES (?, ?)
                """,
                    (
                        form_data['variety_name'], form_data['country_of_origin']
                    ))

    return redirect(reverse('icecreamapp:variety_list'))
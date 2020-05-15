import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from icecreamapp.models import Flavor, model_factory
from ..connection import Connection


def flavor_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Flavor)
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT
                f.id,
                f.name,
                f.alcohol_percent
            FROM icecreamapp_flavor f
            """)

           
            all_flavors = db_cursor.fetchall()
            
            template = 'flavor/flavor_list.html'
            context = {
                'flavors': all_flavors
             }

            return render(request, template, context)

    elif request.method == 'POST':
            form_data = request.POST

            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
              INSERT INTO icecreamapp_flavor
        (
           name, alcohol_percent
        )
        VALUES (?, ?)
                """,
                    (
                        form_data['name'], form_data['alcohol_percent']
                    ))

    return redirect(reverse('icecreamapp:flavor_list'))
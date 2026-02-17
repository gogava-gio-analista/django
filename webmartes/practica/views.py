from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def martes(request):
    return HttpResponse("hoy es martes")

def prueba(request):
    return HttpResponse("Mi primera página Django pero probando")

from django.http import HttpResponse

def miercoles(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Martes Django</title>
        <style>
            body {
                background: linear-gradient(to right, #4facfe, #00f2fe);
                text-align: center;
                font-family: Arial, sans-serif;
                color: white;
            }

            h1 {
                margin-top: 50px;
                font-size: 50px;
            }

            .sol {
                width: 150px;
                height: 150px;
                background: yellow;
                border-radius: 50%;
                margin: 40px auto;
                box-shadow: 0 0 40px orange;
                animation: girar 6s linear infinite;
            }

            @keyframes girar {
                from { transform: rotate(0deg); }
                to { transform: rotate(360deg); }
            }

            .mensaje {
                font-size: 25px;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>

        <h1>☀ Hoy es MARTES ☀</h1>

        <div class="sol"></div>

        <div class="mensaje">
            Mi primera página divertida en Django 
        </div>

    </body>
    </html>
    """

    return HttpResponse(html)


from django.http import HttpResponse

def barcelona(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Martes Barça</title>
        <style>
            body {
                background: linear-gradient(to right, #004d98, #a50044);
                text-align: center;
                font-family: Arial, sans-serif;
                color: white;
            }

            h1 {
                margin-top: 40px;
                font-size: 50px;
            }

            img {
                width: 300px;
                margin-top: 40px;
                transition: transform 0.5s;
            }

            img:hover {
                transform: scale(1.2) rotate(10deg);
            }
        </style>
    </head>
    <body>

        <h1>🔵🔴 Visca el Barça 🔴🔵</h1>

        <img src="https://upload.wikimedia.org/wikipedia/en/4/47/FC_Barcelona_%28crest%29.svg">

        <h2>Hoy es martes y somos del mejor equipo 😎</h2>

    </body>
    </html>
    """

    return HttpResponse(html)

from django.http import HttpResponse

def madrid(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Martes Madrid</title>
        <style>
            body {
                background: linear-gradient(to right, #ffffff, #e6e6e6);
                text-align: center;
                font-family: Arial, sans-serif;
                color: #111;
            }

            h1 {
                margin-top: 40px;
                font-size: 50px;
            }

            img {
                width: 300px;
                margin-top: 40px;
                transition: transform 0.6s, filter 0.6s;
            }

            img:hover {
                transform: scale(1.2) rotate(-10deg);
                filter: drop-shadow(0 0 20px gold);
            }

            .champions {
                font-size: 24px;
                margin-top: 30px;
                color: #caa300;
                font-weight: bold;
            }
        </style>
    </head>
    <body>

        <h1>⚪👑 Hala Madrid 👑⚪</h1>

        <img src="https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg">

        <div class="champions">
            El rey de Europa ⭐
        </div>

    </body>
    </html>
    """

    return HttpResponse(html)

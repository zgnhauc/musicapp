
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {
                    font-family: 'Garamond', sans-serif;
                    background-color: #F6FFDC;
                    color: white;
                    text-align: center;
                    padding: 50px;
                }
                h1 {
                    font-size: 48px;
                    color: #F9B2D7;
                    letter-spacing: 2px;
                }
                p {
                    font-size: 18px;
                    color: #021A54;
                }
            </style>
        </head>
        <body>
            <h1>Music Platform</h1>
            <p>Team: Josue Ortiz, Ambrose Mcahee, Annie Nguyen, Julia Navarro, Slobodan Malinkov</p>
            <p>Date: April 9, 2026 | Class: IS218</p>
        </body>
        </html>
    """)
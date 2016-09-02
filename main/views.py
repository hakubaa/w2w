from django.shortcuts import render
from django.http.request import HttpRequest
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

import main.browse as browse

import json


def home_page(request):
    # Start with popular browsing mode
    request.session["browse_mode"] = "popular"
    request.session["browse_page"] = 1

    # movies = browse.get_movies({"mode": "popular", "page": 1})

    return render(request, "main/home.html")


@csrf_exempt
def browse_movies(request, direction = None, page = None):

    browse_settings = dict()
    browse_settings["mode"] = request.session.get("browse_mode", "popular")
    browse_settings["page"] = page
    if browse_settings["page"] is None:
        if direction is None or direction == "next":
            browse_settings["page"] = request.session.get("browse_page", 0) + 1
        else:
            browse_settings["page"] = request.session.get("browse_page", 0) - 1
    browse_settings["page"] = int(browse_settings["page"])
    request.session["browse_page"] = max(browse_settings["page"], 1)

    if browse_settings["mode"] == "search":
        pass
        # request.session.get("browse_query")
        # request.session.get("browse_movies")
        # request.session.get("browse_movies_per_page")
        # request.session.get("browse_total_pages")

    movies = browse.get_movies(browse_settings)
    return JsonResponse(movies, safe = False)

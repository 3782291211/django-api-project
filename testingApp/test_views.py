from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from pymongo import MongoClient
from apiApp.models import (
    find_patterns,
    find_single_pattern,
    find_users,
    find_single_user,
    find_patterns_by_username,
    insert_pattern,
    insert_user,
    update_pattern,
    update_user,
    delete_items
)
import json

import os
import urllib.parse 
from dotenv import load_dotenv
load_dotenv()

mongo_uri = str(os.getenv('MONGO_URI'))
client = MongoClient(mongo_uri)

db = client["multiply_till_you_die_db"]
patterns_collection = db["patterns_test"]
users_collection = db["users_test"]

# Create your views here.
@api_view(["GET", "POST"])
def get_patterns(request):
    if request.method == "GET":
        return Response(
            {"patterns": json.loads(find_patterns(request, patterns_collection))},
            status=status.HTTP_200_OK,
        )
    elif request.method == "POST":
        return insert_pattern(request, patterns_collection, users_collection)


@api_view(["GET", "PUT",'DELETE'])
def single_pattern(request, id):
    if request.method == "GET":
        return find_single_pattern(request, id, patterns_collection)
    elif request.method == "PUT":
        return update_pattern(request, id, patterns_collection)
    elif request.method == 'DELETE':
        return delete_items(id,patterns_collection)


@api_view(["GET", "POST"])
def get_users(request):
    if request.method == "GET":
        return Response(
            {"users": json.loads(find_users(request, users_collection))},
            status=status.HTTP_200_OK,
        )
    elif request.method == "POST":
        return insert_user(request, users_collection)

@api_view(["GET", "PUT", 'DELETE'])
def get_single_user(request, id):
    if request.method == "GET":
        return find_single_user(id, users_collection)
    elif request.method == "PUT":
        return update_user(request, id, users_collection, patterns_collection)
    elif request.method == 'DELETE':
        return delete_items(id,users_collection)


@api_view(["GET"])
def get_patterns_by_username(request, username):
    return find_patterns_by_username(username, patterns_collection, users_collection)

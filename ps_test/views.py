from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from .models import User_table
import json

# Create your views here.
def home(request):
    # all_users = User_table.objects.all()
    # data = serialize("json", all_users)
    all_users = list(User_table.objects.values())
    return JsonResponse(
        {
            'status_code' : 200,
            'data' : all_users,
        },
        safe = False,
    )
    
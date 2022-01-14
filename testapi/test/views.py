from django.http import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def testview(request):
    if request.method == 'GET':
        dat = request.GET
        print(dat)

        return Response(dat)
    elif request.method == 'POST':
        data1 = {
            "name": "working in post",

        }
    # print(dat)

        return Response(data1)
    return Response({"hello": "python"})

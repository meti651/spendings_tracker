from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.core import serializers
from spendingstracker.models import Spending

import json


def index(request):
    if request.method == "GET":
        response = handle_index_get(request)
    elif request.method == "POST":
        response = handle_index_post(request)
    else:
        response = HttpResponse(
            "You can only send GET or POST request to this url", status=400)

    return response


def handle_index_get(request):
    data = list(Spending.objects.all())
    response_data = serializers.serialize('json', data)
    return JsonResponse(response_data, safe=False)


def handle_index_post(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    if 'amount' not in body:
        return HttpResponse("The amount must be added to the request body", status=400)
    if 'currency' not in body:
        return HttpResponse("The currency must be added to the request body", status=400)
    if 'description' not in body:
        body['description'] = ""
    if 'date' not in body:
        body['date'] = timezone.now()

    new_data = {
        'amount': body['amount'],
        'currency': body['currency'],
        'description': body['description'],
        'date': body['date']
    }

    query = Spending(amount=new_data['amount'], currency=new_data['currency'],
                     description=new_data['description'], date=new_data['date'])
    query.save()

    return HttpResponse("New record saved")


def delete(request, id):
    spending = Spending.objects.filter(pk=id).first()

    if spending == None:
        return HttpResponse("There is no matching spending with the requested id", status=400)

    spending.delete()
    return HttpResponse(f"Spending with the id: {id}, is deleted")


def update(request, id):
    spending = Spending.objects.filter(pk=id).first()

    if spending == None:
        return HttpResponse("There is no matching spending with the requested id", status=400)

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    if 'amount' in body:
        spending.amount = body['amount']
    if 'currency' in body:
        spending.currency = body['currency']
    if 'description' in body:
        spending.description = body['description']
    if 'date' in body:
        spending.date = body['date']

    spending.save()

    return HttpResponse(f"{spending.__str__()} is updated")


def order(request, order_by, descending):
    spendings = Spending.objects.all().order_by(order_by)
    response_date = serializers.serialize('json', spendings)
    return JsonResponse(response_date, safe=False)


def filter(request, currency):
    spendings = Spending.objects.filter(currency=currency)
    response_date = serializers.serialize('json', spendings)
    return JsonResponse(response_date, safe=False)

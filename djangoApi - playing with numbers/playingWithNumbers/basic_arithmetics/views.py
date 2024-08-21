from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from functools import reduce

# Create your views here.


@csrf_exempt
def total(request):
    if request.method == 'POST':
        json_in_request = json.loads(request.body)
        nums_to_total = json_in_request.get('numbers')

        total_res = {
            'numbers': nums_to_total,
            'total': sum(nums_to_total)
        }

        return JsonResponse(total_res)

    return JsonResponse({
        'error': 'POST request required'
    })


@csrf_exempt
def average(request):
    if request.method == 'POST':
        json_in_request = json.loads(request.body)
        nums_to_take_avg = json_in_request.get('numbers')

        nums_avg = sum(nums_to_take_avg)/len(nums_to_take_avg)

        avg_res = {
            'numbers': nums_to_take_avg,
            'average': nums_avg
        }

        return JsonResponse(avg_res)

    return JsonResponse({
        'error': 'POST request required'
    })


@csrf_exempt
def product(request):
    if request.method == 'POST':
        json_in_request = json.loads(request.body)
        nums_to_take_product = json_in_request.get('numbers')

        nums_product = reduce(lambda x, y: x*y, nums_to_take_product)

        product_res = {
            'numbers': nums_to_take_product,
            'product': nums_product
        }

        return JsonResponse(product_res)

    return JsonResponse({
        'error': 'POST request required'
    })

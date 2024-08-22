from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from functools import reduce

# Create your views here.


# Controlling the API Endpoints

@csrf_exempt
def total(request):
    """total: It controls the /api/total endpoint. It receives a list of numbers and returns the total of those numbers in the response with json. The endpoint accepts POST requests only."""

    if request.method == 'POST':

        # Loading the json data and getting the numbers to be total from the request
        json_in_request = json.loads(request.body)
        nums_to_total = json_in_request.get('numbers')

        # Calculating the total and preparing the response
        total_res = {
            'numbers': nums_to_total,
            'total': sum(nums_to_total)
        }

        # Returning the response
        return JsonResponse(total_res)

    # returning error if the request is not POST

    return JsonResponse({
        'error': f'Invalid request-type {request.method}, Expected POST'
    })


@csrf_exempt
def average(request):
    """
    average: It controls the /api/average endpoint. It receives a list of numbers and returns the average of those numbers in the response with json."""

    if request.method == 'POST':

        # Loading the json data and getting the numbers to take their average from the request

        json_in_request = json.loads(request.body)
        nums_to_take_avg = json_in_request.get('numbers')

        # Calculating the average

        nums_avg = sum(nums_to_take_avg)/len(nums_to_take_avg)

        # preparing the response

        avg_res = {
            'numbers': nums_to_take_avg,
            'average': nums_avg
        }

        # returning the response

        return JsonResponse(avg_res)

    # returning error if the request is not POST

    return JsonResponse({
        'error': f'Invalid request-type {request.method}, Expected POST'
    })


@csrf_exempt
def product(request):
    """
    product: It controls the /api/product endpoint. It receives a list of numbers and returns the product of those numbers in the response with json.
    """

    if request.method == 'POST':

        # Loading the json data and getting the numbers to take their product from the request

        json_in_request = json.loads(request.body)
        nums_to_take_product = json_in_request.get('numbers')

        # Calculating the product

        nums_product = reduce(lambda x, y: x*y, nums_to_take_product)

        # preparing the response

        product_res = {
            'numbers': nums_to_take_product,
            'product': nums_product
        }

        # returning the response

        return JsonResponse(product_res)

    # returning error if the request is not POST

    return JsonResponse({
        'error': f'Invalid request-type {request.method}, Expected POST'
    })

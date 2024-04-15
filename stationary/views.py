
from django.shortcuts import render
from .models import TransactionItem
from django.shortcuts import redirect

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def addtocart(request):
    return render(request, 'addtocart.html')

def Ball_Pens(request):
    api_url = "http://192.168.1.34:8000/getproductdata/"
    print (api_url)
    
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            pens_data = [item for item in data if item.get('product_name') == 'Pens' and item.get('product_category') == 'Ball Pens']
            print(pens_data)

            return render(request, 'Ball_Pens.html', {'data': pens_data})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

def contact(request):
    return render(request, 'contact.html')

def Erasers(request):
    return render(request, 'Erasers.html')

def Folders_Fillings(request):
    return render(request, 'Folders_Fillings.html')

def pen_fountain(request):
    api_url = "http://192.168.1.34:8000/getproductdata/"
    print(api_url)
    
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            
            # Filter data for items with product name "Pen" and category "Ball Pen"
            pens_data = [item for item in data if item.get('product_name') == 'Pens' and item.get('product_category') == 'Gel Pens']
            print(pens_data)


            return render(request, 'fountain_pens.html', {'data': pens_data})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})


def Gel_Pens(request):
    api_url = "http://192.168.1.34:8000/getproductdata/"
    
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            
            # Filter data for items with product name "Pen" and category "Ball Pen"
            pens_data = [item for item in data if item.get('product_name') == 'Pens' and item.get('product_category') == 'Gel Pens']
            print(pens_data)


            return render(request, 'Gel_Pens.html', {'data': pens_data})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

def highlighter(request):
    return render(request, 'highlighter.html')

def Memo_Blocks(request):
    return render(request, 'Memo_Blocks.html')

def notebooks(request):
    return render(request, 'notebooks.html')

def notepads(request):
    return render(request, 'notepads.html')

def organizers(request):
    return render(request, 'organizers.html')

def Paperclips(request):
    return render(request, 'Paperclips.html')

def Premium_Gel_Pens(request):
    return render(request, 'Premium_Gel_Pens.html')

def Roller_Ball_Pens(request):
    api_url = "http://192.168.1.34:8000/getproductdata/"
    
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            print(data)
            
            # Filter data for items with product name "Pen" and category "Ball Pen"
            pens_data = [item for item in data if item.get('product_name') == 'Pens' and item.get('product_category') == 'Roller Ball Pens']
            print(pens_data)

            return render(request, 'Roller_Ball_Pens.html', {'data': pens_data})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})


def Shopners(request):
    return render(request, 'Sharpener.html')

def Staplers(request):
    return render(request, 'Staplers.html')

def Sticky_Notes(request):
    return render(request, 'Sticky_Notes.html')

def todolist(request):
    return render(request, 'To-do_list.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def cancelation(request):
    return render(request, 'cancelation_policy.html')


def return_policy(request):
    return render(request, 'return_policy.html')


def refund_policy(request):
    return render(request, 'refund_policy.html')


def privacy_policy(request):
    return render(request, 'privacy_policy.html')


def terms_conditions(request):
    return render(request, 'terms_conditions.html')


def shipping_policy(request):
    return render(request, 'shipping_policy.html')


def my_account(request):
    return render(request, 'my_account.html')


def faq(request):
    return render(request, 'faq.html')


def registration(request):
    return render(request, 'registration.html')


def scissors(request):
    return render(request, 'scissors.html')

def calculators(request):
    return render(request, 'calculators.html')

def files(request):
    return render(request, 'files.html')

def pen_stands(request):
    return render(request, 'pen_stands.html')

def cutters(request):
    return render(request, 'download_app.html')

def download_app(request):
    return render(request, 'cutters.html')

def paper_clips(request):
    return render(request, 'paper_clips.html')

def white_board_markers(request):
    return render(request, 'white_board_markers.html')

def punches(request):
    return render(request, 'punches.html')

def tape_dispenser(request):
    return render(request, 'tape_dispenser.html')

def paints(request):
    return render(request, 'paints.html')

def art_pencils(request):
    return render(request, 'art_pencils.html')

def brush_pens(request):
    return render(request, 'brush_pens.html')

def brushes(request):
    return render(request, 'brushes.html')

def sketch(request):
    return render(request, 'sketch.html')



from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import TransactionItem

def generate_pdf(request):
    items = TransactionItem.objects.all()
    total = sum(item.total for item in items)
    
    template_path = 'bill.html'
    context = {'items': items, 'total': total}
    
    template = get_template(template_path)
    html = template.render(context)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="transaction_bill.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')

    return response

from .forms import RegistrationForm
import requests

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


# def getproduct(request):
#     api_url = "http://192.168.1.36:7000/getproductdata/"
    
#     try:
#         # Fetch data from the API
#         response = requests.get(api_url)
#         if response.status_code == 200:
#             # Convert the response to JSON
#             data = response.json()
#             # Pass the data to the template
#             return render(request, 'data_template.html', {'data': data})
#         else:
#             # If there's an error in fetching data, return an error message
#             return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
#     except Exception as e:

#         return render(request, 'error_template.html', {'error_message': str(e)})

import requests
from django.shortcuts import render
# def getproduct(request):
#     api_url = "http://192.168.1.36:7000/getproductdata/"zz
    
#     try:
#         # Fetch data from the API
#         response = requests.get(api_url)
#         if response.status_code == 200:
#             # Convert the response to JSON
#             data = response.json()
            
#             # Filter data for items with product name "Pens"
#             pens_data = [item for item in data if item.get('product_name') == 'Pens']
        
            
#             # Pass the filtered data to the template
#             return render(request, 'data_template.html', {'data': pens_data})
#         else:
#             # If there's an error in fetching data, return an error message
#             return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
#     except Exception as e:
#         return render(request, 'error_template.html', {'error_message': str(e)})]

import requests

def getproduct(request):
    api_url = "http://192.168.1.56:8000/getproductdata/"
    
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            
            # Filter data for items with product name "Pen" and category "Ball Pen"
            pens_data = [item for item in data if item.get('product_name') == 'Pens' and item.get('product_category') == 'Ball Pen']
            # print(pens_data)

            return render(request, 'data_template.html', {'data': pens_data})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})



import requests
from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        # Retrieve data from the form
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        image = request.FILES.get('image')

        # Prepare data to send to the API
        data = {
            'username': username,
            'name': name,
            'email': email,
            'phone': phone,
            'password': password,
            'image': image,
        }
        
        response = requests.post('http://192.168.1.34:9000/register/', data=data)

        print(response.text)

        return HttpResponse("Registration successful!")  # Assuming registration is successful

    elif request.method == 'GET':
        return render(request, 'registeration.html')

    else:
        return HttpResponse(status=405)  # Method Not Allowed for other request methods
# views.py
# views.py
# views.py



# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.http import require_POST
# import requests
# # views.py
# # views.py

# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.http import require_POST
# import requests
# # views.py

# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.http import require_POST
# import requests

# @csrf_exempt
# @require_POST
# def register(request):
#     if request.method == 'POST':
#         # Extract registration data from POST request
#         username = request.POST.get('username')
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         password = request.POST.get('password')
#         image = request.FILES.get('image')  # Assuming image is uploaded as a file

#         # Prepare the data to be sent to the external API
#         registration_data = {
#             'username': username,
#             'name': name,
#             'email': email,
#             'phone': phone,
#             'password': password,
#             # 'image': image  # Assuming image is uploaded as a file
#             # Ensure the 'image' key is removed if not needed by the API
#         }

#         # API endpoint where you want to save the registration data
#         api_url = 'http://192.168.1.35:9000/register/'

#         try:
#             # Send a POST request to the API endpoint with registration data
#             response = requests.post(api_url, data=registration_data)

#             # Check if the request was successful
#             if response.status_code == 200:
#                 # Registration successful
#                 return JsonResponse({'message': 'Registration successful'})
#             else:
#                 # Registration failed
#                 return JsonResponse({'error': 'Failed to register'}, status=400)
#         except Exception as e:
#             # Handle exceptions, such as connection errors, timeout, etc.
#             return JsonResponse({'error': str(e)}, status=500)

#     # Return an error if the request method is not POST
#     return JsonResponse({'error': 'Method not allowed'}, status=405)

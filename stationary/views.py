
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
    api_url = "http://192.168.1.44:9000/getproductdata/"
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
    api_url = "http://192.168.1.44:9000/getproductdata/"
    print (api_url)
    
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            print(data)
            pencils_data = [item for item in data if item.get('product_name') == 'Pencils' and item.get('product_category') == 'Pencil']
            print(pencils_data)

            return render(request, 'contact.html', {'data': pencils_data})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

def Erasers(request):
    api_url = "http://192.168.1.44:9000/getproductdata/"
    
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            print(data)
            
            Erasers_data = [item for item in data if item.get('product_name') == 'Erasers' and item.get('product_category') == 'Erasers']
            print(Erasers_data)

            return render(request, 'Roller_Ball_Pens.html', {'data': Erasers_data})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

def Folders_Fillings(request):
    return render(request, 'Folders_Fillings.html')

def pen_fountain(request):
    api_url = "http://192.168.1.44:9000/getproductdata/"
    print(api_url)
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            
            pens_data = [item for item in data if item.get('product_name') == 'Pens' and item.get('product_category') == 'Gel Pens']
            print(pens_data)


            return render(request, 'fountain_pens.html', {'data': pens_data})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})


def Gel_Pens(request):
    api_url = "http://192.168.1.44:9000/getproductdata/"
    print (api_url)
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            pens_data = [item for item in data if item.get('product_name') == 'Pens' and item.get('product_category') == 'Gel Pens']
            print(pens_data)

            return render(request, 'Gel_Pens.html', {'data': pens_data})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})


def Gel_Pen(request):
    api_url = "http://192.168.1.44:9000/getproductdata/"
    print (api_url)
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            pens_data = [item for item in data if item.get('product_name') == 'Pens' and item.get('product_category') == 'Gel Pens']
            print(pens_data)

            return render(request, 'gel.html', {'data': pens_data})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

def highlighter(request):
    api_url = "http://192.168.1.44:9000/getproductdata/"
    print (api_url)
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            Highlighters_data = [item for item in data if item.get('product_name') == 'Highlighters' and item.get('product_category') == 'Highlighters']
            print(Highlighters_data)

            return render(request, 'highlighter.html', {'data': Highlighters_data})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

def Memo_Blocks(request):
    api_url = "http://192.168.1.44:9000/getproductdata/"
    
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            print(data)
            
            Memo_Blocks_data = [item for item in data if item.get('product_name') == 'Memo Blocks' and item.get('product_category') == 'Memo Blocks']
            print(Memo_Blocks_data)

            return render(request, 'Roller_Ball_Pens.html', {'data': Memo_Blocks_data})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

def notebooks(request):
    api_url = "http://192.168.1.44:9000/getproductdata/"
    print (api_url)
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            notebooks_data = [item for item in data if item.get('product_name') == 'Notebooks' and item.get('product_category') == 'Notebooks']
            print(notebooks_data)

            return render(request, 'notebooks.html', {'data': notebooks_data})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})


def notepads(request):
    api_url = "http://192.168.1.44:9000/getproductdata/"
    print (api_url)
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            notepads_data = [item for item in data if item.get('product_name') == 'Notepads' and item.get('product_category') == 'notebooks']
            print(notepads_data)

            return render(request, 'notepads.html', {'data': notepads_data})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})


def organizers(request):
    return render(request, 'organizers.html')

def Paperclips(request):
    return render(request, 'Paperclips.html')

def Premium_Gel_Pens(request):
    api_url = "http://192.168.1.44:9000/getproductdata/"
    
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            print(data)
            
            pens_data = [item for item in data if item.get('product_name') == 'Pens' and item.get('product_category') == 'Roller Ball Pens']
            print(pens_data)

            return render(request, 'Roller_Ball_Pens.html', {'data': pens_data})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})


def Roller_Ball_Pens(request):
    api_url = "http://192.168.1.44:9000/getproductdata/"
    
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            print(data)
            
            pens_data = [item for item in data if item.get('product_name') == 'Pens' and item.get('product_category') == 'Roller Ball Pens']
            print(pens_data)

            return render(request, 'Roller_Ball_Pens.html', {'data': pens_data})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})


def Shopners(request):
    api_url = "http://192.168.1.44:9000/getproductdata/"
    
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            print(data)
            
            Sharpeners_data = [item for item in data if item.get('product_name') == 'Sharpeners' and item.get('product_category') == 'Sharpeners']
            print(Sharpeners_data)

            return render(request, 'Roller_Ball_Pens.html', {'data': Sharpeners_data})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})


def Staplers(request):
    return render(request, 'Staplers.html')

def Sticky_Notes(request):
    api_url = "http://192.168.1.44:9000/getproductdata/"
    
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            print(data)
            
            Sticky_Notes_data = [item for item in data if item.get('product_name') == 'Sticky Notes' and item.get('product_category') == 'Sticky Notes']
            print(Sticky_Notes_data)

            return render(request, 'Roller_Ball_Pens.html', {'data': Sticky_Notes_data})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

def todolist(request):
    api_url = "http://192.168.1.44:9000/getproductdata/"
    
    try:
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            print(data)
            
            To_Do_List_data = [item for item in data if item.get('product_name') == 'To Do List' and item.get('product_category') == 'To Do List']
            print(To_Do_List_data)

            return render(request, 'Roller_Ball_Pens.html', {'data': To_Do_List_data})
        else:

            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})


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
def getproduct(request):
    api_url = "http://192.168.1.44:9000/getproductdata/"
    
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        if response.status_code == 200:
            # Convert the response to JSON
            data = response.json()
            
            # Filter data for items with product name "Pens"
            pens_data = [item for item in data if item.get('product_name') == 'Pens']
        
            
            # Pass the filtered data to the template
            return render(request, 'data_template.html', {'data': pens_data})
        else:
            # If there's an error in fetching data, return an error message
            return render(request, 'error_template.html', {'error_message': 'Failed to fetch data from the API.'})
    except Exception as e:
        return render(request, 'error_template.html', {'error_message': str(e)})

import requests

def getproduct(request):
    api_url = "http://192.168.1.44:9000/getproductdata/"
    
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
from django.http import JsonResponse

def register_with_api(request):
    if request.method == 'POST':
        api_url = 'http://192.168.1.45:9000/register/'

        # Validate form data
        username = request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')  # Optional field
        password = request.POST.get('password')

        if not (username and name and email and password):
            return JsonResponse({'error': 'Missing required fields'})

        # Sanitize input
        username = username.strip()
        name = name.strip()
        email = email.strip()
        phone = phone.strip()

        user_data = {
            'username': username,
            'name': name,
            'email': email,
            'phone': phone,
            'password': password,
        }

        try:
            response = requests.post(api_url, data=user_data)

            if response.status_code == 200:
                return JsonResponse({'message': 'Registration successful'})
            else:
                # Registration failed, provide more details about the error
                error_message = f"Registration failed with status code {response.status_code}."
                if response.text:
                    error_message += f" Response from server: {response.text}"
                return JsonResponse({'error': error_message})
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': f"Failed to connect to API server: {str(e)}"})
    else:
        return render(request, 'registration_form.html')

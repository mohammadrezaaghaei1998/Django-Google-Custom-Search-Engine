from django.shortcuts import render
import requests

#import your api key from settings.py
from google.settings import GOOGLE_API_KEY





#custom view

def search_view(request):
    query = request.GET.get('q', '')  

    if query:
        cx = '765ee326cea934447'


        #get your public URL from 'console.providers.google.com'
        api_url = f'https://www.googleapis.com/customsearch/v1?q={query}&key={GOOGLE_API_KEY}&cx={cx}'

        try:
            response = requests.get(api_url)

            if response.status_code == 200:
                search_results = response.json()

                return render(request, 'search_results.html', {'results': search_results, 'query': query})
            else:
                error_message = f'API request failed with status code {response.status_code}'
                print(error_message)
                return render(request, 'error.html', {'error_message': error_message})

        except Exception as e:
            error_message = f'An error occurred: {str(e)}'
            print(error_message)
            return render(request, 'error.html', {'error_message': error_message})

    return render(request, 'search_form.html')





#default view  
def second_search_view(request):
    return render(request,'search_form.html')
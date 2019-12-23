from django.shortcuts import render, redirect
from .models import quote
from .forms import quoteForm
from django.contrib import messages

def home(request):
    import requests
    import json

    if request.method == 'POST':
            ticker = request.POST['ticker']
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_b49e2be9722c4e59ac4d0cbece105368")

            try:
                api = json.loads(api_request.content)
            except Exception as e:
                api = "Error"
            return render(request, 'home.html', {'api': api})

    else:
        return render(request, 'home.html', {'ticker': "Enter a ticker symbol"})
    

    
def about(request):
    return render(request, 'about.html', {})

def add_stock(request):
    import requests
    import json

    if request.method == 'POST':
        form = quoteForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock has been added"))
            return redirect('add_stock')

    else:
        ticker = quote.objects.all()
        output =[]

        for ticker_item in ticker:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_b49e2be9722c4e59ac4d0cbece105368")

            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error"
        return render(request, 'add_stock.html', {'ticker': ticker, 'output': output})


def delete(request,quote_id):
    item = quote.objects.get(pk=quote_id)
    item.delete()
    messages.success(request,("stock ticker symbol has been deleted!"))
    return redirect(delete_stock)

def delete_quote(request):
    ticker = quote.objects.all()
    return render(request, 'delete_quote.html', {'ticker':ticker})
from django.shortcuts import  render




def index(request):
    #return redirect(reverse ("shop:index"))
    return render(request, 'index.html')

def store(request):
    return render(request, 'store.html') 
   
def checkout(request):
    return render(request, 'checkout.html')
 
def product(request):       
    return render(request, 'product.html') 
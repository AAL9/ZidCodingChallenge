from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from .models import Order



def home(request):
    context = {'rooms':"rooms"}
    return render(request, 'base/home.html',context)

def CreateWaybill(request):
    orders_with_no_waybills = Order.objects.filter(waybillCreated = False).filter(status = 'Ready to be Shipped')
    context = {'orders':orders_with_no_waybills}

    if request.method == 'POST':
        courier = request.POST.get('courier')
        selected_orders = request.POST.getlist('order')
        print("Creating Waybill selected orders...", selected_orders)
        # Update the product in the database with the policy number
        for order_id in selected_orders:
            order = Order.objects.get(id=order_id)
            #policy_number = createPolicyNumber(courier,order)
            #order.policyNum = policy_number
            #print(order.productName, " the Policy: ", policy_number)
            order.save()
        
        # Redirect to a success page or render a template
        return HttpResponse("Success!!")
        #return redirect('success_page')
    return render(request, 'base/CreateWaybill.html',context)


def PrintWaybill(request):
    context = {'rooms':"rooms"}
    return render(request, 'base/PrintWaybill.html',context)

def TrackShipment(request):
    context = {'rooms':"rooms"}
    return render(request, 'base/TrackShipment.html',context)

def CancelWaybill(request):
    context = {'rooms':"rooms"}
    return render(request, 'base/CancelWaybill.html',context)

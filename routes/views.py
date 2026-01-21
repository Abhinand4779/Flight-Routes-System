from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AirportRouteForm, NthNodeSearchForm
from .models import AirportRoute

# ROUTE 

def add_route(request):
    if request.method=="POST":
        form=AirportRouteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Flight route added successfully!")
            return redirect('add_route')
        else:
            messages.error(request,"Error in form submission.Please check the fields.")
    else:
        form=AirportRouteForm()

    routes=AirportRoute.objects.all().order_by('airport_code')
    return render(request,'add_route.html',{'form': form,'routes':routes})

# Nth NODE 
    
def find_nth_node(request):
    result=None
    if request.method=="POST":
        form = NthNodeSearchForm(request.POST)
        if form.is_valid():
            start_node = form.cleaned_data['root_airport']
            n = form.cleaned_data['n']
            pos = form.cleaned_data['position']
            
            result=AirportRoute.get_nth_node(start_node,n,pos)
            if not result:
                messages.warning(request,f"No airport found {n} steps to the {pos}.")
    else:
        form=NthNodeSearchForm()

    return render(request,'find_nth_node.html',{'form': form, 'result': result})

#LONGEST ROUTE

def longest_route(request):
    result = None
    if request.method == "POST":
        airport_code = request.POST.get('airport_code')
        node = AirportRoute.objects.filter(airport_code__iexact=airport_code).first()
        if node:
            duration,path = node.get_longest_path_info()
            result={
                'node':node,
                'max_duration':duration,
                'path': " -> ".join(path)
            }
        else:
            messages.error(request,f"Airport'{airport_code}'not found.")

    return render(request,'longest_route.html',{'result': result})

# SHORTEST ROUTE 

def shortest_route_between(request):
    result = None
    if request.method == "POST":
        a1_code=request.POST.get('airport1','').strip()
        a2_code=request.POST.get('airport2','').strip()
        
        result,error_msg=AirportRoute.find_shortest_path(a1_code, a2_code)
        if error_msg:
            messages.warning(request, error_msg)

    return render(request,'shortest_route.html', {
        'result': result
    })



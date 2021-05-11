from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import vaccineDetails
from django.urls import reverse
from staff.forms import VacForm
from django.contrib import messages

# Create your views here.
def requirement_req(request):
    if request.method == "GET":
        form = VacForm()
        context = {
            'form': form,
        }
        return render(request, 'requirement_req.html', context)
    elif request.method == "POST":
        form = VacForm(request.POST)
        if form.is_valid():
            comment = vaccineDetails(
                staff_name=form.cleaned_data["staff_name"],
                staff_no=form.cleaned_data["staff_no"],
                dp_code=form.cleaned_data["dp_code"],
                branch_name=form.cleaned_data["branch_name"],
                ro_code=form.cleaned_data["ro_code"],
                circle_name=form.cleaned_data["circle_name"],
                vaccinated=form.cleaned_data["vaccinated"],                
                vaccinated_date = form.cleaned_data["vaccinated_date"],  
                contact_number = form.cleaned_data["contact_number"],                           
            )
            comment.save()                  
            staffName = form.cleaned_data.get('staff_name')
            messages.info(request, f"Vaccinated details Added for: {staffName}")
            #login(request, user)
            #return httpResponse("file uploaded successfully")
            return redirect("requirement_req")
        else :
            #return render(request,"project_req.html")
            #context = "Data Invalid"
            #messages.info(request, f"New requirement Added: {form.errors}")
            return render(
                request, "requirement_req.html",
                {"form": form}
            )
            #return redirect("requirement_req")

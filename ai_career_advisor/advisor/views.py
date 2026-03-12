from django.shortcuts import render
from .forms import CareerForm
from .utils import analyze_skills
from .models import CareerAdvice

def home(request):

    form = CareerForm()

    if request.method == "POST":

        form = CareerForm(request.POST)

        if form.is_valid():

            skills = form.cleaned_data["skills"]

            result = analyze_skills(skills)

            CareerAdvice.objects.create(
                skills=skills,
                advice=str(result)
            )

            return render(request,"result.html",{
                "skills": skills,
                "careers": result["careers"],
                "additional_skills": result["skills"]
            })

    return render(request,"index.html",{"form":form})
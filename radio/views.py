from django.shortcuts import render

def radio_view(request):
    context = {
        'selected_gender': ""
    }

    if request.method == "POST":
        gender = request.POST.get("gender")
        if gender == "male":
            context['selected_gender'] = "Male"
        elif gender == "female":
            context['selected_gender'] = "Female"
        else:
            context['selected_gender'] = "pls select gender"

    return render(request, 'radio/radio.html', context)

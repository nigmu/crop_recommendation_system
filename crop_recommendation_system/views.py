# # crop_recommendation_system/views.py
# from django.shortcuts import render, redirect
# from soil.models import upload_soil_data_class
# from soil.forms import soil_data_form
# from utils.crop_recom import crop_predictor

# def home(request):
#     form = soil_data_form(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect('prediction')
        
#     soil_data = upload_soil_data_class.objects.all()

#     context = {
#         'form': form,
#         'soil_data': soil_data,
#     }
#     return render(request, 'main.html', context)



# def prediction(request):
#     # Retrieve the latest soil data
#     soil_data = upload_soil_data_class.objects.all()
#     # soil_data = upload_soil_data_class.objects.last()

#     if soil_data:
#         # Prepare data for prediction
        
#         data = [
#             soil_data.N, soil_data.P, soil_data.K,
#             soil_data.Temperature, soil_data.Humidity,
#             soil_data.Ph, soil_data.Rainfall
#         ]
        
#         # Predict crop using the imported function
#         predicted_crop = crop_predictor(data)
#         print("Predicted Crop:", predicted_crop)
#     else:
#         predicted_crop = None

#     context = {
#         'predicted_crop': predicted_crop
#     }
#     return render(request, 'prediction.html', context)


# crop_recommendation_system/views.py
from django.shortcuts import render, redirect
from soil.models import upload_soil_data_class
from soil.forms import soil_data_form
from utils.crop_recom import crop_predictor

def home(request):
    form = soil_data_form(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_soil_data = form.save(commit=False)  # Don't save to the database yet
            data = [
                new_soil_data.N, new_soil_data.P, new_soil_data.K,
                new_soil_data.Temperature, new_soil_data.Humidity,
                new_soil_data.Ph, new_soil_data.Rainfall
            ]
            predicted_crop = crop_predictor(data)
            new_soil_data.predicted_crop = predicted_crop  # Save the prediction to the model instance
            new_soil_data.save()  # Now save the instance to the database
            return redirect('prediction')  # Redirect to prediction view

    soil_data = upload_soil_data_class.objects.all()

    predictions = []
    predicted_crop = None
    if soil_data.exists():
        latest_data = soil_data.latest('id')
        latest_input_data = [
            latest_data.N, latest_data.P, latest_data.K,
            latest_data.Temperature, latest_data.Humidity,
            latest_data.Ph, latest_data.Rainfall
        ]
        predicted_crop = crop_predictor(latest_input_data)

        for data in soil_data:
            input_data = [
                data.N, data.P, data.K,
                data.Temperature, data.Humidity,
                data.Ph, data.Rainfall
            ]
            predictions.append((data, crop_predictor(input_data)))
    
    predictions.reverse()

    context = {
        'form': form,
        'predicted_crop': predicted_crop,
        'predictions': predictions
    }
    return render(request, 'main.html', context)

def prediction(request):
    soil_data = upload_soil_data_class.objects.all()

    predictions = []
    predicted_crop = None
    if soil_data.exists():
        latest_data = soil_data.latest('id')
        latest_input_data = [
            latest_data.N, latest_data.P, latest_data.K,
            latest_data.Temperature, latest_data.Humidity,
            latest_data.Ph, latest_data.Rainfall
        ]
        predicted_crop = crop_predictor(latest_input_data)

        for data in soil_data:
            input_data = [
                data.N, data.P, data.K,
                data.Temperature, data.Humidity,
                data.Ph, data.Rainfall
            ]
            predictions.append((data, crop_predictor(input_data)))
    predictions.reverse()

    context = {
        'predicted_crop': predicted_crop,
        'predictions': predictions
    }
    return render(request, 'prediction.html', context)

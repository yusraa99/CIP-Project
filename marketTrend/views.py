from django.shortcuts import render
import os
import tensorflow as tf
from tensorflow import keras
from django.shortcuts import redirect
# Create your views here.


path_to_model="/nflx_Bi_Lstm.h5"
def model_loader(path_to_model:os.path)-> tf.keras.Sequential:
    """
    Load a saved model and return it as a tf.keras.Sequential object.
    
    Parameters:
    path_to_model (os.path): The path to the saved model.
    
    Returns:
    tf.keras.Sequential: The loaded model.
    """
    # Load the model from the given path
    global model
    model = keras.models.load_model(path_to_model)
    
    # Return the loaded model
    return model
    
def markettrend(request):


    # Load the model from the given path
    
    
    return render(request,'marketTrend/markettrend.html')



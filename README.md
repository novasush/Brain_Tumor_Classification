# Deploy TF-Keras Model with Flask as Web App

Steps 


1. Clone the repo
2. Download the trained weights from [here](https://drive.google.com/file/d/1vDk5TbaXylcjbaxpH6YTyknOQV01C2_3/view?usp=sharing)
3. Add the downloaded weights in models folder
4. Create Virtualenv
   '''bash
   virtualenv env_name
   '''
5. Activate Virtual Env
   '''bash
   source env_name/bin/activate
   '''
6. Install required libraries
   '''bash
   pip install -r requirements.txt
   '''
7. Run app.py

Note - Upgrade pip to 20.0.2 version before running the app (pip install --upgrade pip)


Training & Testing

<table class="tfo-notebook-buttons" align="left">
  <td>
    <a target="_blank" href="https://colab.research.google.com/github.com/omkarmohanjoshi/Brain_Tumor_Classification/blob/master/brain_tumor_classification_training.ipynb">Run Training file in Google Colab</a>
  </td>
  <td>
    <a target="_blank" href="https://github.com/omkarmohanjoshi/Brain_Tumor_Classification/blob/master/brain_tumor_classification_training.ipynb">View Training file source on GitHub</a>
  </td>
  <td>
    <a target="_blank" href="https://colab.research.google.com/github.com/omkarmohanjoshi/Brain_Tumor_Classification/blob/master/brain_tumor_classification_prediction.ipynb">Run Prediction file in Google Colab</a>
  </td>
  <td>
    <a target="_blank" href="https://github.com/omkarmohanjoshi/Brain_Tumor_Classification/blob/master/brain_tumor_classification_prediction.ipynb">View Prediction file source on GitHub</a>
  </td>
</table>

If you want the train the model on your dataset, you can refer above given notebooks.


   

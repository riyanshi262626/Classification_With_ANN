# Customer Churn Prediction with Artificial Neural Network (ANN)

A machine learning project that predicts customer churn using an Artificial Neural Network (ANN). This project implements a deep learning model trained on customer data to classify whether a customer is likely to leave or stay with the service.

## 📋 Project Overview

This project demonstrates the complete workflow of building a classification model with ANN, including:
- **Data Exploration & Analysis**: Comprehensive exploratory data analysis
- **Model Training**: Building and training an ANN classifier
- **Model Evaluation**: Assessing model performance with various metrics
- **Web Application**: Interactive Streamlit app for making predictions on new customers

## 📁 Project Structure

```
Classification_With_ANN/
├── Churn_Modelling.csv          # Dataset with customer information
├── experiments.ipynb             # Jupyter notebook for model training and experimentation
├── prediction.ipynb              # Jupyter notebook for prediction demonstrations
├── app.py                        # Streamlit web application
├── model.h5                      # Trained ANN model
├── labelencoder_gender.pkl       # Label encoder for gender feature
├── onehotencoder.pkl             # One-hot encoder for geography feature
├── scaler.pkl                    # StandardScaler for feature scaling
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

## 🗂️ Files Description

| File | Purpose |
|------|---------|
| **Churn_Modelling.csv** | Contains customer data with features like credit score, age, tenure, balance, and churn status |
| **experiments.ipynb** | Notebook containing data exploration, preprocessing, model building, and evaluation |
| **prediction.ipynb** | Notebook demonstrating how to make predictions on new customer data |
| **app.py** | Streamlit application providing an interactive UI for customer churn predictions |
| **model.h5** | Pre-trained Keras/TensorFlow neural network model |
| **Encoders & Scaler (.pkl)** | Serialized preprocessing objects for consistent data transformation |

## 🚀 Features

- **User-Friendly Interface**: Interactive Streamlit web app
- **Feature Engineering**: Proper encoding and scaling of input features
- **Pre-trained Model**: Ready-to-use ANN model
- **Easy Deployment**: Simple setup and execution

### Input Features

The model accepts the following customer information:
- Geography (France, Spain, Germany)
- Gender (Male, Female)
- Credit Score
- Age
- Tenure (years as customer)
- Account Balance
- Estimated Salary
- Number of Products
- Credit Card Status (Yes/No)
- Active Member Status (Yes/No)

### Output

- **Churn Prediction**: Binary classification - "Likely to churn" or "Unlikely to churn"
- **Prediction Confidence**: Probability score (0-1)

## 📦 Requirements

All dependencies are listed in `requirements.txt`:

```
tensorflow==2.15.0
pandas
numpy
scikit-learn
tensorboard
matplotlib
streamlit
ipykernel
```

## 🔧 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/riyanshi262626/Classification_With_ANN.git
   cd Classification_With_ANN
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

### Running the Web Application

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`. Use the interactive interface to:
1. Select customer geography
2. Select customer gender
3. Enter customer financial and demographic information
4. Get instant churn prediction

### Exploring the Notebooks

- **experiments.ipynb**: Open with Jupyter Notebook to see the complete model development process
  ```bash
  jupyter notebook experiments.ipynb
  ```

- **prediction.ipynb**: View demonstration examples of making predictions
  ```bash
  jupyter notebook prediction.ipynb
  ```

## 🤖 Model Architecture

The ANN model is built using TensorFlow/Keras and includes:
- Input layer matching the number of features
- Multiple hidden layers with activation functions
- Output layer with sigmoid activation for binary classification
- Optimized for classification tasks using appropriate loss and metrics

## 📊 Data Preprocessing

The preprocessing pipeline includes:
1. **Label Encoding**: For categorical variables like gender
2. **One-Hot Encoding**: For geographic regions
3. **Feature Scaling**: StandardScaler normalization for numerical features
4. All preprocessing steps are saved as pickle files for consistent transformation during prediction

## 🎯 Model Performance

The trained model performs binary classification:
- **Threshold**: 0.5 probability
- Predicts churn likelihood based on customer characteristics
- Performance metrics available in `experiments.ipynb`

## 📝 Notebook Overview

### experiments.ipynb
- Data loading and exploration
- Feature engineering and preprocessing
- Model architecture design
- Model training and validation
- Performance evaluation and visualization

### prediction.ipynb
- Loading trained model and preprocessors
- Making predictions on sample customers
- Interpreting prediction results
- Example usage scenarios

## 🛠️ Technologies Used

- **TensorFlow/Keras**: Deep learning framework
- **Scikit-learn**: Machine learning preprocessing and utilities
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Streamlit**: Web application framework
- **Matplotlib**: Data visualization

## 📈 Future Enhancements

Potential improvements for this project:
- Model accuracy optimization
- Hyperparameter tuning
- Additional feature engineering
- Ensemble methods
- API deployment
- Model explainability (SHAP, LIME)
- Performance monitoring dashboard

## 💡 How the ANN Works

1. **Input Processing**: Customer data is preprocessed using saved encoders and scalers
2. **Feature Transformation**: Categorical variables are encoded and all features are normalized
3. **Neural Network**: Data passes through multiple layers of neurons with non-linear activations
4. **Prediction**: Output layer produces probability of churn (0-1)
5. **Classification**: Probability is compared to threshold (0.5) for final prediction

## 📚 Learning Outcomes

This project demonstrates:
- Building and training neural networks with TensorFlow/Keras
- Proper data preprocessing and feature engineering
- Model serialization and deployment
- Creating interactive applications with Streamlit
- Binary classification problem solving
- Working with real-world business data

## 📄 License

This project is open source and available for educational and research purposes.

## 👤 Author

Created by **riyanshi262626**

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## 📞 Support

If you encounter any issues or have questions, please open an issue on the GitHub repository.

---

**Happy Predicting! 🎉**

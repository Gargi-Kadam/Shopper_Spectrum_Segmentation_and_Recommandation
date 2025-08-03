# 🛒 Shopper Segmentation and Revenue Optimization  
*By Gargi Kadam*

This project focuses on identifying valuable customer segments and optimizing revenue strategies using data-driven insights. Leveraging EDA, feature engineering, and ML models, we deliver meaningful shopper segmentation and business recommendations from online retail data.

---

## 📌 Project Objective

- Analyze historical e-commerce transaction data  
- Understand customer purchase behavior  
- Segment customers using RFM and clustering  
- Build ML models for classification and prediction  
- Recommend business strategies for revenue growth  

---

## 📊 Key Insights from EDA

- 🇬🇧 The **UK** is the primary market, driving over 80% of sales  
- 🎁 Gift sets, cards, and bags are consistent top sellers  
- 🕒 Seasonal spikes in **November–December** due to holidays  
- 💸 High purchase frequency strongly correlates with total revenue  

---

## 🤖 Machine Learning Models

| Model               | Accuracy | F1-Score | Summary                                |
|--------------------|----------|----------|----------------------------------------|
| Logistic Regression| ✅ Good baseline | ⚠️ Moderate for imbalanced classes | Interpretable, fast                    |
| Random Forest       | ✅ Better recall | ✅ Handles imbalance well | Ensemble model                         |
| **XGBoost (Final)** | 🏆 Best overall | 💪 High F1-score & precision | Robust and deployment-ready            |

Final model saved using `joblib` and is ready for real-world use.

---

## 🧰 Tech Stack

- **Language**: Python 3.9+  
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn  
- **ML/Modeling**: Scikit-learn, XGBoost, SMOTE  
- **Text Processing**: NLTK, TF-IDF  
- **Feature Engineering**: PCA, Label Encoding  
- **Hyperparameter Tuning**: GridSearchCV, RandomizedSearchCV  
- **Optional UI**: Streamlit (for deployment)

---

## 📈 Evaluation Metrics

Models were evaluated using:
- **Accuracy**: Overall correctness
- **Precision**: Minimize false positives in customer targeting
- **Recall**: Capture all high-value customers
- **F1-Score**: Balanced score for imbalanced data

---

## 🚀 Final Model Summary

- **Best Model**: XGBoost Classifier  
- **Optimization**: GridSearchCV  
- **Metric Focus**: F1-Score  
- **Exported As**: `xgb_final_model.pkl`  

---

## 🧠 Future Enhancements

- Create a Streamlit-based prediction UI  
- Deploy as a REST API using Flask or FastAPI  
- Automate real-time customer segmentation pipeline  
- Extend with NLP for product review analysis  

---

## 📄 License

Licensed under the **MIT License**.  
Feel free to use, modify, or contribute to this project.

---

## 🙋‍♀️ Author

**Gargi Kadam**  


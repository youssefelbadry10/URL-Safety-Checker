import streamlit as st
import pandas as pd
import joblib  # لو عندك موديل محفوظ

st.title("🔍 URL Safety Checker")


user_input = st.text_input("Enter a URL to check if it's Safe or Not Safe")

import re

def extract_features(url):
    return {
        'has_https': 1 if 'https' in url.lower() else 0,
        'url_length': len(url),
        'num_dots': url.count('.'),
        'has_ip': 1 if re.match(r'^http[s]?://\d+\.\d+\.\d+\.\d+', url) else 0
    }

if user_input:
    features = extract_features(user_input)
    input_df = pd.DataFrame([features])
    
    # prediction = model.predict(input_df)[0]  ← شغلي دي لو عندك موديل
    prediction = "safe" if features['has_https'] == 1 else "not_safe"  # مؤقتاً من غير موديل

    st.markdown(f"### ✅ Result: **{prediction.upper()}**")

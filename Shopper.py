import streamlit as st


def get_recommendations(product_name):
    return ["Product A", "Product B", "Product C", "Product D", "Product E"]

def predict_customer_segment(recency, frequency, monetary):
    if monetary > 1000 and frequency > 10:
        return "High-Value"
    elif frequency > 5:
        return "Regular"
    elif recency > 60:
        return "At-Risk"
    else:
        return "Occasional"


st.set_page_config(page_title="Customer Insights App", layout="wide")
st.title("🛍️ Customer Intelligence Dashboard")

# Sidebar navigation
st.sidebar.title("🔍 Navigation")
page = st.sidebar.radio("Go to:", ["🏠 Home", "🎯 Product Recommendations", "📊 Customer Segmentation"])

# Home Page
if page == "🏠 Home":
    st.header("Welcome to the Customer Intelligence Dashboard!")
    st.markdown("Use the sidebar to navigate between **Product Recommendations** and **Customer Segmentation** tools.")

# Product Recommendation Page
elif page == "🎯 Product Recommendations":
    st.header("🎯 Product Recommendation")
    product_name = st.text_input("Enter a product name:")
    if st.button("Get Recommendations"):
        recommendations = get_recommendations(product_name)
        st.subheader("🔎 Recommended Products:")
        for product in recommendations:
            st.markdown(f"- ✅ **{product}**")

# Customer Segmentation Page
elif page == "📊 Customer Segmentation":
    st.header("📊 Customer Segmentation (RFM Model)")
    recency = st.number_input("Recency (days since last purchase)", min_value=0)
    frequency = st.number_input("Frequency (number of purchases)", min_value=0)
    monetary = st.number_input("Monetary (total spend)", min_value=0.0)

    if st.button("Predict Cluster"):
        cluster_label = predict_customer_segment(recency, frequency, monetary)
        st.success(f"🧠 Predicted Segment: **{cluster_label}**")

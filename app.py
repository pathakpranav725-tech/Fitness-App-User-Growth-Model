import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🏋️ Fitness App User Growth Model")

st.markdown("""
This project simulates how a fitness app grows over time using:
- Exponential user growth
- Retention analysis
- Dropout modeling
""")

# Sidebar inputs
st.sidebar.header("Parameters")

initial_users = st.sidebar.number_input("Initial Users", 100, 10000, 500)
growth_rate = st.sidebar.slider("Growth Rate", 0.01, 0.5, 0.1)
retention_rate = st.sidebar.slider("Base Retention Rate", 0.5, 1.0, 0.8)
improvement = st.sidebar.slider("Retention Improvement", 0.0, 0.2, 0.05)
days = st.sidebar.slider("Days", 10, 100, 60)

# Variables
active_users = initial_users
active_list = []
new_users_list = []
dropout_list = []

for t in range(days):
    new_users = initial_users * np.exp(growth_rate * t)
    
    adjusted_retention = retention_rate + improvement
    retained = active_users * adjusted_retention
    dropouts = active_users * (1 - adjusted_retention)

    active_users = retained + new_users

    active_list.append(active_users)
    new_users_list.append(new_users)
    dropout_list.append(dropouts)

# Results
peak_users = max(active_list)
peak_day = active_list.index(peak_users)

st.write(f"Peak Active Users: {int(peak_users)}")
st.write(f"Peak occurs on Day: {peak_day}")

# Graph
fig, ax = plt.subplots()

ax.plot(active_list, label="Active Users")
ax.plot(new_list, label="New Users")
ax.plot(drop_list, label="Dropouts")

ax.set_xlabel("Days")
ax.set_ylabel("Users")
ax.legend()


st.pyplot(plt)

st.subheader("Conclusion")
st.write("Retention strategies significantly increase long-term user growth.")

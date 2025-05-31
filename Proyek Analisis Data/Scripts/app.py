import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# Contoh data, ganti dengan data asli kamu
df_city = pd.DataFrame({
    'city': ['jundiaí', 'rio de janeiro', 'campinas', 'vila velha', 'são sebastião do oeste'],
    'revenue': [56000, 49000, 38000, 38000, 36000]
})

df_product = pd.DataFrame({
    'category': ['bed_bath_table', 'furniture_decor', 'health_beauty', 'sports_leisure', 'computers_accessories'],
    'orders': [13800, 11500, 11000, 9900, 9800]
})

df_monthly = pd.DataFrame({
    'year_month': ['201609', '201610', '201612', '201701', '201702', '201703', '201704', '201705', '201806', '201809'],
    'order_count': [250, 500, 0, 1300, 2700, 2300, 3600, 3200, 8300, 0]
})

df_dayofweek = pd.DataFrame({
    'day_name': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'order_item_id': [21577, 21794, 20609, 20103, 18912, 13889, 15617]
})

df_timeofday = pd.DataFrame({
    'time_category': ['dawn', 'morning', 'afternoon', 'night'],
    'order_item_id': [6190, 29767, 52310, 44234]
})

st.markdown("<h1 style='font-size:28px;'>E-Commerce Dashboard</h1>", unsafe_allow_html=True)


# Fungsi untuk plot bar horizontal
def plot_barh(df, y_col, x_col, title, ax, palette='viridis', title_fontsize=12):
    sns.barplot(data=df, y=y_col, x=x_col, ax=ax, palette=palette)
    ax.set_title(title, fontsize=title_fontsize)
    ax.set_xlabel(x_col.replace('_', ' ').title())
    ax.set_ylabel(y_col.replace('_', ' ').title())

col1, col2 = st.columns(2)

with col1:
    st.markdown("<h3 style='font-size:18px;'>Top 5 city by revenue</h3>", unsafe_allow_html=True)
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    plot_barh(df_city, 'city', 'revenue', 'Top 5 city by revenue', ax1)
    st.pyplot(fig1)

with col2:
    st.markdown("<h3 style='font-size:18px;'>Bottom 5 city by revenue</h3>", unsafe_allow_html=True)
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    plot_barh(df_city, 'city', 'revenue', 'Bottom 5 city by revenue', ax2)
    st.pyplot(fig2)

col1, col2 = st.columns(2)

with col1:
# Plot Top 5 product by category
    st.markdown("<h3 style='font-size:18px;'>Top 5 Product by Category</h3>", unsafe_allow_html=True)
    fig3, ax3 = plt.subplots(figsize=(8, 4))
    plot_barh(df_product, 'category', 'orders', 'Top 5 Product by Category', ax3, palette='rocket')
    st.pyplot(fig3)

with col2:
# Plot Bottom 5 product by category (gunakan data asli bottom 5)
    st.markdown("<h3 style='font-size:18px;'>Bottom 5 Product by Category</h3>", unsafe_allow_html=True)
    fig4, ax4 = plt.subplots(figsize=(8, 4))
    plot_barh(df_product, 'category', 'orders', 'Bottom 5 Product by Category', ax4, palette='rocket')
    st.pyplot(fig4)

# Evolution of total orders over time
st.markdown("<h3 style='font-size:18px;'>Evolution of Total Orders Overtime</h3>", unsafe_allow_html=True)
fig5, ax5 = plt.subplots(figsize=(10, 5))
sns.lineplot(data=df_monthly, x='year_month', y='order_count', marker='o', ax=ax5)
ax5.set_xticklabels(df_monthly['year_month'], rotation=45)
ax5.set_ylabel('Orders')
ax5.set_xlabel('Year-Month')
ax5.set_title('Evolution of Total Orders Overtime')

# Annotations
max_idx = df_monthly['order_count'].idxmax()
ax5.annotate('Highest orders received',
             xy=(max_idx, df_monthly.loc[max_idx, 'order_count']),
             xytext=(max_idx-1, df_monthly['order_count'].max() + 1000),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=10)

min_idx = df_monthly['order_count'].idxmin()
ax5.annotate('Noise on data\n(huge decrease)',
             xy=(min_idx, df_monthly.loc[min_idx, 'order_count']),
             xytext=(min_idx, df_monthly['order_count'].min() + 1500),
             arrowprops=dict(facecolor='red', shrink=0.05),
             fontsize=10)

st.pyplot(fig5)

col1, col2 = st.columns(2)

with col1:
# Total orders by Day of Week
    st.markdown("<h3 style='font-size:18px;'>Total Orders by Day of Week</h3>", unsafe_allow_html=True)
    fig6, ax6 = plt.subplots(figsize=(8, 4))
    sns.barplot(data=df_dayofweek, x='day_name', y='order_item_id', palette='Blues_d', ax=ax6)
    ax6.set_ylabel('Orders')
    ax6.set_xlabel('Day of Week')
    ax6.set_title('Total Orders by Day of Week')

    total_day = df_dayofweek['order_item_id'].sum()
    for i, val in enumerate(df_dayofweek['order_item_id']):
        pct = val / total_day * 100
        ax6.text(i, val + 300, f'{val}\n{pct:.1f}%', ha='center', fontsize=5)

    st.pyplot(fig6)

with col2:
# Total orders by Time of Day
    st.markdown("<h3 style='font-size:18px;'>Total Orders by Time of Day</h3>", unsafe_allow_html=True)
    fig7, ax7 = plt.subplots(figsize=(8, 4))
    sns.barplot(data=df_timeofday, x='time_category', y='order_item_id', palette='Set2', ax=ax7)
    ax7.set_ylabel('Orders')
    ax7.set_xlabel('Time of Day')
    ax7.set_title('Total Orders by Time of Day')

    total_time = df_timeofday['order_item_id'].sum()
    for i, val in enumerate(df_timeofday['order_item_id']):
        pct = val / total_time * 100
        ax7.text(i, val + 1000, f'{val}\n{pct:.1f}%', ha='center', fontsize=9)

    st.pyplot(fig7)
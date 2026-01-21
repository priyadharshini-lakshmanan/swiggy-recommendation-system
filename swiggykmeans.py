import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Swiggy Restaurant Recommender",
    layout="wide"
)

st.title("🍽️ Swiggy Restaurant Recommender")
@st.cache_data
def load_data():
    return pd.read_csv("C:\\Users\\ACER\\Desktop\\final_data.csv")

df = load_data()
st.sidebar.header("🔧 Your Preferences")

city = st.sidebar.selectbox("City",sorted(df["city_final"].dropna().unique()))
all_cuisines = (df["cuisine"].dropna().str.split(",").explode().str.strip().unique())
cuisine = st.sidebar.multiselect("Cuisine",sorted(all_cuisines))
min_rating = st.sidebar.slider("Min Rating",1.0, 5.0, 4.0, 0.1)
max_cost = st.sidebar.slider("Max Cost (₹)",200, 2000, 1000)

if st.sidebar.button("🔍 Get Recommendations", type="primary"):
    if not cuisine:
        st.warning("⚠️ Please select at least one cuisine.")
        st.stop()
    cuisine_pattern = "|".join(cuisine)
    exact_matches = df[
        (df["city_final"] == city) &
        (df["cuisine"].str.contains(cuisine_pattern, case=False, na=False)) &
        (df["rating"] >= min_rating) &
        (df["cost"] <= max_cost)
    ]

    exact_matches = exact_matches.drop_duplicates(subset="name")

    if len(exact_matches) > 0:
        top_recs = exact_matches.nlargest(10, "rating")

        col1, col2 = st.columns([2, 1])
        with col1:
            st.success(
                f"✅ Found {len(top_recs)} restaurants in **{city}** "
                f"for **{', '.join(cuisine)}**"
            )

            st.dataframe(
                top_recs[["name", "rating", "cost", "cuisine", "city_final"]],
                use_container_width=True,
                hide_index=True
            )

        with col2:
            st.subheader("📌 Your Preferences")

            st.write(f"**City:** {city}")
            st.write(f"**Cuisine:** {', '.join(cuisine)}")
            st.write(f"**Min Rating:** {min_rating} ⭐")
            st.write(f"**Max Budget:** ₹{max_cost}")

            st.metric("🍴 Restaurants Found", len(top_recs))

    else:
        fallback = df[
            (df["city_final"] == city) &
            (df["cuisine"].str.contains(cuisine_pattern, case=False, na=False))
        ].drop_duplicates(subset="name").nlargest(10, "rating")

        if len(fallback) > 0:
            st.info(
                f"📍 Showing best **{', '.join(cuisine)}** restaurants "
                f"in **{city}** (relaxed filters)"
            )

            st.dataframe(
                fallback[["name", "rating", "cost", "cuisine", "city_final"]],
                use_container_width=True,
                hide_index=True
            )
        else:
            st.error(
                f"❌ No restaurants found for **{', '.join(cuisine)}** in **{city}**."
            )





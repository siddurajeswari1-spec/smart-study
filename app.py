import streamlit as st
from datetime import datetime, timedelta

# 🌐 Page config
st.set_page_config(page_title="Smart Study Planner", page_icon="📚", layout="wide")

# 🎨 UI
st.markdown("""
    <style>
        .title {
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            color: #4CAF50;
        }
        .card {
            background-color: #1e1e1e;
            padding: 15px;
            border-radius: 12px;
            margin-bottom: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# 🧠 Title
st.markdown('<p class="title">📚 Smart Study Planner</p>', unsafe_allow_html=True)

# 📌 Inputs
subject = st.text_input("📖 Subject")
topics = st.text_area("📝 Topics (comma separated)")
days = st.slider("📅 Study Days", 1, 30, 7)
hours = st.slider("⏰ Hours per Day", 1, 10, 3)

generate = st.button("🚀 Generate Plan")

# 📊 Logic Planner
if generate:
    if subject and topics:

        topic_list = [t.strip() for t in topics.split(",") if t.strip()]

        if len(topic_list) == 0:
            st.warning("⚠️ Please enter valid topics")
        else:
            st.success("✅ Smart Study Plan Created!")

            today = datetime.today()

            # distribute topics evenly
            for i in range(days):
                date = today + timedelta(days=i)
                topic = topic_list[i % len(topic_list)]

                st.markdown(f"""
                <div class="card">
                    <h4>📅 Day {i+1} - {date.strftime('%d %b %Y')}</h4>
                    <p><b>Subject:</b> {subject}</p>
                    <p><b>Topic:</b> {topic}</p>
                    <p><b>Plan:</b> Study {topic} for {hours} hours → Practice + Revision</p>
                </div>
                """, unsafe_allow_html=True)

    else:
        st.warning("⚠️ Please fill all fields")
else:
    st.info("Enter details and click Generate Plan")
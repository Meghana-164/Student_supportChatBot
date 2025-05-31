import streamlit as st
from main_logic import generate_answer

st.set_page_config(page_title="Student Support Chatbot", page_icon="🎓", layout="centered")

st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>🎓 Student Support Chatbot</h1>
    <p style='text-align: center;'>Ask any academic question and get a smart answer from our AI tutor.</p>
    <hr style="border: 1px solid #f0f0f0;" />
""", unsafe_allow_html=True)

# Info note for long responses
st.info("ℹ️ For very detailed questions, responses may be trimmed. Try rephrasing or asking follow-ups.")

user_query = st.text_input("📌 Type your question below:", placeholder="e.g. What is the second law of thermodynamics?")

if st.button("💬 Get Answer"):
    if not user_query.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating answer, please wait..."):
            try:
                answer = generate_answer(user_query)
                st.success("✅ Response Generated!")
                st.markdown(f"""
                    <div style="background-color: #1e1e1e; color: #ffffff; padding: 15px; border-radius: 10px;">
                        <strong>🧾 Question:</strong> {user_query}<br><br>
                        <strong>📘 Answer:</strong> {answer}
                    </div>
                """, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"❌ Error: {e}")


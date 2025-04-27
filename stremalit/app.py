import streamlit as st
import openai  # Correct import

# --- Page Configuration ---
st.set_page_config(page_title="⚖️ Legal Chatbot", layout="centered")

# --- Title & Instructions ---
st.title("⚖️ Legal Chatbot")
st.write("""
Welcome! This chatbot is fine-tuned to answer questions related to **Arabic law**.
""")

# --- Set Your API Key Here (or use `st.secrets["openai_api_key"]`) ---
openai_api_key = ""

# --- Validate API Key ---
if not openai_api_key:
    st.info("🔑 Please add your OpenAI API key to continue.")
    st.stop()

# --- Set OpenAI API Key ---
openai.api_key = openai_api_key  # Correct way to set API key

# --- Initialize Message History ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant specialized in Arabic law."}
    ]

# --- Display Chat History (excluding system) ---
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- Chat Input at Bottom ---
if user_input := st.chat_input("Ask a legal question..."):

    # --- Show User Message ---
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # --- Stream Assistant Response ---
    try:
        # Stream the assistant's response
        stream = openai.ChatCompletion.create(
            model="ft:gpt-4.1-2025-04-14:securaxe::BP9vFtqa",  # <- Your fine-tuned model
            messages=st.session_state.messages,
            stream=True,
        )

        # Buffer to collect the full response
        full_response = ""

        for chunk in stream:
            if chunk.get("choices"):
                delta = chunk["choices"][0]["delta"]
                if "content" in delta:
                    full_response += delta["content"]  # Accumulate without newlines

        # Once all chunks are processed, display the final response in a single line
        response = full_response.strip()

        # --- Save Assistant Response ---
        st.session_state.messages.append({"role": "assistant", "content": response})

        # Display response in a single line (no newlines or breaks)
        with st.chat_message("assistant"):
            st.markdown(response.replace("\n", " "), unsafe_allow_html=True)

    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")

import streamlit as st

# Initialize session state to store chat history and input count
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
if "input_count" not in st.session_state:
    st.session_state["input_count"] = 1  # Start with one input field


# Function to append user input and response to chat history
def append_to_chat_history(user_input, response):
    st.session_state["chat_history"].append(f"User: {user_input}")
    st.session_state["chat_history"].append(f"ChatGPT: {response}")


# Function to handle user input and generate new input field
def handle_user_input():
    for i in range(st.session_state["input_count"]):
        user_input = st.text_area(f"You {i + 1}", key=f"user_input_{i}")

        if st.button(f"Send {i + 1}", key=f"send_{i}"):
            response = "This is a response from ChatGPT."  # Replace with actual ChatGPT response
            append_to_chat_history(user_input, response)
            st.session_state["input_count"] += 1
            st.experimental_rerun()


# Display chat history
st.write("### Chat History")
for line in st.session_state["chat_history"]:
    st.write(line)

# Generate new input fields based on the input count
handle_user_input()

# Save chat history to file
if st.button("Save Chat"):
    with open("chat_history.txt", "w") as f:
        for line in st.session_state["chat_history"]:
            f.write(line + "\n")
    st.success("Chat history saved to chat_history.txt")

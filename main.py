import streamlit as st
import openai

# Function to generate code using OpenAI API
def generate_code(prompt, language, engine, api_key):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine=engine,
        prompt=f"{prompt} in {language}",
        max_tokens=3048,
        temperature=0.5,
        n=1,
        stop=None,
        frequency_penalty=0.4,
        presence_penalty=0.6,
        best_of=1,
    )
    code = response.choices[0].text.strip()
    return code

# Streamlit UI for entering API key
st.title("SKAV Code Generator.")
api_key = st.text_input("Enter your OpenAI API key:")  # Define api_key here

# Check if API key is provided and valid
if api_key:
    try:
        # Attempt to generate a sample code to test the API key
        test_prompt = "Generate a sample code"
        test_language = "Python"
        engine = "text-davinci-003"
        generated_code = generate_code(test_prompt, test_language, engine, api_key)
        st.success("API key is valid. You can now use the application.")

        # Streamlit UI for code generation
        prompt = st.text_area("Enter your prompt:")
        language = st.text_input("Enter the programming language:")
        if st.button("Generate Code"):
            if prompt and language:
                generated_code = generate_code(prompt, language, engine, api_key)
                st.subheader("Generated Code:")
                st.code(generated_code)
            else:
                st.warning("Please enter a prompt and programming language.")
    except Exception as e:
        st.error(f"Invalid API key. Error: {e}")
else:
    st.warning("Please enter your OpenAI API key to start the application.")

javascript_code = """
<script src="https://cloud.openchat.so/search.js"></script>
<script>
    window.onload = () => {
        initilizeChatBot({
            initialFirstMessage: "Hello, I am SKAV Code Generator resources.",
            token: "WyvIEm9VwFj5SRBiv7if",
            //initiatorId: "search-openchat" // provide a unique id for the search widget if you want to have custom button
        });
    };
</script>
"""
st.markdown(javascript_code, unsafe_allow_html=True)
html_code = open("index.html", "r").read()

# Display the embedded HTML content
st.components.v1.html(html_code, height=500)

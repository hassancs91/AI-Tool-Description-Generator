import streamlit as st
import openai
import json

st.title("SEO Optimized Descriptions for AI Tools")

# Input for OpenAI API key
api_key = st.text_input("Enter your OpenAI API key", type="password")

# Inputs for the tool name and function
tool_name = st.text_input("Enter the Tool Name")
tool_function = st.text_input("Enter the Tool Function")

if api_key and tool_name and tool_function:
    openai.api_key = api_key

    # Define the prompt
    prompt = f'''Your task is to create SEO-optimized descriptions for AI tools on a new website. For each provided Tool Name and Function below:

    Tool Name: [{tool_name}]
    Tool Function: [{tool_function}]

    Please generate the following:
    1) Tool Description (3-4 sentences): Craft a unique, creative, and informative description that accurately outlines the tool's purpose and features while incorporating relevant keywords related to AI tools and their functions. Emphasize both the usefulness of the tool and its benefits.

    2) Meta Description (max 150 characters): Compose an engaging meta description highlighting the main benefits or uses of the tool within the character limit. Focus on what makes this specific tool stand out from others in its category, effectively capturing user interest.

    Ensure your responses are tailored specifically to each given Tool Name and Function,
    providing captivating descriptions that emphasize both SEO optimization and attracting potential users' attention.

    Output format: Json
    Example:
    {{
    tool_description : "",
    tool_meta :""
    }}

    '''

    # Button to generate responses
    if st.button("Generate"):
        messages = [
            {"role": "user", "content": prompt}
        ]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        json_data = json.loads(response['choices'][0]['message']['content'])
        #st.json(response.choices[0].text.strip())

        #st.write(json_data)
        # Access the tool description and meta description
        tool_description = json_data["tool_description"]
        tool_meta = json_data["tool_meta"]


        # Display each field in a separate box
        st.text_area("Tool Description:", value=tool_description, height=200, max_chars=None, key=None)
        st.text_area("Tool Meta:", value=tool_meta, height=200, max_chars=None, key=None)
import openai

# Set your API key for OpenAI
openai.api_key = 'sk-sYYkGEOZA0tx6ooLBA1JFPCoID3pW6Omjj5EnJ5GSdT3BlbkFJGhunXlJ9QWb8wSyPdIiq-dGSVrNNqP3S9_iOuty3IA'

def get_response_from_ai(user_input):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

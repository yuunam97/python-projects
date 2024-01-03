import openai
from dotenv import dotenv_values

config = dotenv_values(".env")

openai.api_key = config['OPENAI_API_KEY']

def generate_blog(paragraph_topic):
    response = openai.completions.create(
        model = 'text-davinci-002',
        prompt = 'Write a paragraph about the following topic:' + paragraph_topic,
        max_tokens = 400,
        temperature = 0.3
    )

    retrieve_blog = response.choices[0].text

    return retrieve_blog

print(generate_blog("why is Cape Town better than Johannesburg?"))

## Multiple paragraphs:

keep_writing = True

while keep_writing:
    answer = input("Write a paragraph? (Y/N)")
    if answer == "Y":
        paragraph_topic = input("What should this paragraph talk about?")
        print(generate_blog(paragraph_topic))
    else:
        keep_writing = False
        

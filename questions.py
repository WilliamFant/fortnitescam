# #pretty much just have to code this out so it will make a question-air into prompts for the ai

import openai
import codecs
import webbrowser

# Set up the OpenAI API client
openai.api_key = "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"

# Set up the model and prompt
model_engine = "text-davinci-003"

prompt = "hi"

# Initialize empty list to store answers
answers = [[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]]]


# Define boolean questions and follow-up questions
questions = {
    # Add more questions and follow-up questions as needed
    #0
    "Do you have a website name? ": [
        "What do you want to title the website? ",
        "What do your website to do? ",
    ],
    #1
    "Do you have a logo and branding in place? ": [
        "What color scheme do you want your website to be? ",

    ],
    #2
    "Will you need e-commerce functionality on the website? ": [
        "What types of products or services will you be selling? ",
    ],
    #3
    "Do you need a blog section on the website? ": [
        "What topics do you plan to cover in your blog? ",
    ],
    "Will the website require any custom functionality or programming? ": [
        "What specific features or functionality do you need that cannot be achieved through existing plugins or tools? ",
    ]
}
answers = [[] for _ in range(len(questions))]

for i, question in enumerate(questions):
    answer = input(question + " (yes/no) ")
    if answer.lower() == "yes":
        for followup in questions[question]:
            answer = input(followup + " ")
            answers[i].append(answer)

            prompt = prompt + answer

    else:
        for followup in questions[question]:
            answer = "null"
            answers[i].append(answer)

            prompt = prompt + answer



# Print the list of answers
print(answers)

prompt =  "Make a highly functional user friendly html javascript bootstrap and css that makes a user friendly modern website named" + answers[0][0] +  " that has information about " + answers[0][1] + "that uses  " + answers[1][0] + " as its colors that sells " + answers[2][0] + " and uses debit cards and paypal as a way to purchase things  with a blog section that talks about " + answers[3][0] + " that can be commented on liked and shared also include related pictures from the internet."

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=4000,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text

print(response)

  
# to open/create a new html file in the write mode
f = open('null.html', 'w')
  
# the html code which will go in the file GFG.html
html_template = (response)

  
# writing the code into the file
f.write(html_template)
  
# close the file
f.close()
  
# viewing html files
# below code creates a 
# codecs.StreamReaderWriter object
file = codecs.open("null.html", 'r', "utf-8")
  
# using .read method to view the html 
# code from our object
print(file.read())

webbrowser.open('null.html') 
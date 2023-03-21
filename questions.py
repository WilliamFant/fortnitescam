# #pretty much just have to code this out so it will make a question-air into prompts for the ai

import openai

# Set up the OpenAI API client
openai.api_key = "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"

# Set up the model and prompt
model_engine = "text-davinci-003"

# start of prompt
prompt = "Make a detailed html css and javascript document that "

# Initialize empty list to store answers
answers = [[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]]]


# Define boolean questions and follow-up questions
questions = {
    # Add more questions and follow-up questions as needed
    #0
    "Do you have a website name? ": [
        "What do you want to title the website? ",
        "What do your website to do? ",
        # "Who will see your website? "
    ],
    #1
    "Do you have a logo and branding in place? ": [
        "What color scheme do you want your website to be? ",
        # "What message or impression do you want your logo/branding to convey? ",
    ],
    #2
    "Will you need e-commerce functionality on the website? ": [
        "What types of products or services will you be selling? ",
        "Do you have a preferred payment gateway or shipping method? ",
        # "What security measures do you need in place to protect customer data and financial ,transactions? "
    ],
    #3
    "Do you need a blog section on the website? ": [
        "What topics do you plan to cover in your blog? ",
    ],
    #4
    # "Will the website require integration with any third-party tools or services? ": [
    #     "What specific third-party tools or services do you need to integrate with? ",
    #     "What data or functionality do you need to share between the website and these tools/services? ",
    #     "Do you have any existing APIs or integrations in place that need to be maintained or updated? "
    # ],
    # #5
    # "Do you need a contact form or any other types of forms on the website? ": [
    #     "What information do you need to collect from users through the forms? ",
    #     "Do you have any specific fields or questions that need to be included? ",
    #     "How will you want to receive and manage form submissions? "
    # ],
    # #6
    # "Will you need website hosting and maintenance services? ": [
    #     "What type of hosting do you prefer (shared, VPS, dedicated, cloud)? "
    # ],
    # #7
    # "Will you need a website privacy policy and terms of use? ": [
    #     "Do you have any specific legal requirements or regulations to comply with? ",
    #     "What information do you need to include in your privacy policy and terms of use? ",
    #     "Do you have any existing policies or guidelines that need to be updated or integrated into the website? "
    # ],
    # #8
    "Will the website require any custom functionality or programming? ": [
        "What specific features or functionality do you need that cannot be achieved through existing plugins or tools? ",
    #     "Do you have any technical requirements or constraints that need to be taken into consideration? ",
    ]
    # #9
    # "Will you need a content management system (CMS) for the website? ": [
    #     "What level of control do you want over website content and updates? ",
    # ],
    # #10
    # "Will the website require any special accessibility features? ": [
    #     "Are there any specific accessibility guidelines or standards you need to follow? ",
    #     "What types of users or disabilities will you need to accommodate? ",
    # ],
    # #11
    # "Will you need help with website promotion and marketing? ": [
    #     "What channels or tactics do you plan to use for website promotion and marketing? "
    # ]
}

# Loop through each question and ask the user for a yes or no answer
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

prompt =  "Make a highly functional user friendly html javascript bootstrap and css that makes a user friendly modern website named" + answers[0][0] +  " that has information about " + answers[0][1] + "that uses  " + answers[1][0] + " as its colors that sells " + answers[2][0] + " and uses debit cards and paypal as a way to purchase things " + answers[2][1] + " with a blog section that talks about " + answers[3][0] + " that can be commented on liked and shared also include related pictures from the internet."
#+ answers[4][0] + " functionality of 3rd party tools = " + answers[4][1] + " APIs = " + answers[4][2] + " forms = " + answers[5][0] + " form fields = " + answers[5][1] + " receive and manage form submissions = " + answers[5][2] + " hosting = " + answers[6][0] + " legal = " + answers[7][0] + " privacy policy = " + answers[7][1] + " policies = " + answers[7][2] + " specific features = " + answers[8][0] + " technical requirements = " + answers[8][1] + " content management = " + answers[9][0] + " accessibility guidelines = " + answers[10][0] + " types of users or disabilities " + answers[10][1] + "website promotion = " + answers[11][0]

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
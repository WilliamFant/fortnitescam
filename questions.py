# #pretty much just have to code this out so it will make a question-air into prompts for the ai

import openai

# Set up the OpenAI API client
openai.api_key = "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"

# Set up the model and prompt
model_engine = "text-davinci-003"

# start of prompt
prompt = "Make a html document that "

# Initialize empty list to store answers
answers = [[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]],[[None],[None],[None]]]


# Define boolean questions and follow-up questions
questions = {
    # Add more questions and follow-up questions as needed
    #0
    "Do you have a website name? ": [
        "What do you want to title the website? ",
        "What do your website to do? ",
        "Who will see your website? "
    ],
    #1
    "Do you have a logo and branding in place? ": [
        "what color scheme do you want your website to be? ",
        "What message or impression do you want your logo/branding to convey? ",
    ],
    #2
    "Will you need e-commerce functionality on the website? ": [
        "What types of products or services will you be selling? ",
        "Do you have a preferred payment gateway or shipping method? ",
        "What security measures do you need in place to protect customer data and financial ,transactions? "
    ],
    #3
    "Do you need a blog section on the website? ": [
        "What topics do you plan to cover in your blog? ",
    ],
    #4
    "Will the website require integration with any third-party tools or services? ": [
        "What specific third-party tools or services do you need to integrate with? ",
        "What data or functionality do you need to share between the website and these tools/services? ",
        "Do you have any existing APIs or integrations in place that need to be maintained or updated? "
    ],
    #5
    "Do you need a contact form or any other types of forms on the website? ": [
        "What information do you need to collect from users through the forms? ",
        "Do you have any specific fields or questions that need to be included? ",
        "How will you want to receive and manage form submissions? "
    ],
    #6
    "Will you need website hosting and maintenance services? ": [
        "What type of hosting do you prefer (shared, VPS, dedicated, cloud)? "
    ],
    #7
    "Will you need a website privacy policy and terms of use? ": [
        "Do you have any specific legal requirements or regulations to comply with? ",
        "What information do you need to include in your privacy policy and terms of use? ",
        "Do you have any existing policies or guidelines that need to be updated or integrated into the website? "
    ],
    #8
    "Will the website require any custom functionality or programming? ": [
        "What specific features or functionality do you need that cannot be achieved through existing plugins or tools? ",
        "Do you have any technical requirements or constraints that need to be taken into consideration? ",
    ],
    #9
    "Will you need a content management system (CMS) for the website? ": [
        "What level of control do you want over website content and updates? ",
    ],
    #10
    "Will the website require any special accessibility features? ": [
        "Are there any specific accessibility guidelines or standards you need to follow? ",
        "What types of users or disabilities will you need to accommodate? ",
    ],
    #11
    "Will you need help with website promotion and marketing? ": [
        "What channels or tactics do you plan to use for website promotion and marketing? "
    ]
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

            # Generate a response
            # completion = openai.Completion.create(
            #     engine=model_engine,
            #     prompt=prompt,
            #     max_tokens=1024,
            #     n=1,
            #     stop=None,
            #     temperature=0.5,
            # )

            # response = completion.choices[0].text
            # print(response)
    else:
        for followup in questions[question]:
            answer = "null"
            answers[i].append(answer)

            prompt = prompt + answer



# Print the list of answers
print(answers)

prompt =  "Make a  user friendly and useful html and css document using this information. name = " + answers[0][0] +  " use = " + answers[0][1] + " users =" + answers[0][2] + " color scheme = " + answers[1][0] + " impression to people = " + answers[1][1] + " products = " + answers[2][0] + "payment method = " + answers[2][1] + " security = " + answers[2][2] + " blog topics = " + answers[3][0] + " 3rd party tools = " + answers[4][0] + " functionality of 3rd party tools = " + answers[4][1] + " APIs = " + answers[4][2] + " forms = " + answers[5][0] + " form fields = " + answers[5][1] + " receive and manage form submissions = " + answers[5][2] + " hosting = " + answers[6][0] + " legal = " + answers[7][0] + " privacy policy = " + answers[7][1] + " policies = " + answers[7][2] + " specific features = " + answers[8][0] + " technical requirements = " + answers[8][1] + " content management = " + answers[9][0] + " accessibility guidelines = " + answers[10][0] + " types of users or disabilities " + answers[10][1] + "website promotion = " + answers[11][0]
# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)


# Welcome to [Website Name], the [Purpose of Website] website for [Target Audience]! Our website features [Main Features of Website], and offers a variety of [Content Types] for your browsing pleasure.

# Our [Logo and Branding] convey [Message or Impression]. We also offer [E-commerce Functionality], with a range of [Products or Services] available for purchase. Our secure payment gateway and [Shipping Method] ensure that your transactions are safe and convenient.

# Check out our [Blog Section], where we cover [Blog Topics] on a [Frequency] basis. We take pride in our engaging and informative content, and are always open to new ideas and guest bloggers.

# For your convenience, we also offer integration with [Third-Party Tools or Services], so you can easily access [Data or Functionality] across platforms. We also have a [Contact Form] and other forms available for you to submit feedback, requests, and inquiries.

# Our website is hosted on [Type of Hosting], and our team of experts is always on hand to provide [Website Maintenance Services]. We take your privacy seriously, and have a comprehensive [Privacy Policy and Terms of Use] in place to protect your data and ensure compliance with [Legal Requirements or Regulations].

# If you need any custom features or programming, we've got you covered. Our skilled developers can create [Custom Functionality] to meet your specific needs and technical requirements.

# Our website is powered by [Content Management System], giving you full control over your content and updates. We also take accessibility seriously, and have [Accessibility Features] in place to ensure that all users can access our website with ease.

# Last but not least, we offer website promotion and marketing services to help you reach your target audience and achieve your goals. Whether you need help with [Marketing Channels and Tactics], SEO, or other digital marketing strategies, our team is here to help.

# Thank you for choosing [Website Name] as your go-to source for [Purpose of Website] content. We hope you enjoy browsing our website, and look forward to hearing from you soon!


# for i, not_bool in enumerate(not_bool):
#     answer = input(f"{i+1}. {not_bool} ")

#     prompt = "Make a html document that " + answer

#     # Generate a response
#     completion = openai.Completion.create(
#         engine=model_engine,
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )

#     response = completion.choices[0].text
#     print(response)

# "What do you want to title the website? Our website will be called " + answers [0][0] + ".

# "What do you want your website to do? Our website will be a " + answers [0][1] + " website that " + answers [0][1] + ".

# "Who will see your website? Our website will be seen by " + answers [0][2] + ".

# "What color scheme do you want your website to have? Our website will have a " + answers [1][0] + " color scheme that conveys " + answers [1][1] + ".

# "What types of products or services will you be selling? Our website will sell " + answers [2][0] + " and we prefer to use " + answers [2][1] + " as our payment gateway/shipping method. We also need to have " + answers [2][2] + " security measures in place to protect our customer's data and financial transactions." + "What topics do you plan to cover in your blog? Our blog will cover " + answers [][] + " and we plan to publish new posts " + answers [][] + "."

# "What specific third-party tools or services do you need to integrate with? We need to integrate with " + answers [][] + " to share " + answers [][] + " and we have existing APIs or integrations that need to be maintained/updated with " + answers [][] + ".

# "What information do you need to collect from users through the forms? Our contact form will collect " + answers [][] + " and we need to have specific fields or questions included for " + answers [][] + ". We will receive and manage form submissions through " + answers [][] + ".

# "What type of hosting do you prefer? We prefer " + answers [][] + " hosting.

# "What specific legal requirements or regulations do you need to comply with? Our privacy policy and terms of use need to comply with " + answers [][] + " and include " + answers [][] + ". We also have existing policies or guidelines that need to be updated/integrated into the website."

# What specific features or functionality do you need that cannot be achieved through existing plugins or tools? Our website requires " + answers [][] + " and we have specific technical requirements or constraints to take into consideration.

# What level of control do you want over website content and updates? We need a " + answers [][] + " content management system (CMS) for the website.

# Are there any specific accessibility guidelines or standards you need to follow? Our website needs to accommodate " + answers [][] + " and we will need help from " + answers [][] + " to ensure accessibility.

# What channels or tactics do you plan to use for website promotion and marketing? We plan to use " + answers [][] + " for website promotion and marketing, and we have existing marketing materials or campaigns that need to be integrated into the website. We will also need help with " + answers [][] + " for SEO and other digital marketing strategies.""
# Start with the basic structure of an HTML document
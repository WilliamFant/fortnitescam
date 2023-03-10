# Define the questions and follow-up questions
questions = {
    "Do you have a website name? ": [
        "What do you want to title the website? ",
        "What do your website to do? ",
        "Who will see your website? "
    ],
    "Do you have a logo and branding in place? ": [
        "what color scheme do you want your website to be? ",
        "What message or impression do you want your logo/branding to convey? ",
        "Will you need help with creating a logo and developing branding guidelines? "
    ],
    "Will you need e-commerce functionality on the website? ": [
        "What types of products or services will you be selling? ",
        "Do you have a preferred payment gateway or shipping method? ",
        "What security measures do you need in place to protect customer data and financial transactions? "
    ],
    "Do you need a blog section on the website? ": [
        "What topics do you plan to cover in your blog? ",
        "How frequently do you plan to publish new blog posts? ",
        "Will you need help with creating and managing blog content? "
    ],
    "Will the website require integration with any third-party tools or services? ": [
        "What specific third-party tools or services do you need to integrate with? ",
        "What data or functionality do you need to share between the website and these tools/services? ",
        "Do you have any existing APIs or integrations in place that need to be maintained or updated? "
    ],
    "Do you need a contact form or any other types of forms on the website? ": [
        "What information do you need to collect from users through the forms? ",
        "Do you have any specific fields or questions that need to be included? ",
        "How will you want to receive and manage form submissions? "
    ],
    "Will you need website hosting and maintenance services? ": [
        "What type of hosting do you prefer (shared, VPS, dedicated, cloud)? "
    ],
    "Will you need a website privacy policy and terms of use? ": [
        "Do you have any specific legal requirements or regulations to comply with? ",
        "What information do you need to include in your privacy policy and terms of use? ",
        "Do you have any existing policies or guidelines that need to be updated or integrated into the website? "
    ],
    "Will the website require any custom functionality or programming? ": [
        "What specific features or functionality do you need that cannot be achieved through existing plugins or tools? ",
        "Do you have any technical requirements or constraints that need to be taken into consideration? ",
    ],
    "Will you need a content management system (CMS) for the website? ": [
        "What level of control do you want over website content and updates? ",
    ],
    "Will the website require any special accessibility features? ": [
        "Are there any specific accessibility guidelines or standards you need to follow? ",
        "What types of users or disabilities will you need to accommodate? ",
        "Will you need any third-party tools or services to help with accessibility? "
    ],
    "Will you need help with website promotion and marketing? ": [
        "What channels or tactics do you plan to use for website promotion and marketing? ",
        "Do you have any existing marketing materials or campaigns that need to be integrated into the website? ",
        "Will you need any help with search engine optimization (SEO) or other digital marketing strategies? "
    ]
}

# Prompt the user for their answers to the questions
answers = []

# Loop through each question and ask the user for their answer
for questions, follow_up_questions in questions.items():
    # Ask the initial question
    answer = input(questions)
    # Store the answer in tds
    #he answers dictionary
    answers[i] = [answer]
    # Loop through any follow-up questions and ask for the user's answer
    for follow_up_question in follow_up_questions:
        follow_up_answer = input(follow_up_questions)
        # Add the follow-up answer to the answers list for the current question
        answers[questions].append(follow_up_answer)

# Use the answers dictionary to generate the final prompt
prompt = "Welcome to " + answers["Do you have a website name? "][0] + ", the " + answers["Do you have a logo and branding in place? "][1] + " website for " + answers["Do you have a website name? "][2] + "! Our website features " + answers["Do you have a website name? "][3] + ", and offers a variety of " + answers["Will you need e-commerce functionality on the website? "][0] + " for your browsing pleasure. Our " + answers["Do you have a logo and branding in place? "][0] + " and branding convey " + answers["Do you have a logo and branding in place? "][1] + ". We also offer " + answers["Will you need e-commerce functionality on the website? "][1] + ", with a range of " + answers["Will you need e-commerce functionality on the website? "][2] + " available for purchase. Our secure payment gateway and " + answers["Will you need e-commerce functionality on the website? "][3] + " ensure that your transactions are safe and convenient. Check out our " + answers["Do you need a blog section on the website? "][0] + ", where we cover " + answers["Do you need a blog section on the website? "][1] + " on a " + answers["Do you need a blog section on the website? "][2] + " basis. We take pride in our engaging and informative content, and are always open to new ideas and guest bloggers. For your convenience, we also offer integration with " + answers["Will the website require integration with any third-party tools or services? "][0] + ", so you can easily access " + answers["Will the website require integration with any third-party tools or services? "][1] + " across platforms. We also have a " + answers["Do you need a contact form or any other types of forms on the website? "][0] + " and other forms available for you to submit feedback, requests, and inquiries. Our website is hosted on " + answers["Will you need website hosting and maintenance services? "][0] + ", and our team of experts is always on hand to provide " + answers["Will you need website hosting and maintenance services? "][1] + ". We take your privacy seriously, and have a comprehensive " + answers["Will you need a website privacy policy and terms of use? "][0] + " in place to protect your data and ensure compliance with " + answers["Will you need a website privacy policy and terms of use? "][1] + ". If you need any custom features or programming, we've got you covered. Our skilled developers can create " + answers["Will the website require any custom functionality or programming? "][0] + " to meet your specific needs and technical requirements. Our website is powered by " + answers["Will you need a content management system (CMS) for the website? "][0] + ", giving you full control over your content and updates. We also take accessibility seriously, and have " + answers["Will the website require any special accessibility features? "][0] + " in place to ensure that all users can access our website with ease. Last but not least, we offer website promotion and marketing services to help you reach your target audience and achieve your goals. Whether you need help with " + answers["Will you need help with website promotion and marketing? "][0] + ", SEO, or other digital marketing strategies, our team is here to help. Thank you for choosing " + answers["Do you have a website name? "][0] + " as your go-to source for " + answers["Do you have a website name? "][2] + " content. We hope you enjoy browsing our website, and look forward to hearing from you soon!"

print(prompt)

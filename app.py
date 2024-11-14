import os
import random
import re
import logging
import g4f
import g4f.Provider
from flask import Flask, request, jsonify, send_file, render_template
from flask_limiter import Limiter
from pptx import Presentation

app = Flask(__name__)

logging.basicConfig(filename='app.log', level=logging.INFO)

limiter = Limiter(
    app,
    default_limits=["10 per day"],
)

PROMPT_TEMPLATE = """Write a presentation/powerpoint about the user's topic. You only answer with the presentation. Follow the structure of the example.
Notice
-You do all the presentation text for the user.
-You write the texts no longer than 250 characters!
-You make very short titles!
-You make the presentation easy to understand.
-The presentation has a table of contents.
-The presentation has a summary.
-At least 8 slides.

Example! - Stick to this formatting exactly!
#Title: TITLE OF THE PRESENTATION

#Slide: 1
#Header: table of contents
#Content: 1. CONTENT OF THIS POWERPOINT
2. CONTENTS OF THIS POWERPOINT
3. CONTENT OF THIS POWERPOINT
...

#Slide: 2
#Header: TITLE OF SLIDE
#Content: CONTENT OF THE SLIDE

#Slide: 3
#Header: TITLE OF SLIDE
#Content: CONTENT OF THE SLIDE

#Slide: 4
#Header: TITLE OF SLIDE
#Content: CONTENT OF THE SLIDE

#Slide: 5
#Headers: summary
#Content: CONTENT OF THE SUMMARY

#Slide: END
"""

def create_ppt_text(input_topic):
    """Generate presentation content using the g4f provider."""
    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            provider=g4f.Provider.ChatGpt,
            messages=[
                {"role": "system", "content": PROMPT_TEMPLATE},
                {"role": "user", "content": f"The user wants a presentation about {input_topic}"}
            ],
            stream=True,
        )
    except Exception as e:
        print(f"Error during API call: {e}")
        return ""

    presentation_text = ""
    for message in response:
        if "[DONE]" in str(message):
            continue
        presentation_text += str(message)

    output_path = f'Cache/{input_topic}.txt'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(presentation_text)

    return presentation_text


def create_ppt(text_file, design_number, ppt_name, host_url):
    """Create a PowerPoint presentation using the specified design template and open it."""
    design_path = f"Designs/Design-{design_number}.pptx"
    print(f"Looking for design file at: {os.path.abspath(design_path)}")

    if not os.path.exists(design_path):
        raise FileNotFoundError(f"Design template not found at {design_path}. Please check the file path.")

    prs = Presentation(design_path)
    slide_count = 0
    header = ""
    content = ""
    last_slide_layout_index = -1

    with open(text_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#Title:'):
                header = line.replace('#Title:', '').strip()
                slide = prs.slides.add_slide(prs.slide_layouts[0])  # Title slide
                slide.shapes.title.text = header
                continue

            elif line.startswith('#Slide:'):
                if slide_count > 0:
                    slide = prs.slides.add_slide(prs.slide_layouts[last_slide_layout_index])
                    slide.shapes.title.text = header
                    slide.shapes.placeholders[1].text = content

                content = ""
                slide_count += 1
                last_slide_layout_index = random.choice([1, 7, 8])
                continue

            elif line.startswith('#Header:'):
                header = line.replace('#Header:', '').strip()
                continue

            elif line.startswith('#Content:'):
                content = line.replace('#Content:', '').strip()
                next_line = f.readline().strip()
                while next_line and not next_line.startswith('#'):
                    content += '\n' + next_line
                    next_line = f.readline().strip()
                continue

    output_file_path = f'GeneratedPresentations/{ppt_name}.pptx'
    prs.save(output_file_path)

    abs_path = os.path.abspath(output_file_path)
    os.startfile(abs_path)

    return f"{host_url}{output_file_path}"


@app.route('/GeneratedPresentations/<path:path>')
def send_generated_presentation(path):
    return send_file(f'GeneratedPresentations/{path}', as_attachment=True)


@app.route("/")
def home():
    return render_template("powerpoint.html", charset="utf-8")


@app.route('/generate', methods=['POST'])
@limiter.limit("10 per day")
def generate_presentation():
    topic = request.form.get('topic')
    if not topic:
        return "Please provide a topic.", 400

    ppt_link = get_bot_response(topic, request.host_url)
    return ppt_link


def get_bot_response(msg, host_url="http://localhost:5000/"):
    """Process user input and generate a PowerPoint presentation."""
    user_input = msg.strip()
    last_char = user_input[-1]
    input_string = re.sub(r'[^\w\s.\-\(\)]', '', user_input).rstrip()
    number = 1

    if last_char.isdigit():
        number = int(last_char)
        input_string = user_input[:-2].rstrip()
        print(f"Design Number: {number} selected.")
    else:
        print("No design specified, using default design...")

    os.makedirs('Cache', exist_ok=True)

    ppt_text = create_ppt_text(input_string)
    if not ppt_text:
        return "Error generating presentation text."

    text_file_path = f'Cache/{input_string}.txt'

    if not os.path.exists(text_file_path):
        return f"Error: The file {text_file_path} was not created."

    ppt_link = create_ppt(text_file_path, number, input_string, host_url)
    return str(ppt_link)

task = input("Task=>")
if "presentation" in task or "ppt" in task:
    task=task.replace("jarvis","")
    task = task.replace("make a presentation", "")
    task = task.replace("make a ppt", "")
    task=task.replace("create a presentation","")
    task=task.replace("create a ppt","")
    task=task.replace("powerpoint","")
    task=task.replace("about","")
    task=task.replace("with design","")
    topic=task.replace(task[-1],"")
    task = task.replace(" ","")
    print(task)
    print(topic)
    print("Generating presentation content for you sir. Please hold on.")
    print("Fetching information to create an engaging presentation.")
    get_bot_response(task)
    print(f"Saving the presentation as {topic}.")
    print(f"Your presentation on {topic} is complete and ready for review sir.")
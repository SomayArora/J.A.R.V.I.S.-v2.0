import google.generativeai as genai
import os

task = input("TASK=>")

if "write" in task and "code" in task:
    print("Initiating code writing process.")
    API = "AIzaSyCWWP_F_XxKUlS2kZrmRkC1-bV-fDoci5Q"
    prompt = f"{task}, write only code no explanation"
    genai.configure(api_key=API)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt).text
    response = response.replace("`", "").replace("python", "")
    language_extensions = {
        'python': '.py',
        'java': '.java',
        'cpp': '.cpp',
        'c++': '.cpp',
        'javascript': '.js',
        'typescript': '.ts',
        'html': '.html',
        'css': '.css',
    }

    for language, extension in language_extensions.items():
        if language in prompt.lower():
            ext = extension

    file_name = prompt.replace("write a","").replace("code","").replace("for","").replace("in python","").replace("in html","").replace("in javascript","").replace("in cpp","").replace("in c++","").replace("in typescript","").replace("in css","").replace(", write only  no explanation","").replace(" ","_")

    def write_code_to_file(code, filename=f"{file_name}{ext}"):
        with open(filename, 'w') as file:
            file.write(code)
        print(f"Code written to {filename}")

    def open_code_file(filename=f"{file_name}{ext}"):
        os.system(f'start {filename}')

    write_code_to_file(response)
    print("Code has been successfully written sir.")
    open_code_file()
    print("All done! Here’s the final code.")




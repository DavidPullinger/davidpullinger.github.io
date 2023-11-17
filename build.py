import os
import json

def generate_project_html(project):
    html = f'''
    <div class="border-4 border-black">
        <h2>{project['name']}</h2>
        <p>{project['description']}</p>
        <div class="technologies">
    '''
    for technology in project['technologies']:
        html += f'<p>{technology}</p>'
    html += '''
        </div>
        <div class="images">
    '''
    for image in project['images']:
        html += f'<img src="images/{image}" alt="{image}">'
    html += '''
        </div>
    </div>
    '''
    return html

directory = 'projects'
output_file = 'index.html'
projects = []
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        with open(os.path.join(directory, filename)) as file:
            project_data = json.load(file)
            projects.append(project_data)

projects_html = ''
for project in projects:
    projects_html += generate_project_html(project)

# Create the index.html file
with open(output_file, 'w') as output:
    html_content = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="dist_styles.css">
        <title>HOME | david</title>
    </head>
    <body>
        <div class="flex justify-between">
            <p id="title" class="font-bold pb-5 underline text-lg">David Pullinger</p>
            <p>github</p>
        </div>
        <div class="py-3">
            <h1 class="text-5xl pb-2 font-black">About Me</h1>
            <p class="w-[60ch]">Dynamic, results-driven recent graduate with a robust academic background in Computer Science and Mathematics. Excel at tackling intricate technical challenges and thrive in high-stakes scenarios, driven by a genuine passion for critical problem-solving. Hands-on experience in full-stack development and a keen interest in cutting-edge technologies like big data, computer vision, and machine learning.</p>
        </div>
        <div class="py-3">
            <h1 class="text-5xl pb-2 font-black">Projects</h1>
            {projects_html}
        </div>
    </body>
    </html>
    '''
    output.write(html_content)

print("Successfully generated HTML")


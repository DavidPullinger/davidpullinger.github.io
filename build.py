import os
import json

project_dir = 'projects'
project_image_dir = f'{project_dir}/images'
output_file = 'index.html'

def generate_technologies(technologies):
    html = ""
    for technology in technologies:
        html += f'<p class="bg-accent border-2 border-black px-2 py-1 font-bold">{technology}</p>'
    return html

def generate_images(images):
    html = ""
    for image in images:
        html += f'<img src={project_image_dir}/{image} alt={image} onclick="enlargeImage(event)" class="max-w-[90%] max-h-80 rounded-lg flex cursor-zoom-in" />'
    return html

def generate_project_html(project):
    html = f'''
    <div class="border-2 border-black p-4 flex flex-col gap-3 h-fit bg-secondary" style="box-shadow: 8px 8px 0 0 black">
        <div class="flex justify-between items-center">
            <h2 class="text-2xl font-bold">{project['name']}</h2>
            <div class="flex gap-3 items-center">
                <a target="_blank" rel="noreferrer" href={project["giturl"]}>
                    <img class="w-6" src="assets/github.png"/>
                </a>
                {f'<a target="_blank" rel="noreferrer" href={project["url"]}><img class="w-6" src="assets/web.png"/></a>'
                 if project.get("url") else ''}
            </div>
        </div>
        <h3 class="text-xl opacity-70 -mt-3">{project['type']} Project &bull; {project['year']}</h3>
        <p>{project['description']}</p>
        <div class="flex gap-3 flex-wrap">
            {generate_technologies(project['technologies'])}
        </div>
        <div class="flex items-center gap-3 w-full overflow-x-scroll scroll-shadows" style="overscroll-behavior-x:none">
            {generate_images(project['images'])}
        </div>
    </div>
    '''
    return html

projects = []
filenames = sorted(os.listdir(project_dir),reverse=True)
filenames.remove("template.json")
for filename in filenames:
    if filename.endswith('.json'):
        with open(os.path.join(project_dir, filename)) as file:
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
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;900&family=Space+Mono:wght@700&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="assets/dist_styles.css">
        <script src="assets/main.js" defer></script>
        <link rel="icon" type="image/x-icon" href="assets/favicon.ico">
        <title>HOME | david</title>
    </head>
    <body class="bg-primary py-4 px-6 md:py-8 md:px-12">
        <div id="overlay" class="fixed inset-0 bg-black bg-opacity-70 hidden"></div>
        <div class="flex justify-between items-center mb-5">
            <p id="title" class="font-bold underline text-lg">David Pullinger</p>
            <div class="flex gap-3 items-center">
                <a href="https://github.com/DavidPullinger" target="_blank" rel="noreferrer">
                    <img class="w-6" src="assets/github.png"/>
                </a>
                <a href="https://www.linkedin.com/in/david-pullinger-94a3a420b/" target="_blank" rel="noreferrer">
                    <img class="w-6" src="assets/linkedin.png"/>
                </a>
            </div>
        </div>
        <div class="py-3 h-[100svh] relative">
            <h1 class="text-5xl sm:text-6xl !leading-normal md:text-[100px] pb-3 font-bold mono">$ whoami<span class="blinking-cursor">|</span></h1>
            <div class="text-base md:text-lg flex flex-col gap-3">
                <div>
                    <p class="text-secondary font-bold text-2xl">01</p>
                    <p>Dynamic, results-driven recent graduate with a robust academic background in Computer Science and Mathematics.</p>
                </div>
                <div>
                    <p class="text-secondary font-bold text-2xl">02</p>
                    <p>Excel at tackling intricate technical challenges and thrive in high-stakes scenarios, driven by a genuine passion for critical problem-solving.</p>
                </div>
                <div>
                    <p class="text-secondary font-bold text-2xl">03</p>
                    <p>Hands-on experience in full-stack development and a keen interest in cutting-edge technologies like big data, blockchain, and machine learning.</p>
                </div>
            </div>
            <div id="scroll-indicator" class="absolute bottom-[12%] right-0 border-4 border-secondary rounded-full h-20 w-10"></div>
        </div>
        <div class="py-3 flex flex-col gap-3">
            <h1 class="text-5xl sm:text-6xl !leading-normal md:text-[100px] pb-3 font-bold mono tracking-tighter">$ ls projects<span class="blinking-cursor">|</span></h1>
            <div class="grid grid-cols-1 lg:grid-cols-2 2xl:grid-cols-4 gap-6">
                {projects_html}
            </div>
        </div>
    </body>
    </html>
    '''
    output.write(html_content)

print("Successfully generated HTML")

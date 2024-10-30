# Python Flask - microblog Project

### The challenge

Users should be able to:

This is a simple blog application built with Flask and MongoDB. Users can add blog entries, which are saved in a MongoDB database and displayed on the main page. The application uses Flask’s templating and routing capabilities, and the blog entries are rendered dynamically in the UI.

Key Features
Create and View Blog Entries: Users can submit new blog entries that are saved with a timestamp. Each entry is displayed on the home page with the submission date formatted as "Month Day".

Dynamic Templating: The home.html template is used to display blog entries in a user-friendly format.
Database Storage: Blog entries are stored in a MongoDB database, allowing for persistence across sessions.


![Screenity video - Oct 30, 2024](https://github.com/user-attachments/assets/9954b686-09bb-4c27-beee-193f8b3da499)


## My process

### Built with

- Flask
- Jinja2
- Python
- Flask
- MongoDb
- Semantic HTML5 mark

### What I learned

1. Connecting Flask with MongoDB for Data Storage

```python
client = MongoClient("mongodb+srv://marlonmontenegro:********@datahive.fzhuskp.mongodb.net/")
app.db = client.MicroBlog

if request.method == "POST":
    entry_content = request.form.get("content")
    formated_date = datetime.today().strftime("%Y-%m-%d")
    app.db.entries.insert_one({"content": entry_content, "date": formated_date})
```

What I Learned:

- How to work with NoSQL databases using MongoDB to store structured data.
- How to connect to a remote MongoDB instance using the pymongo library.
- Capturing POST requests from forms and saving user inputs into a database.

2. Dynamic HTML Rendering with Jinja2 Templates
   
```html
{% for entry in entries %}
<article class="entry">
    <div>
        <h2 class="entry__title">{{ entry[0] | truncate(30, true) }}</h2>
        <time class="entry__date" datetime="{{ entry[1] }}"> • {{ entry[2] }}</time>
    </div>
    <p class="entry__content">
        {{ entry[0] }}
    </p>
</article>
{% endfor %}
```

What I Learned:

- Using Jinja2 templates to dynamically render content in HTML from backend logic.
- Implementing control flow structures such as for loops to display database content in the UI.
- Applying template filters like truncate() to improve the display of data.


### Continued Development

In future projects, I plan to dive deeper into **using Flask with databases** to enhance my ability to manage and manipulate data efficiently. I also aim to further develop my skills in **Jinja2 templates** to improve dynamic content rendering and create more polished, user-friendly interfaces. Specifically, I want to:

- Refine my understanding of **CRUD operations** (Create, Read, Update, Delete) within Flask applications connected to databases.
- Explore **more advanced template logic with Jinja2**, such as custom filters and macros, to enhance reusability and maintainability of templates.


## Author

- Website - [@Marlon Montenegro](https://marlonmontenegro.github.io/montenegro-portfolio/)
- Frontend Mentor - [@MarlonMontenegro](https://www.frontendmentor.io/profile/MarlonMontenegro)
- LinkedIn - [@MarlonMontenegro](https://www.linkedin.com/in/montenergopaz/)


## Acknowledgments

This project was developed as part of the course created by José Salvatierra on Udemy. 
I would like to express my gratitude for the knowledge and guidance provided throughout the course, which enabled me to successfully complete this project.

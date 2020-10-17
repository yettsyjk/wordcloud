blogTitle=input(" Please enter a title for this page: ")
blogDesc=input(" Please enter a description for this page: ")

def myNewBlog(blogTitle, blogDesc):
    file=open("C:/Users/yettsyknapp/Desktop/blog.html", "wt")
    file.write("""
    <!DOCTYPE html>
    <html>
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1"/>
    <title>Life within Highlands Ranch | Yettsy Knapp</title>
    <style type="text/css">
    body(
        color: #000000;
        background-color: #75A9B8;
        margin: 0;

    )
    </style>
    </head>
    <body>
    <h3>"""+blogTitle+"""</h3>
    <h3>"""+blogDesc+"""</h3>
    <h3>Connected here</h3>
    <p><a href="C:/Users/yettsyknapp/MSCyber/wordcloud/blog.txt">Link to Blog</a></p>
    </body>
    </html>
    """)
    file.close()

myNewBlog(blogTitle, blogDesc)
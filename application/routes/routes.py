def add(app):

    from flask import render_template


    @app.route("/")
    def home():

        posts = [post for post in app.client.home.posts.find()]

        return render_template(
            'home.html',
            title='Good Evening,',
            subtitle='Web!',
            collection=app.client.home.posts,
            posts=posts,
            )

"""Add crud functionality to handle our database"""

def add(app):

    from flask import redirect, url_for

    @app.route('/new/<title>/<text>')
    def new(title, text):
        """The structure here is:
           app.client.database.collection
           we insert a new document. """

        doc = {'title': title, 'text': text}
        app.client.home.posts.insert_one(doc)
        
        return redirect(url_for('home'))


    @app.route('/drop')
    def drop():
        """Drops all documents from the blogpost collection. """
        app.client.home.posts.drop()

        return redirect(url_for('home'))

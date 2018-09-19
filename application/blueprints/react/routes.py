def add(app):

    from flask import render_template
    from flask import Blueprint

    bprint = Blueprint(
        'react',
        __name__,
        static_url_path='/react/static',
        static_folder='./static',
        template_folder='./templates'
        )

    @bprint.route("/react")
    def react():
        return render_template('react.html')

    return app.register_blueprint(bprint)

def add(app):

    from flask import render_template
    from flask import Blueprint

    bprint = Blueprint(
        'blueprint',
        __name__,
        static_url_path='/bprint/static',
        static_folder='./static',
        template_folder='./templates'
        )

    @bprint.route("/blueprint")
    def blueprint():
        return render_template(
            'bprint.html',
            title='Blueprint',
            subtitle='my secret portal',
            )


    return app.register_blueprint(bprint)

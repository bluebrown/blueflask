def add(app):

    from flask import render_template
    from flask import Blueprint

    bprint = Blueprint(
        'admin',
        __name__,
        static_url_path='/bprint/static',
        static_folder='./static',
        template_folder='./templates'
        )

    @bprint.route("/admin")
    def blueprint():
        return render_template(
            'admin.html',
            title='Admin Page',
            subtitle='my secret portal',
            )


    return app.register_blueprint(bprint)

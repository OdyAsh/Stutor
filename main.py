from website import create_app #website is a python package as it contains __init__.py file, which automatically runs its code

app = create_app()

if __name__ == '__main__': #ensures that if main.py is imported, all of what is inside this if condition will not be run
    app.run(debug=True) #runs the webserver, "debug=True" means that each time we make a new change in the code, the server will re-run
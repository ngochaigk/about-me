from flask import Flask, render_template
app=Flask(__name__)

@app.route('/about-me')
def index():
    about={'Name':'Hai Nguyen','Work':'Creative','Hobbies':['Read books','Write']}
    return render_template('me.html',data=about)

@app.route('/school')
def school():
    return '''<html>
    <a href="http://techkids.vn">school</a>
    </html>
    '''

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000,debug=True)




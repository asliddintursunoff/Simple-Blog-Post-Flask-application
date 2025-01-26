from flask import Flask, request, jsonify,render_template,flash,redirect
app = Flask(__name__, static_url_path='/', static_folder='static',template_folder='templates')
app.config['SECRET_KEY'] = 'mysecretkey'
lst = []


def adding_id(lst):   
    for index,item in  enumerate(lst):
        item['id'] = index
        
    return lst[::-1]

@app.route('/')
def home():
    return render_template('index.html',data=adding_id(lst))

@app.route('/admin' , methods=['GET', 'POST'])
def create_post():
    
    if request.method == "POST":
        title = request.form['title']
        postbody = request.form['postbody']
        img = request.files['img']
        img.save(f'static/images/{img.filename}')
        data = {'title':title,'postbody':postbody,'img':f"images/{img.filename}"}
        
        lst.append(data)
        flash('Post created successfully')
        return redirect('/')
    else: 
        return render_template('admin.html')



@app.route('/<int:id>' , methods=['GET', 'PUT','POST'])
def edit_post(id):
    for value in  adding_id(lst):
        if value['id']==id:
            render_template('editing.html')
        
            if request.method == "POST":
                    title = request.form['title']
                    postbody = request.form['postbody']
                    img = request.files['img']
                    img.save(f'static/images/{img.filename}')
                    value['title'] = title
                    value['postbody'] = postbody
                    value['img'] = f"images/{img.filename}"
                    flash('Post updated successfully')
                    return redirect('/')
            else:
                flash( 'Post not found')
         
    return render_template('editing.html')
@app.route("/post/<int:id>")
def post(id):
    ids = adding_id(lst)
    for value in ids:
        if value['id'] == id:
            return render_template('post.html',posts=value)
    return 'Post not found'
    
    
    
if __name__ == '__main__':
    app.run(debug=True)
    
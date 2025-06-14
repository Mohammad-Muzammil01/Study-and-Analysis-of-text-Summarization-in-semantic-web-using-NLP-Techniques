from flask import Flask, render_template, request
from yt import generate_summary
import os
import tempfile

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    summary = None
    if request.method == 'POST':

        text = request.form.get('text')
        summary_size = request.form.get('summary_size', 'medium')
        

        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
            temp_file.write(text)
            temp_path = temp_file.name
        
        try:

            summary = generate_summary(temp_path, summary_size=summary_size)
            

            os.unlink(temp_path)
        except Exception as e:
            summary = f"Error generating summary: {str(e)}"
    
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True) 
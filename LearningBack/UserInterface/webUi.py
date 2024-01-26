from flask import Flask, render_template, request, send_file
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Handle file upload and processing
        input_file = request.files['input_file']
        output_file = process_files(input_file)

        # Return the processed file for download
        return send_file(output_file, as_attachment=True)

    return render_template("index.html")

def process_files(input_file):
    # Perform file processing here
    # Replace this with your own logic

    # Save the processed file
    output_file_path = 'output.txt'
    input_file.save(output_file_path)
    return output_file_path

if __name__ == '__main__':
    app.run(debug=True)

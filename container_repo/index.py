from flask import Flask, request, render_template, jsonify,send_file
import os
from werkzeug.utils import secure_filename
import subprocess

app = Flask(__name__)

# soffice= "C:\Program Files (x86)\LibreOffice\program\soffice.exe" 

@app.route("/", methods=["GET", "POST"])
def convert_func():
    if request.method == 'POST':
        global download_file_path,secure_name,output_directory
        input_file = request.files['fileName']
        if input_file.filename[-4:].lower() == "docx":

            input_file.save(os.path.join(
                "input", secure_filename(input_file.filename)))
            secure_name = secure_filename(input_file.filename)
            output_directory=os.path.relpath("output/")
            download_file_path=os.path.relpath(f'output/{secure_name.replace("docx","pdf")}')
            try:
                subprocess.call(['soffice',
                                 '--headless',
                                 '--convert-to',
                                 'pdf',
                                 '--outdir',
                                 output_directory,
                                 f"input/{secure_name}"],timeout=120)
                os.remove(f"input/{secure_name}")

                return jsonify({
                "Parameters": [
                    {
                        "Name": "File",
                        "fileValue":
                        {"Name": secure_name}
                    },
                    {
                        "storageName": f"{secure_name[:-5]}.pdf",
                        "httpStatus": 200
                    }
                ]
            }),{"Refresh": "3; url=/downloadFile"}
            except subprocess.TimeoutExpired:
                return jsonify({"message": "Timeout when converting file to PDF"})
            except Exception as error:
                return jsonify({"message": str(error)})   
        elif input_file.filename == "":
            return jsonify({"message": "No file uploaded"})
        else:
            return jsonify({"message": "Unsupported file type"})

    return render_template("button.html")


@app.route("/downloadFile")
def re_direct():
    return render_template("download.html")


@app.route('/download',methods=["GET"])
def download():
    if request.method=='GET':
        # some functionality can be added here to automatically delete the files which are older than one day (or) on clean the entire folder based on folder size.
        return send_file(download_file_path,as_attachment=True)
        
if __name__ == "__main__":
    app.run(port=int(os.environ.get('PORT', 5000)),host="0.0.0.0")

from flask import *
app = Flask(__name__)


@app.route("/")
def hello():
    # return "<h1 style='color:blue'>yahooooooooooooo!!!!!!!!!!!!!!</h1>"
    return render_template('hello.html')


@app.route('/upload', methods=['POST'])
def upload():
    import json
    import io
    import os
    file = request.files['inputFile']
    file.save(file.name)
    Ffile = file.name
    with io.open(Ffile, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
    fileN = os.path.basename(Ffile)
    # print(fileN)
    # fileN2 = os.path.splitext(fileN)[0]
    # print(fileN2)

    file = open(fileN + '_Korean_only.txt', 'w+', encoding='utf-8-sig')

    for i in range(0, len(data["subtitles"]["paragraphs"])):
        # print(data["subtitles"]["paragraphs"][i]["lines"][0]["text"])
        file.write(data["subtitles"]["paragraphs"][i]["lines"][0]["text"] + '\n')
        try:
            file.write(data["subtitles"]["paragraphs"][i]["lines"][1]["text"] + '\n')
            # print(data["subtitles"]["paragraphs"][i]["lines"][1]["text"])
        except:
            pass

    f.close()
    file.close()

    return "<p>finish</p>"


if __name__ == "__main__":
    app.run(Debug=True)


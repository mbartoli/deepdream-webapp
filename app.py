from flask import Flask
import dream.py as dream
app = Flask(__name__)

@app.route("/")
def hello():
    img = np.float32(PIL.Image.open('sky1024px.jpg'))
    _ = dream.deepdream(net, img)


# The complexity of the details generated depends on which layer's activations we try to maximize. Higher layers produce complex features, while lower ones enhance edges and textures, giving the image an impressionist feeling:

# In[ ]:

    _ = dream.deepdream(net, img, end='inception_3b/5x5_reduce')
    return "Deepdream inside Docker!!"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')


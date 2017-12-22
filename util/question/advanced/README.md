mnist-images-loader
===================

### What
Two python scripts that will load the training and testing images from the [MNIST](http://yann.lecun.com/exdb/mnist/) data set. Uses Python 3.

### Usage
1. Clone this repository
    
    `$ git clone https://github.com/tarunbod/mnist-images-loader.git`

2. Install Python dependencies (if needed)

    `$ pip install numpy pillow`

3. Run the python script

    `$ ./generate-training-images.py`

    `$ ./generate-testing-images.py`

    This will create two folders: `training-images/` and `testing-images`. These folders will contain the actual images. The actual values represented by the images will be saved in a json file called `training-labels.json` and `testing-labels.json`. 

### License
MIT License




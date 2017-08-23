# digit-recognition

JSON in/out RESTful API for digit recognition.

The solution consists in wrapping a neural network [model found on Kaggle](https://www.kaggle.com/poonaml/deep-neural-network-keras-way) in an API.

#### Requirements
* Python 2.7

Install dependencies with:
* ```pip install -r requirements.py```

### Local usage
* Start server with ```python server.py```
* Send a request, for instance ```curl -XPOST -F "image=@/Users/skynet/800.png" -vv http://localhost:5000/recognize.json```

## Testing
* ```pip install -r requirements.py```
* ```pip install -r requirements_tests.py```
* ```python tests/tests.py```

## Deployment
* Standard Heroku deployment ```git push heroku master```

## Concepts
This is a problem of image recognition. **Deep learning** has been popularized by increasing significantly the results in this field. So we are going to make use of it.

* pyData ecosystem is a famous ecosystem for solving machine learning problems in **python**. Specifically for deep learning, python also has some famous libraries (tensorflow, pyTorch for instance). So I will develop the solution in python. Please note that python is NOT the language I am *most comfortable with*: I feel way more comfortable in ruby. Python is the best compromise I could do between architecture choices and comfort.
* I decide to use **keras** on top of **tensorflow**, because I've heard during the first interview that it's what you use.
* I decide to use **Flask** because it's a very lightweight Framework for python.
* Deploy to **Heroku**: because they have a free offer. Because of the limited resources of the free offer, it will have some negative implications. They are described in the following paragraph **trade-offs**.

Trade-offs:
* **Model architecture** -  I used a model that I found on [Kaggle](https://www.kaggle.com/poonaml/deep-neural-network-keras-way). This model does not contain a lot of layers and does not provide good results. A good model was not the main scope of this tech test, though.
* **Training set** - Training the model is long and this can obviously not be done during the request: it need to be preprocessed. At the end the model is trained when the web-server is starting on Heroku. Because of the server resources ([Memory](https://devcenter.heroku.com/articles/error-codes#r14-memory-quota-exceeded), and  [deployment timeout](https://devcenter.heroku.com/articles/error-codes#h10-app-crashed)), I could not use more than 5% of the MNIST dataset. My original idea was:
  1. train the model locally ;
  * serialize the model object  to a file (locally)
  * and upload the file to the server during the deployment.<br />

  It hasn't worked because:
  1. [cPickle raises an exception](https://stackoverflow.com/questions/35355657/python-multiprocessing-cpickle-picklingerror-cant-pickle-type-instancemetho) (and it is not recommended anyway);
  * dill also raises exception;
  * keras method for model serialization [ has an open bug](https://github.com/fchollet/keras/issues/6211) with this model.
* **Scalability** - The response time on a free Heroku solution is correct (0.1s). To scale we could increase the numbers of Heroku workers ; for [other hosting solutions](http://flask.pocoo.org/docs/0.12/deploying/), we should add an application server and optimize it, etc. It has not been done because I don't have a context for it. And as the UNIX philosophy resumes it "*Premature optimization is the root of all evil*" [Donald_Knuth, Professor Emeritus at Stanford University, winner of the 1974 Turing Award].
* **Production-readiness** - I added an exception logging to SEntry. From experience, it makes debugging great and fast. Heroku already provides some basic logging (```heroku logs```) and monitor tool. More advanced services can be installed with add-ons like *papertrail* (for logging) or *new relic* (for monitoring).

## About me
I haven't really worked on my online presence, but well:

1. [github profile](https://github.com/gobert)
  * specially [sem-marketing](https://github.com/gobert/data-science-notebooks/tree/master/sem-marketing), where I try to predict the outcome of a Search Engine Marketing (SEM) campaign.
2. [Resume](https://drive.google.com/file/d/0B1BAeQsIi6lgTGpSSGdwcGh2WTg/view?usp=sharing)

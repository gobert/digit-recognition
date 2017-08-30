Coding challenge - Machine Learning Engineer
============================================

Functional spec
---------------

Prototype the following project: **Digit recognition service**

###  Digit recognition service

Create a digit recognition service that predicts the label of an uploaded digit image.

Example PNGs for testing your service can be downloaded from here:
* [Digit images](https://s3.eu-central-1.amazonaws.com/smacc-public/digit_images.zip) (testing examples)


Technical spec
--------------

The service should provide a JSON in/out RESTful API.
Use the technology you are most comfortable working with, e.g.:

* Python
* JavaScript
* Ruby
* PHP
* Go
* C++
* Java

Feel free to use any web framework.

You can either use any pre-trained models or any training code you can find on the web.
Optionally, you can also send us your own training model including your validation results.

If you decide to train your own model you can download training samples from here:
* [MNIST DB](http://yann.lecun.com/exdb/mnist/) (Training samples)


Host it!
--------

When you’re done, host it somewhere (e.g. on Amazon EC2, Heroku, Google AppEngine, etc.).

Readme
------

Write your README as if it was for a production service. Include the following items:

* Description of the problem and solution.
* Trade-offs you might have made, anything you left out, or what you might do differently if you were to spend additional time on the project.
* Link to other code you're particularly proud of.
* Link to your resume or public profile.
* Link to to the hosted application where applicable.

How we review
-------------

Your application will be reviewed by at least two of our engineers. We do take into consideration your experience level.

**We value quality over feature-completeness**. It is fine to leave things aside provided you call them out in your project's README. The goal of this code sample is to help us identify what you consider production-ready code. You should consider this code ready for final review with your colleague, i.e. this would be the last step before deploying to production.

The aspects of your code we will assess include:

* **Clarity**: does the README clearly and concisely explains the problem and solution? Are technical tradeoffs explained?
* **Correctness**: does the application do what was asked? If there is anything missing, does the README explain why it is missing?
* **Code quality**: is the code simple, easy to understand, and maintainable?  Are there any code smells or other red flags? Is the coding style consistent with the language's guidelines? Is it consistent throughout the codebase?
* **Testing**: how thorough are the automated tests? Will they be difficult to change if the requirements of the application were to change? Are there some unit and some integration tests?
	* We're not looking for full coverage (given time constraint) but just trying to get a feel for your testing skills.
* **Technical choices**: do choices of libraries, databases, architecture etc. seem appropriate for the chosen application?

Bonus point (those items are optional):

* **Scalability**: will technical choices scale well? If not, is there a discussion of those choices in the README?
* **Production-readiness**: does the code include monitoring? logging? proper error handling?
* **Model-performance and description**: if you decide to train your own model we'd like to hear from you about a brief summary of your methodology, the model architecture you picked and the resulting model's performance   

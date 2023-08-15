### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  
  While many of the same things can be accomplished in Python and Javascript, there are many differences especially in the syntax of how each language is written. Python more closely resembles English with keywords like "is" and "not" compared to JS's "!=" and "=". Additionally JS is camel cased while Python is snakecased. Overall, Python is primarily back-end and JS is both back and front end. 

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

    Using setdefault() or  get('key', 'val')

- What is a unit test?

  A testing program for part of an app.

- What is an integration test?

  A test to see how pieces of an app work together.

- What is the role of web application framework, like Flask?

  Flask is used to run th server and can also be used to debug. 

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  You can choose which option to use based on whether or not these routes are unchanging. Query params are better for search engines, but hard coding routes is better for directories. 

- How do you collect data from a URL placeholder parameter using Flask?

  Using <name> placeholders in the URL and accepting the corresponding <name> arguments in the view function. 

- How do you collect data from the query string using Flask?

  Accessing the query_string property of the request.

- How do you collect data from the body of the request using Flask?

  Using the request method, i.e. request.form, request.data, etc.

- What is a cookie and what kinds of things are they commonly used for?

  Cookies are used to store information in a browser for a specific user. Often used for things like browsing preferences or user information. 

- What is the session object in Flask?

  The session object is similar to cookies and dictionaries, but is used with a secret key to store values. 

- What does Flask's `jsonify()` do?

  Converts JSON (Javascript Object Notation) into a response object. 

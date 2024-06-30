from werkzeug.exceptions import HTTPException
from flask import jsonify
from __main__ import app



#werkzug http exception method in a function validation 

@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({'error': e.description}), e.code
    return jsonify({'error': str(e)}), 500
    
    
    
## a format function that response depends on the problem inside the data /error/messege provided
def format_response(data=None, error=None, message=None):
    response = {}
    if data is not None:
        response['data'] = data
    if error is not None:
        response['error'] = error
    if message is not None:
        response['message'] = message
    return jsonify(response)
    
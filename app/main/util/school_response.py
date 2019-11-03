"""this is for handling responses"""
from flask import json, Response
from http.client import responses
from logging import getLogger, StreamHandler, Formatter, INFO

def custom_response(res):
    return Response(
        mimetype="application/json",
        response=json.dumps(res),
    )


def dictionary_response(status_code, message):

    try:
        if status_code == 200 or status_code == 201:
            dictionary_response = {
                "applicationCode": 0, "code": status_code, "message": message, "status": responses[status_code],
            }
        else:
            dictionary_response = {
                "applicationCode": 1, "code": status_code, "message": message, "status": responses[status_code],
            }

        return dictionary_response

    except KeyError:
        dictionary_response = {
            "applicationCode": 1, "code": status_code, "message": message, "status": "Code is invalid",
        }
        return dictionary_response

    except:
        dictionary_response = {
            "applicationCode": 1, "code": 424, "message": message, "status": responses[424],
        }
        return dictionary_response


def overall_response(code, msg):

    out = dictionary_response(code, msg)
    return custom_response(out)


def custom_log(name):
    logger = getLogger(name)
    logger.propagate = False

    # Created handler object
    handler = StreamHandler()
    formatter = Formatter('%(asctime)s - SchoolAPI -  %(name)-8s  %(levelname)-s: %(message)s',
                          '%Y-%m-%d %H:%M:%S:%MS')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(INFO)
    return logger


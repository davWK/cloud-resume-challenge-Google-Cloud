#!/usr/bin/env python3

import functions_framework
from flask import jsonify
from google.cloud import firestore

PROJECT='alilikpo-228'
VISITORS_COLLECTION=u'cloud-resume-challenge' # que veut dire le u
COUNTER_DOCUMENT=u'visitors-count'


def getCount():
    db = firestore.Client(project=PROJECT)
    visitors_ref = db.collection(VISITORS_COLLECTION)
    counter_doc = visitors_ref.document(COUNTER_DOCUMENT)
    count_data = counter_doc.get()
    count = count_data.to_dict()['count']
    return count


def saveCount(count):
    db = firestore.Client(project=PROJECT)
    visitors_ref = db.collection(VISITORS_COLLECTION)
    counter_doc = visitors_ref.document(COUNTER_DOCUMENT)
    counter_doc.set({
        u'count': count
    })
    return count


@functions_framework.http
def get_visitor_number(request):

    if request.method == "GET" or request.method ==  "POST":
        count = getCount() + 1
        saveCount(count)
        response =  jsonify({'count': count})
        response.headers.set('Access-Control-Allow-Origin', '*')
        response.headers.set('Access-Control-Allow-Methods', 'GET, POST')
        return response


    else:
        return "Method not allowed ", 401

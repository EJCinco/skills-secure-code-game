# Welcome to Secure Code Game Season-1/Level-3!

# You know how to play by now, good luck!

import os
from flask import Flask, request

app = Flask(__name__)
@app.route("/")
def source():
    TaxPayer('foo', 'bar').get_tax_form_attachment(request.args["input"])
    TaxPayer('foo', 'bar').get_prof_picture(request.args["input"])

class TaxPayer:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.prof_picture = None
        self.tax_form_attachment = None


    def _safe_path(self, path):
        base_dir = os.path.abspath(os.path.dirname(__file__))  
        filepath = os.path.abspath(os.path.normpath(os.path.join(base_dir, path)))

        if not filepath.startswith(base_dir + os.sep):
            return None
        return filepath

    def get_prof_picture(self, path=None):
        if not path:
            return None

        prof_picture_path = self._safe_path(path)
        if not prof_picture_path:
            return None

        try:
            with open(prof_picture_path, 'rb') as pic:
                picture = bytearray(pic.read())

            return prof_picture_path
        except Exception:
            return None

    def get_tax_form_attachment(self, path=None):
        if not path:
            return None

        tax_form_path = self._safe_path(path)
        if not tax_form_path:
            return None

        try:
            with open(tax_form_path, 'rb') as form:
                tax_data = bytearray(form.read())

            return tax_form_path
        except Exception:
            return None



import re
from flask import Flask
from flask import request
from flask_cors import CORS
import logging
from transformers import AutoTokenizer, AutoModelWithLMHead, pipeline, GPT2Tokenizer
import os
import sys

if "MODEL" not in os.environ:
    print("Please set the environment variable MODEL")
    sys.exit(1)

app = Flask(__name__)
cors = CORS(app)

tokenizer = AutoTokenizer.from_pretrained(os.environ["MODEL"])
model = AutoModelWithLMHead.from_pretrained(os.environ["MODEL"])

text_generator = pipeline('text-generation', model=model, tokenizer=tokenizer)


@app.route('/generate', methods = ["POST"])
def generate():
    prompt = request.form["prompt"]
    output = text_generator(
        prompt,
        do_sample=True,
        max_length=50,
        top_k=50,
        top_p=0.95,
        num_return_sequences=1
    )[0]["generated_text"]

    output = output.split("\n")[0]

    app.logger.info("prompt:%s  output:%s" % (prompt, output))
    return output

if __name__ == "__main__":
    app.run(host="0.0.0.0")
else:
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
from flask import Flask, render_template,request,url_for, jsonify
from flask_bootstrap import Bootstrap 

# NLP Packages
from textblob import TextBlob,Word 
import random 
import time

app = Flask(__name__)
Bootstrap(app)


@app.route('/analyse',methods=['POST'])
def analyse():
	start = time.time()
	if not request.json or not 'rawtext' in request.json:
		abort(400)
	rawtext = request.json['rawtext']
	#NLP Stuff
	blob = TextBlob(rawtext)
	received_text2 = blob
	blob_sentiment,blob_subjectivity = blob.sentiment.polarity ,blob.sentiment.subjectivity
	number_of_tokens = len(list(blob.words))
	# Extracting Main Points
	nouns = list()
	final_word = list()
	for word, tag in blob.tags:
	    if tag == 'NN':
	        nouns.append(word.lemmatize())
	        len_of_words = len(nouns)
	        rand_words = random.sample(nouns,len(nouns))
	        for item in rand_words:
	        	word = Word(item).pluralize()
	        	final_word.append(word)
	summary = final_word
	end = time.time()
	final_time = end-start
	response = {
		"received_text" : str(received_text2), 
		"number_of_tokens" : str(number_of_tokens),
		"blob_sentiment" : str(blob_sentiment),
		"blob_subjectivity" : str(blob_subjectivity),
		"summary" : str(summary),
		"final_time" : str(final_time)
	}

	return jsonify(response), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000, debug=True)
from nose.tools import * 
from ex49 import lexicon2
from ex49 import parser
from ex49.parser import Sentence

def test_peek():
	word_list = lexicon2.scan('princess') #We need to compare this to the outcome of parser.peek
	assert_equal(parser.peek(word_list), 'noun')

def test_match():
	word_list = lexicon2.scan('princess')
	assert_equal(parser.match(word_list, 'noun'), ('noun', 'princess'))
	assert_equal(parser.match(None, 'noun'), None)
	assert_equal(parser.match(word_list, 'stop'), None)

def test_skip():
	word_list = lexicon2.scan('princess')
	assert_equal(word_list, [('noun', 'princess')])
	parser.skip(word_list, 'noun')

def test_parse_verb():
	word_list = lexicon2.scan('kill the')
	parser.parse_verb([('verb', 'kill'), ('stop', 'the')])
	assert_equal(parser.parse_verb(word_list), ('verb', 'kill'))
	word_list = lexicon2.scan('north')
	assert_raises(parser.ParserError, parser.parse_verb, word_list)

def test_parse_object():
	word_list = lexicon2.scan('princess')
	word_list2 = lexicon2.scan('north')
	word_list3 = lexicon2.scan('the it')
	parser.parse_object([('noun', 'princess'), ('direction', 'north')])
	assert_equal(parser.parse_object(word_list), ('noun', 'princess'))
	assert_equal(parser.parse_object(word_list2), ('direction', 'north'))
	assert_raises(parser.ParserError, parser.parse_object, word_list3)

def test_parse_subject():
	word_list = [('verb', 'kill'), ('direction', 'north')]
	subj = ('noun', 'princess')
	verb = ('verb', 'kill')
	obj = ('direction', 'north')
	obj_sent = Sentence(subj, verb, obj) #This is the first instance of Sentence()
	assert_equal(parser.parse_subject(word_list, subj), obj_sent)
	#this is the second instance of Sentence() that I need to compare to the first one.

def test_parse_sentence():
	word_list = lexicon2.scan('kill north the')
	subj = ('noun', 'player')
	verb = ('verb', 'kill')
	obj = ('direction', 'north')
	obj_sent = Sentence(subj, verb, obj)
	assert_equal(parser.parse_sentence(word_list), obj_sent)
	assert_raises(parser.ParserError, parser.parse_sentence, word_list)

def test_sentence():
	subject = ('noun', 'player')
	verb = ('verb', 'kill')
	obj = ('direction', 'north')
	sent = Sentence()
	compare = Sentence(subject, verb, obj)
	assert_equal(parser.Sentence(subject, verb, obj), compare)
	assert_equal(sent.subject, (subject[1])
	



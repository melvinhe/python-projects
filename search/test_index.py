import pytest
from index import Indexer

# Here's an example test case to make sure your tests are working
# Remember that all test functions must start with "test"
def test_example():
    assert 2 == 1 + 1


def file_as_set(filename):
    """
    Returns all of the non-empty lines in the file, as strings in a set.
    """
    line_set = set()
    with open(filename, "r") as file:
        line = file.readline()
        while line and len(line.strip()) > 0:
            line_set.add(line.strip())
            line = file.readline()
    return line_set

def test_file_contents():
    simple_index = Indexer("wikis/SimpleWiki.xml", "simple_titles.txt",
       "simple_docs.txt", "simple_words.txt")
    simple_index.run() # run the indexer to write to the files
    titles_contents = file_as_set("simple_titles.txt")
    assert len(titles_contents) == 2
    assert "200::Example page" in titles_contents
    assert "30::Page with links" in titles_contents


def test_process_document():
    test_document = Indexer("test.xml", "test.txt",
       "test.txt", "test.txt")

    test_title = "Vexillology"
    test_id = 420
    test_body = "Vexillology decodes flag symbolism with meticulous scrutiny."
    processed = test_document.process_document(test_title, test_id, test_body)
    assert processed == ["vexillolog", "vexillolog", "decod", "flag", "symbol", "meticul", "scrutini"]

def test_process_document_simple():
    test_document = Indexer("test.xml", "test.txt",
       "test.txt", "test.txt")
    test_title = "easy"
    test_id = 0
    test_body = "Easy peasy lemon squeezy!"
    processed = test_document.process_document(test_title, test_id, test_body)
    assert processed == ["easi", "easi", "peasi", "lemon", "squeezi"]

def test_process_document_empty():
    test_document = Indexer("test.xml", "test.txt",
       "test.txt", "test.txt")
    test_title = "empty"
    test_id = 0
    test_body = ""
    processed = test_document.process_document(test_title, test_id, test_body)
    assert processed == ["empti"]

def test_process_document_sentence():
    test_document = Indexer("test.xml", "test.txt",
       "test.txt", "test.txt")
    test_title = "sentence"
    test_id = 0
    test_body = "This is a sentence. This is the an not the the they isn't sentence."
    processed = test_document.process_document(test_title, test_id, test_body)
    assert processed == ["sentenc", "sentenc", "sentenc"]

#def test_parse_contents():
    #test_parse = Indexer("ExampleWiki.xml", "titles.txt", "docs.txt", "words.txt")
    #test_parse.run()
    #titles_contents = file_as_set("simple_titles.txt")
    #assert len(titles_contents) == 2
    #assert "200::Example page" in titles_contents
    #assert "30::Page with links" in titles_contents

    #test_parse.process_docume

def test_compute_tf():
    test_tf = Indexer("wikis/test_tf_idf.xml", "titles.txt",
       "docs.txt", "words.txt")
    test_tf.parse()
    assert test_tf.compute_tf() == {'zarf': {0: 1.0, 2: 0.5}, 'histor': {0: 0.5}, 'holder': {0: 0.5}, 'sleev': {0: 0.5, 2: 1.0}, 'use': {0: 0.5}, 'insul': {0: 0.5}, 'hot': {0: 0.5}, 'beverag': {0: 0.5}, 'cup': {0: 0.5, 2: 1.0}, '19th': {0: 0.5}, 'centuri': {0: 0.5}, 'refer': {0: 0.5}, '[[cup sleeve]]': {0: 0.5}, '[[tableware]]': {0: 0.5, 2: 0.5}, '[[beverage history|(https://us.coca-cola.com/)]]': {0: 0.5}, 'tablewar': {1: 0.2}, 'tabl': {1: 1.0}, 'see': {2: 1.0}, '[[zarf]]': {2: 0.5}, 'also': {2: 0.5}}
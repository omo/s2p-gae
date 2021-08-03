
import main

def _assert_redirect(get, url):
  main.app.testing = True
  client = main.app.test_client()
  resp = client.get(get)
  assert resp.status_code == 301
  assert resp.headers['Location'] == url


def test_index():
  _assert_redirect('/', 'https://anemone.dodgson.org/') 

def test_unknown():
  _assert_redirect('/hoge', 'https://anemone.dodgson.org/') 

def test_tdiary():
  _assert_redirect('/?date=20110417', 'https://bn.dodgson.org/bn/2011/04/17/') 

def test_tdiary_older():
  _assert_redirect('/omo/t/?date=20080316', 'https://bn.dodgson.org/bn/2008/03/16/') 

def test_tdiary_broken():
  _assert_redirect('/omo/t/?date=2008031', 'https://anemone.dodgson.org/') 

def test_octopress():
  _assert_redirect('/b/2014/12/11/why-is-real-dom-slow/', 'https://blog.dodgson.org/b/2014/12/11/why-is-real-dom-slow/') 

def test_octopress_pages():
  _assert_redirect('/blog/archives/', 'https://blog.dodgson.org/blog/archives/') 

def test_feed():
  _assert_redirect('/atom.xml', 'https://anemone.dodgson.org/index.xml')

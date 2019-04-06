
import flask
import re

from flask import Flask

app = Flask(__name__)


def _redirect_to_fallback():
  return flask.redirect('https://anemone.dodgson.org/')


@app.route('/<path:path>')
def  all(path):
  # All the relevant URL is (shold be able to) categorized solely based on the path part.
  # You don't have to look at the host name.

  # Handle tDiary-like, e.g: http://stepped.dodgson.org/?date=20110417
  #                          http://www.dodgson.org/omo/t/?date=20080316
  date_param = flask.request.args.get('date', None)
  if date_param:
      match = re.match('(\d\d\d\d)(\d\d)(\d\d)', date_param)
      if not match:
        return _redirect_to_fallback()
      yyyy, mm, dd = match.group(1, 2, 3)
      return flask.redirect('https://bn.dodgson.org/bn/{}/{}/{}/'.format(yyyy, mm, dd))

  # Handle /bn/... e.g: http://steps.dodgson.org/bn/2007/11/03/
  if flask.request.path.startswith('/bn/'):
    return flask.redirect('https://bn.dodgson.org' + flask.request.path)

  # Handle /b/... e.g: http://steps.dodgson.org/b/2014/12/11/why-is-real-dom-slow/
  if flask.request.path.startswith('/b/') or \
     flask.request.path == '/blog/archives/' or \
     flask.request.path == '/selection/':
    return flask.redirect('https://blog.dodgson.org' + flask.request.path)

  # No clue what this is.
  return _redirect_to_fallback()


@app.route('/')
def  index():
  return all('/')


@app.route('/favicon.ico')
def  favicon():
  flask.abort(404)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
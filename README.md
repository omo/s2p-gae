

## Prereq

 * [Pyenv](https://github.com/pyenv/pyenv)
 * [GCloud SDK](https://cloud.google.com/sdk/docs/)

## Setup

```
$ conda deacitvate # As needed
$ pyenv rehash
# $ pyenv virtualenv venv-s2p-gae
$ pyenv activate venv-s2p-gae
$ pip install -r requirements.txt
```

## Test

```
$ pip install pytest
$ pytest
```

## Run locally

```
$ python main.py
```

## Deploy

```
$ gcloud app deploy
```

## Browse

 * https://s2p-gae.appspot.com

## Relevant Links

 * https://github.com/pyenv/pyenv/blob/master/COMMANDS.md
 * https://github.com/pyenv/pyenv-virtualenv

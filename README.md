Junction | https://hackit.galepartners.com/
========


**Version**: 0.3.2

Junction is a software to manage proposals, reviews, schedule, feedback during conference.

Setup
=====

It is advised to install all the requirements inside [virtualenv], use [virtualenvwrapper] to manage virtualenvs.

[virtualenv]: https://virtualenv.pypa.io/en/latest/
[virtualenvwrapper]: https://virtualenvwrapper.readthedocs.org/en/latest/

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install libpq-dev python-dev build-essential tcl
pip install -r requirements-dev.txt
cp settings/dev.py.sample settings/dev.py
python manage.py migrate --noinput
python manage.py sample_data
sudo apt-get -y install redis-server
```

Initial auth data: admin/123123

If docker and docker-compose are not installed already (Not mandatory):
--------------------------------------------
Refer to (http://docs.docker.com/installation/) for detailed installation instructions.

```
curl -sSL https://get.docker.com/ | sudo sh
sudo pip install docker-compose
```

Create aliases for docker and docker-compose to avoid running them with sudo everytime.
Append the following lines to your ~/.bashrc or ~/.zshrc

```
alias docker='sudo docker'
alias docker-compose='sudo docker-compose'
```

Finally, run
```
docker-compose up
```


Configuring Django-allauth
---------------------------

 - Go to `http://localhost:8000/nimda/sites/site/`
 - Change the default site's(the one with ID = 1) name and display to `localhost:8000`
 - Go to `Social Applications` in admin panel and add [Github](http://django-allauth.readthedocs.org/en/latest/providers.html#github) and [Google](http://django-allauth.readthedocs.org/en/latest/providers.html#google)'s auth details

Making Frontend Changes
---------------------------
Make sure you have nodejs, npm, bower, grunt-cli & grunt installed

```
$ cd junction/static
$ npm install
$ bower install
$ grunt // This starts a watcher to watch for file changes
```


Contributing
------------

1. Choose an [issue][issue-list] and ask any doubts in the issue thread.
2. Report any bugs/feature request as Github [new issue][new-issue], if it's already not present.
3. If you are starting to work on an issue, please leave a comment saying "I am working on it".
4. Once you are done with feature/bug fix, send a pull request according to the [guidelines].

[issue-list]: https://github.com/pythonindia/junction/issues/
[new-issue]: https://github.com/pythonindia/junction/issues/new
[guidelines]: https://github.com/pythonindia/junction/blob/master/CONTRIBUTING.md

### API

- HTTP API documentation is [here](https://github.com/pythonindia/junction/blob/master/docs/api.md).
- Python Client for junction is [here](https://github.com/pythonindia/junction-client).


License
-------

This software is licensed under The MIT License(MIT). See the [LICENSE][LICENSE] file in the top distribution directory for the full license text.

[LICENSE]: https://github.com/pythonindia/junction/blob/master/LICENSE

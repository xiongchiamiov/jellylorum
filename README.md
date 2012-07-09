This is an anime information mashup, pulling from [AniDB], [A-P] and [ANN].

[AniDB]: http://anidb.net
[A-P]: http://anime-planet.com
[ANN]: http://animenewsnetwork.com

# Requirements #

* [virtualenv]

[virtualenv]: http://pypi.python.org/pypi/virtualenv

# Installing #

Since we're using virtualenv, everything's nice and easy.

	$> cd jellylorum
	$> virtualenv --no-site-packages env
	$> source env/bin/activate
	$> pip install -r requirements.txt
	$> ./manage.py syncdb
	$> ./manage.py migrate
	$> ./manage.py loaddata anime/initial_data.json


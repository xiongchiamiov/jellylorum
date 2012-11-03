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
	$> virtualenv --distribute --no-site-packages env
	$> source env/bin/activate
	$> pip install -r requirements.txt
	$> ./manage.py syncdb
	$> ./manage.py migrate
	$> ./manage.py loaddata anime/initial_data.json

# Creating a Migration #

Since I always forget.

	$> ./manage.py schemamigration --auto anime
	$> ./manage.py migrate
	$> ./manage.py dumpdata anime --indent=4 > anime/initial_data.json

# TODO #

* Grab more information from sources.
  * ~~AniDB~~
  * A-P
  * ANN
* Add searching.
* Refetch when data's too stale.
* And update via AJAX.
* Figure out how we're going to get the database populated.
* User accounts for customization?


Jellylorum is an anime information mashup, pulling from [AniDB], [A-P] and [ANN].

Looking up information about an anime is a PITA.  When looking at a Hollywood
movie, the only place you have to go is IMDB - or maybe Wikipedia for some
extra information.  Information on anime, however, is spread out on multiple
sites:

* **AniDB** is the go-to source for release group information - who's subbing
  the show and how well they're doing it.  It's also my favorite place to see a
  quick'n'dirty summary of a show, since the user-generated tags display all
  the tropes the show exhibits, and most anime isn't inventive enough to be
  more than a compilation of tropes.
* **Anime-Planet** has, hands-down, the best show recommendations.  It also
  tends to have excellent user and staff reviews due to [Sothis]' fanaticism
  for high quality writing.
* **Anime News Network** is the IMDB of anime - if you want to know who voiced
  who (in more than just the original Japanese), ANN is the place to go.

A notable exclusion is [MyAnimeList][MAL], which is an inferior version of A-P.
MAL will never be supported in Jellylorum.  No, I don't have any strong
feelings about this.

In order to get a full view of an anime (and to track which files you possess /
have watched), you have to visit all three of these sites.  This is annoying.
Enter Jellylorum, the engine behind [Ani.PE(dia)].

Be aware that Jellylorum is not designed to be a replacement for any of its
source sites; as such, you will never be able to mark episodes as watched,
browse by category, etc.  Those are things the source sites do well, so there's
absolutely no reason for me to re-invent it.  Jellylorum is instead intended to
be the starting point for browsing to other sites, which is why there are
conveniently large links at the top of every anime page.

For more information on how Jellylorum is actually constructed, take a look at
[the docs](docs/).

[AniDB]: http://anidb.net
[A-P]: http://anime-planet.com
[ANN]: http://animenewsnetwork.com
[Sothis]: http://www.anime-planet.com/users/sothis
[MAL]: http://myanimelist.net/
[Ani.PE(dia)]: http://ani.pe/dia/anime/

# Roadmap #

* ~~Grab information from sources.~~
  * ~~AniDB~~
  * ~~A-P~~
  * ~~ANN~~
* Get an initial data set.
  * ~~Pull a list of titles from AniDB.~~
  * Automagically create links to the other sources.
* Add searching using [Haystack](http://haystacksearch.org/).
* Refetch when data's too stale.
* And update via AJAX.
* Make the UI usable and not ugly.
* User accounts for customization?

# Requirements #

* A relatively recent version of Python 2.x.  I develop and deploy on 2.6.
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

# Running Tests #

All tests:

	$> ./manage.py test

A specific set of tests:

	$> ./manage.py test anime.tests:APTest


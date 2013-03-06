# The Basics #

Jellylorum is written in Python, using the Django framework.  I think Python is
a language excellently-oriented towards maintainability, and that Django
follows well in those footsteps (and has, hands-down, the best documentation
I've ever seen), but really, like most technical decisions, it comes down to
personal preference - I like Python and thus want to use it for things, and
I've used Django and liked it and thus decided to continue using it for
projects.

Similarly, there is no attempt to make sure this project works on Windows,
because I have no intention of ever hurting myself by attempting to use Windows
as a web server.  I know a great many people do, but they're not me, and
they're not writing this.  So there.

# Fetching Data #

## AniDB ##

**AniDB** is the easiest, because the wonderful folks behind it have made
[several APIs] available to the public.

[The UDP API] is a packet-based API, where the data in predetermined bytes of
the packet correlates to the information you want.  This is a pain.
Fortunately, this API is primarily needed for write operations, and, as stated
in the primary project README, Jellylorum will never support write operations
for its source sites.

*Unfortunately, we may end up needing to do some work with the UPD API to get
mappings between AniDB and ANN; see [this thread] for more information.*

Thankfully, the AniDB developers have also provided [an HTTP API] for read-only
operations.  Fetching and uncompressing the data is easily done using Python's
built-in `urllib2` and `gzip` modules.  [Python provides][etree] a core library
for parsing XML trees, but I chose to use the mostly-compatible [lxml.etree]
for its better performance and more Pythonic API.  From this point on, it's
mostly a matter of looking at the API documentation and pulling out the correct
fields.

[several APIs]: http://wiki.anidb.info/w/API
[The UDP API]: http://wiki.anidb.info/w/UDP_API_Definition
[this thread]: http://anidb.net/perl-bin/animedb.pl?show=cmt&id=45254
[an HTTP API]: http://wiki.anidb.info/w/HTTP_API_Definition
[etree]: http://docs.python.org/2/library/xml.etree.elementtree.html
[lxml.etree]: http://lxml.de/tutorial.html

## Anime-Planet ##

**Anime-Planet** (A-P) does *not* have an API; fortunately, programmers have
long been honing their skills at parsing strings, so we have a number of tools
available to us for screen-scraping.

[pyquery] is my library of choice - it provides a familiar API (a clone of
jQuery's), has reasonable documentation, and is actively maintained.  What more
can you ask for?

As much as possible, strict selectors are used when querying the scraped page's
DOM.  We are, of course, beholden to A-P's developers - if they change the
page's layout, we may need to change our backend.  For this reason, Jellylorum
has a test suite that covers several different types of anime for inconguities;
if we can't reduce the [MTBF], we can at least tackle [MTTR].

[pyquery]: https://pypi.python.org/pypi/pyquery
[MTBF]: http://en.wikipedia.org/wiki/MTBF
[MTTR]: https://en.wikipedia.org/wiki/Mean_time_to_recovery

## Anime News Network ##

**Anime News Network** (ANN) is handled pretty much like A-P.  Scrape, parse,
save.


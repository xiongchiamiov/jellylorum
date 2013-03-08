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

# Overview #

There are two primary operations in Jellylorum: data gathering and data
display.  They are intentionally kept separate because similar sites that start
off with them mixed, like [Reddit Investigator], have serious performance issues
(read: they take multiple minutes to return data to the user).

[Reddit Investigator]: http://www.redditinvestigator.com/

# Data Gathering #

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

One downside of having tests that cover a variety of cases is high maintenance -
some test suites have to cover currently-airing shows, and those will air more
episodes (and finish airing!) on a regular basis.  For the time being, at least,
I've accepted this as a necessary price for development security; in the future,
they may end up commented out, for fear of [PHP syndrom].

[pyquery]: https://pypi.python.org/pypi/pyquery
[MTBF]: http://en.wikipedia.org/wiki/MTBF
[MTTR]: https://en.wikipedia.org/wiki/Mean_time_to_recovery
[PHP syndrom]: http://gcov.php.net/viewer.php?version=PHP_5_4&func=tests

## Anime News Network ##

**Anime News Network** (ANN) is handled pretty much like A-P.  Scrape, parse,
save.

## Tying them all together ##

This is perhaps the most interesting part of the project.

[AniDB makes][title dump] a data-dump of their entire list of anime titles, every day.  This provides a fantastic starting point.

AniDB maintains a set of links between their entries and ANN's; unfortunately,
this is currently only available via the UDP API (see above).  This data is
curated by their detail-obsessed userbase (I have more edits to my credit than
I wish to make public), which is likely more accurate than any algorithm we
can determine.

AniDB *used* to also have user-facing links to the corresponding A-P pages; however, some... drama prompted them to remove these.  They still have some data available via the UDP API, but it's old and severely out-of-date, enough that we shouldn't use it at all.

Neither of the other sites provides links between their content and the other site's, or any other sites', for that matter.

There are, generically, two methods for gaining the required data - algorithmically  and human-generated.

[title dump]: http://wiki.anidb.info/w/API#Anime_Titles

### Human-generated ###

We certainly want to give users the ability to add links; any algorithmic solution will be imperfect, and users will gladly spend a small amount of their time fixing issues that directly affect them.

An almost entirely blank database is a terrible thing to greet users with on a launch, however, so we cannot rely entirely upon user volunteerism.

One option I've considered is paying [Amazon Turk] users a small fee to produce the initial set of linkings.  I'm not sure I wish to front enough money for a decent set, and more importantly, I'm attempting to get senior project credit for this, and I apparently did not spend five years in school to learn how to pay other people to do my work for me.

[Amazon Turk]: https://www.mturk.com/mturk/welcome

### Algorithmically ###

A-P's search returns a 302 redirect if only one result is found, but displays a list of results otherwise.  We can perhaps leverage the information gathered from the other two sources to fill in enough fields in the advanced search parameters to get an acceptably-high single-response rate.

# Data Display #

## Finding the data you want ##

Currently, [the main anime page] displays a list of all the anime we know about;
clicking on one will lead you to the detail page.

Future plans include using [Haystack] to generate search results.

[the main anime page]: http://ani.pe/dia/anime/
[Haystack]: http://haystacksearch.org/

## Displaying details ##

Right now, Jellylorum just spits a bunch of cached data out onto the screen.
This is both ugly and almost entirely unhelpful.

In the future, if the data we have stored is determined to be too stale (say, 1 day
since it's been updated), the old data will still be sent to the client for direct
consumption.  A background job will be queued to update the data, and if any changes
are present, we'll push them in via AJAX.

I'd like to give users some amount of customization as to what data is available on
the page.  This requires user accounts, a backend for saving preferred views, the
front-end logic for implementing it, and some way of changing your preferences,
either in control panel form or edit controls directly on the view page.  This idea
is not fully formed yet; the description here is deliberately vague pending designer
consultation and usability prototyping.

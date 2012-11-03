#!/bin/sh -ex

./manage.py shell <<<"from anime.models import *
#knt = AniDB.objects.get(pk=6466)
knt = AP.objects.get(pk=1)
knt.update()
knt.save()"
./manage.py dumpdata anime --indent=4 > anime/initial_data.json
git diff anime/initial_data.json


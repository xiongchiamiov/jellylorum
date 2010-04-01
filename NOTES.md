# Queue

[delayed_job] comes highly recommended. It uses Redis, though, and I'd rather
not run a second database just for that.

collectiveidea's [fork] includes support for mongodb (MongoMapper,
specifically), as well as a few other things.

A very new project (at the time of this writing, only 3 days old) is
[mongo_queue], which has the advantage of being fairly simple (and I don't need
anything complicated at this current time).

[delayed_job]: http://github.com/tobi/delayed_job
[fork]: http://github.com/collectiveidea/delayed_job
[mongo_queue]: http://github.com/Skiz/mongo_queue

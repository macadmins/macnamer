macadmins-macnamer
==================

This Docker image runs [Macnamer](https://github.com/grahamgilbert/macnamer).

# Settings

Several options, such as the timezone and admin password are customizable using environment variables.

* ``ADMIN_PASS``: The default admin's password. This is only set if there are no other superusers, so if you choose your own admin username and password later on, this won't be created.
* ``DOCKER_MACNAMER_TZ``: The desired [timezone](http://en.wikipedia.org/wiki/List_of_tz_database_time_zones). Defaults to ``Europe/London``.
* ``DOCKER_MACNAMER_ADMINS``: The admin user's details. Defaults to ``Docker User, docker@localhost``.

If you require more advanced settings, for example if you want to hide certain plugins from certain Business Units or if you have a plugin that needs settings, you can override ``settings.py`` with your own. A good starting place can be found on this image's [Github repository](https://github.com/grahamgilbert/macadmins-macnamer/blob/master/settings.py). To use your own ``settings.py`` file, use the ``-v`` option:

`` -v /usr/local/macnamer_data/settings/settings.py:/home/app/macnamer/macnamer/settings.py``

# Database

The directory the SQLite database lives (``/home/app/macnamer/db``) in is exposed. To persist your database, you should run your container with ``-v /host/path/somewhere/db:/home/app/macnamer/db``.

#Running the Macnamer Container

```bash
$ docker run -d --name="macnamer" \
  -p 80:8000 \
  -v /usr/local/macnamer_data/db:/home/app/macnamer/db \
  -e ADMIN_PASS=pass \
  macadmins/macnamer
```

#TODO

* Add support for Postgres and MySQL


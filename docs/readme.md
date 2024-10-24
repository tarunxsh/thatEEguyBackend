# [Heroku setup](https://devcenter.heroku.com/articles/django-assets) : 

## Static Files
1. Django won’t automatically create the target directory (STATIC_ROOT) that collectstatic uses, if it isn’t available
2. You may need to create this directory in your codebase, so it will be available when collectstatic is run.
3. Git does not support empty file directories, so you will have to create a file inside that directory as well.

## [Whitenoise](http://whitenoise.evans.io/en/stable/)
Django does not support serving static files in production. However, the fantastic WhiteNoise project can integrate into your Django application, and was designed with exactly this purpose in mind.

[medium reference](https://medium.com/@vonkunesnewton/understanding-static-files-in-django-heroku-1b8d2f003977)
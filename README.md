# ImageMobile

## Python Dependencies
* Django
* djangorestframework
* pytz
* opencv-python (3.4.2.16)
* opencv-contrib-python (3.4.2.16)
* sklearn
* pylablib
* Pillow

## Base URLs
* "/img_searches/": POST an image to analyse.
* "/img_searches/<int:ID>/": GET image analysis results.
* "/img_searches_DEL/<int:ID>/": Removes analysis results.
* "/listrefs/": GET infos about database.
* "/reindex/": GET regenerates images indexation infos.
* "/form_sendfile/": GET a html form to send an image to "/img_searches/".


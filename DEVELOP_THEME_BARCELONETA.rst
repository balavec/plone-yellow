Theme development
-----------------

In order to develop the theme you need to install grunt-cli global::

    $ sudo npm install -g grunt-cli

And then run `npm install` both in the package root and in the theme folder:

    $ npm install

    $ cd ./src/theme/bob/theme
    $ npm install


After executing these commands you can run grunt on the package root folder to watch for any less changes::

    $ grunt watch

This will make sure that the many .less files are compiled to .css on the fly and then served up from the theme.

You can also use this command to automaticly reload the browser after changes::

    $ grunt plone-bsync

It will run a Grunt browser sync task in a new browser window and will reload after every change of the less files in the less folder. If your Plone is not running on port 8080 you have to adjust the proxy option in the Gruntfile.js.

If you prefer to do a one time compile of the less files you can run::

    $ grunt compile


Note
----

- If you are make changes TTW, make sure that Development Mode is enabled by going to the `Site Setup` > `Resource Registries`
  and check the `Development Mode` checkbox, this ensures that your changes show up and aren't cached.
- this theme is using a Grunt setup to compile the resources. The grunt setup is outside of the theme folder in the package root. If you only have a Zip-file version of this theme, have a look at the example theme plonetheme.tango (github.com/collective) for the Gruntfile.js and package.json to setup your own Grunt above your theme folder.
- You can delete the "custom-theme-marker" in the index.html and in custom.less

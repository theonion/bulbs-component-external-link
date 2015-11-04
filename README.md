<strong><i>:exclamation: THIS REPO SHOULD NOT BE MADE PUBLIC :exclamation:</i></strong>

# bulbs-component-external-link
External link content type component for bulbs projects.

## Setup
Using this project requires setup and implementation of provided Django apps. The
site refers to the site that this component is being installed in.

### Python and Bower Dependencies
From the site using this component:

1. Add a dependency for this project in ```requirements.txt```, where ```<version>```
is the version to install:
  ```
  git+https://0469c955e10241b40fffe0225e29a3c238aadf69:x-oauth-basic@github.com/theonion/bulbs-component-external-link.git@<version>#egg=bulbs-component-external-link
  ```

1. Run ```pip install -r requirements.txt``` on requirements file in the correct
context to install this project's Django apps.

1. Install bower dependencies, where ```<version>``` is the version to
install which should match the ```<version>``` used in ```requirements.txt```:
  ```bash
  $ bower install --save https://0469c955e10241b40fffe0225e29a3c238aadf69:x-oauth-basic@github.com/theonion/bulbs-component-external-link.git\#\<version>
  ```

### Implementation
1. Create a external-link package in the site's app directory.
1. Add ```"bulbs_component_external_link"``` to ```INSTALLED_APPS``` in Django's settings file.
1. Add a ```models.py``` that implements ```bulbs_component_external_link.models.ExternalLinkMixin```.
1. Create a migration for your app with Django migrations as you would any other app.

#### Implementing CMS Resources
To use the CMS templates, scripts, and styles:

1. Include ```"bulbs_component_external_link_cms"``` in ```INSTALLED_APPS``` in
Django's settings file.

1. If using [django-pipeline](https://github.com/cyberdelia/django-pipeline) add the following to the Django settings file:
  ```python
  from bulbs_component_external_link import pipeline as external_link_pipeline
  
  ...
  
  external_link_pipeline.cms_js.update_pipeline(PIPELINE_JS)
  ```
  Where ```PIPELINE_JS``` is the current javascript pipeline dictionary.

1. Create a CMS page with the following html:
  ```html
  <external-link-edit article="content"></external-link-edit>
  ```
  Where ```content``` is an angular scope variable containing the content's data.

1. Add ```bulbs.externalLink``` as a dependency for your CMS's Angular app.

## django-bulbs-cms Package
```compat-builds/django-bulbs-cms``` should not be edited directly. This app exists only until
CMS files are completely migrated out of django. To make changes to this package,
edit files located in ```src/bulbs-cms``` then run ```grunt build_bulbs_cms_for_django```
to rebuild ```compat-builds/django-bulbs-cms``` with your changes.

Commit your changes and the rebuilt package, then reinstall the app on whatever
project(s) require the changes.

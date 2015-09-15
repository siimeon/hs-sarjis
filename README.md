# Comic parser

Comic parser is project for finding out latest daily comic from different websites.

Project start for checking out Fingerpori from [Helsigin Sanomat](http://www.hs.fi/fingerpori/) but has expanded
to work with all sites were data is readable out of html code

## Logic

Comic parser is writen with Python. Idea with comic parser is to parse attribute values from html pages for finding out
comic image url from html code. This logic works with many sites, but there may be sites that use dynamic structure that
comic parsers logic is not able to find comic urls.

All parsing logic is under comicParser folder

## Presentation

This project includes very simple AngularJS web app for displaying comics parsed with comic parser. Web app code can be
found under html folder
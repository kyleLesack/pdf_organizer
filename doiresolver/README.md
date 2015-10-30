Kyle's Notebook

# Notebook for my notes from journal articles and other academic research

## Planned Features:
* organize notes using the article doi
* use makefiles

How to create a .md file for an article:

echo <MYDOI> | sed -r 's/[:./[:space:]]+/_/g' | xargs -I file touch file.md

Some good stuff on makefiles for r projects (see comments as well):
http://robjhyndman.com/hyndsight/makefiles/
http://pirategrunt.com/2015/03/28/makefilesandrmarkdown/

Some stuff on knitr'ing from the cli:
http://stackoverflow.com/questions/10943695/what-is-the-knitr-equivalent-of-r-cmd-sweave-myfile-rnw

Some stuff on APIs:
http://labs.crossref.org/resolving-citations-we-dont-need-no-stinkin-parser/
http://www.crosscite.org/cn/

# Knitr citations
https://cran.r-project.org/web/packages/knitcitations/knitcitations.pdf

Idea for adding new journal article notes:
* Download bibtex file
* Run Makefile to create .md files in draft folder for each new bibtex
* If an existing .md file has been modified move to posts

Directory Structure
_assets --> location of pdf and bibtex files
_posts  --> location for content to be published, category tags will be used to separate journal article notes from topic reports

**Notes**
Link to pdfs using site root url ie: /_assets/MYFILE.pdf
Create indexes for each category of posts:
see: http://jekyllrb.com/docs/posts/


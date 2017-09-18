import requests
import json

requestURL = "https://gatech-primo.hosted.exlibrisgroup.com/primo_library/libweb/webservices/rest/primo-explore/v1/pnxs?addfields=vertitle,title,collection,creator,contributor,edition,subject,ispartof,description,relation,publisher,creationdate,format,language,identifier,lds05,default.fulldisplay.lds04,lds04,citation,source,lds02,versions,type,coverage,lds03,lds06,crsinfo&getMore=0&inst=01GALI_GIT&lang=en_US&limit=1000&mode=advanced&multiFacets=facet_tlevel,include,available|,|facet_domain,include,Science+Fiction+Collection|,|facet_rtype,include,book|,|facet_library,include,GTMAIN&offset=0&pcAvailability=true&q=sub,exact,Science+Fiction,AND;facet_lang,exact,eng,AND;facet_pfilter,exact,book,AND&qExclude=&qInclude=&rtaLinks=true&scope=default_scope&sort=rank&tab=default_tab&vid=01GALI_GIT"


"""
this bearer auth token will have to change for consecutive runs. to update it, visit the following url, open the networking tab, and find the updated bearer token in a request that used an 'Authorization' header:

https://gatech-primo.hosted.exlibrisgroup.com/primo-explore/search?query=sub,exact,Science%20Fiction,AND&pfilter=lang,exact,eng,AND&pfilter=pfilter,exact,book,AND&tab=default_tab&search_scope=default_scope&sortby=rank&vid=01GALI_GIT&mfacet=tlevel,include,available,1&mfacet=domain,include,Science%20Fiction%20Collection,1&mfacet=rtype,include,book,1&mfacet=library,include,GTMAIN,1&lang=en_US&mode=advanced&offset=0
"""
token = "Bearer eyJraWQiOiJwcmltb0V4cGxvcmVQcml2YXRlS2V5LTAxR0FMSV9HSVQiLCJhbGciOiJFUzI1NiJ9.eyJpc3MiOiJQcmltbyIsImp0aSI6IiIsImV4cCI6MTUwNTg1NDQ0MiwiaWF0IjoxNTA1NzY4MDQyLCJ1c2VyIjoiYW5vbnltb3VzLTA5MThfMjA1NDAyIiwidXNlck5hbWUiOm51bGwsInVzZXJHcm91cCI6IkdVRVNUIiwiYm9yR3JvdXBJZCI6bnVsbCwidWJpZCI6bnVsbCwiaW5zdGl0dXRpb24iOiIwMUdBTElfR0lUIiwidmlld0luc3RpdHV0aW9uQ29kZSI6IjAxR0FMSV9HSVQiLCJpcCI6IjE0My4yMTUuMjcuMzgiLCJvbkNhbXB1cyI6ImZhbHNlIiwibGFuZ3VhZ2UiOiJlbl9VUyIsImF1dGhlbnRpY2F0aW9uUHJvZmlsZSI6IiIsInZpZXdJZCI6IjAxR0FMSV9HSVQiLCJpbHNBcGlJZCI6bnVsbH0.cBAWcWvqfZh6BfwQRYKWYOPqzU9T-HPI0C8VVwJEX5Po_8lgErRE53_42Xb31ZzbDeltyNyt7rmG3Djglbz6hA"

r = json.load(requests.get(requestURL, headers={'Authorization': 'TOK:<%s>' % token}).text)

books = []

for entry in r["docs"]:
	info = entry["pnx"]["display"]

	if "Science Fiction, 4th Floor West" in info["availlibrary"]:
		books.append({
			"author" : info["creator"],
			"title" : info["title"],
			"isbn" : info["identifier"]
		})

print books
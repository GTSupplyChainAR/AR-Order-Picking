import requests
import json

requestURL = "https://gatech-primo.hosted.exlibrisgroup.com/primo_library/libweb/webservices/rest/primo-explore/v1/pnxs?addfields=vertitle,title,collection,creator,contributor,edition,subject,ispartof,description,relation,publisher,creationdate,format,language,identifier,lds05,default.fulldisplay.lds04,lds04,citation,source,lds02,versions,type,coverage,lds03,lds06,crsinfo&getMore=0&inst=01GALI_GIT&lang=en_US&limit=1000&mode=advanced&multiFacets=facet_tlevel,include,available|,|facet_domain,include,Science+Fiction+Collection|,|facet_rtype,include,book|,|facet_library,include,GTMAIN&offset=0&pcAvailability=true&q=sub,exact,Science+Fiction,AND;facet_lang,exact,eng,AND;facet_pfilter,exact,book,AND&qExclude=&qInclude=&rtaLinks=true&scope=default_scope&sort=rank&tab=default_tab&vid=01GALI_GIT"


"""
this bearer auth token will have to change for consecutive runs. to update it, visit the following url, open the networking tab, and find the updated bearer token in a request that used an 'Authorization' header:

https://gatech-primo.hosted.exlibrisgroup.com/primo-explore/search?query=sub,exact,Science%20Fiction,AND&pfilter=lang,exact,eng,AND&pfilter=pfilter,exact,book,AND&tab=default_tab&search_scope=default_scope&sortby=rank&vid=01GALI_GIT&mfacet=tlevel,include,available,1&mfacet=domain,include,Science%20Fiction%20Collection,1&mfacet=rtype,include,book,1&mfacet=library,include,GTMAIN,1&lang=en_US&mode=advanced&offset=0
"""
token = "Bearer eyJraWQiOiJwcmltb0V4cGxvcmVQcml2YXRlS2V5LTAxR0FMSV9HSVQiLCJhbGciOiJFUzI1NiJ9.eyJpc3MiOiJQcmltbyIsImp0aSI6IiIsImV4cCI6MTUwNTk1OTMwMSwiaWF0IjoxNTA1ODcyOTAxLCJ1c2VyIjoiYW5vbnltb3VzLTA5MjBfMDIwMTQxIiwidXNlck5hbWUiOm51bGwsInVzZXJHcm91cCI6IkdVRVNUIiwiYm9yR3JvdXBJZCI6bnVsbCwidWJpZCI6bnVsbCwiaW5zdGl0dXRpb24iOiIwMUdBTElfR0lUIiwidmlld0luc3RpdHV0aW9uQ29kZSI6IjAxR0FMSV9HSVQiLCJpcCI6Ijc2Ljk3LjY3LjIwNSIsIm9uQ2FtcHVzIjoiZmFsc2UiLCJsYW5ndWFnZSI6ImVuX1VTIiwiYXV0aGVudGljYXRpb25Qcm9maWxlIjoiIiwidmlld0lkIjoiMDFHQUxJX0dJVCIsImlsc0FwaUlkIjpudWxsfQ.znDIsJsoFDsIZ0WGeveSY9uFGh074ycVP6xuxy4uE1HjiaGVz5HV-2TYGh7JaRBZw4vAJqhwODqxI5Nf-qBWRA"

r = json.loads(requests.get(requestURL, headers={'Authorization': token}).text)

books = []

for entry in r["docs"]:
	info = entry["pnx"]["display"]

	if any("Science Fiction, 4th Floor West" in loc for loc in info["availlibrary"]):
		author = ', '.join(x.encode('utf-8') for x in info["creator"]) if "creator" in info else None
		title = ', '.join(x.encode('utf-8') for x in info["title"]) if "title" in info else None
		identifier = ', '.join(x.encode('utf-8') for x in info["identifier"]).replace('$$CISBN$$', 'ISBN ') if "identifier" in info else None
		books.append({
			"author" : author,
			"title" : title,
			"isbn" : identifier
		})

with open('books.json', 'wb') as file:
    json.dump(books, file)
import json
json_string = """
{
	"name": "Guido van Rossum",
	"age": 65,
	"degree": ["mathematics", "computer science"],	"retired": true,
	"carrer": {
		"google":{
			"from": 1999,
			"to": 2013
		},
		"dropbox": {
			"from": 2013,
			"to": 2019
		}
	}
}"""
data = json.loads(json_string)
print(data)
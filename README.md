# scraper
Steps to execute the app;
1. Clone form the repository. "git clone git@github.com:ravigoswami25/scraper.git"
2. There are 5 branches: Branch Name Functionality a) basic Basic implementation of given functionality without any db connections. b) DbImplementation Added mongo db database for saving the information c) redis Added redis db for in memory caching d) prod Complete final code e) nestedSearch For deeper search

3. Switch to any branch using git checkout "branch_name" Run "pip install requirements.txt"

4. Run "uvicorn main:app --reload"
5. You can now hit the end point using postman: Curl: curl -X POST "http://127.0.0.1:8000/scrape?api_key=my_static_token" \ -H "Content-Type: application/json" \ -d '{ "pages": 3, "proxy": "proxy url" }

# nil_bot
Bot of NIL data

Postscript 04/08:
I started trying to figure out the git scraping step, but so far, nothing is showing up under Github Actions. I will continue to work on debugging this.

Update 04/08:
I worked towards making a bot that scraped the website On3.com/nil/deals and stored data about Big Ten athletes’ NIL deals in a CSV file. Using tools such as our class resources, ChatGPT, and W3schools – as well as a lot of help from my instructor – I was able to get to the point of having functioning code. I have not encountered any error messages the last several times I have run my code, and the output looks reasonably clean as a CSV file. Because I was spending most of my time figuring out how to write Python code and debugging error messages, I have not yet gotten to the point of making a git scraper that automates the data collection, nor have I gotten to the point of creating a publicly accessible output for the data on a website like Datasette. Thus, in order to access the data, a user must have my code, know how run the code, and download the output as a CSV. I hope to continue working on this bot for my final project and turn the data into a news app that addresses some of these issues.

ChatGPT was one of the resources I used in writing my code. I found ChatGPT to be most helpful when I had the initial framework for my bot but needed assistance determining specific lines of code and debugging error messages. For example, one of the prompts I asked was, “How do I change the date output in this code?” ChatGPT gave me a suggestion of how to revise my code, which I implemented and revised slightly to fit my purposes. As someone who is new to Python, I also found ChatGPT to be helpful in explaining what some of my error messages were occurring.

1. Do I need to store this data somehow? What would that look like?
To this point, I have stored the data as a CSV file that can be downloaded and subsequently imported into R or Google Sheets. 

2. If this bot were able to accept input from users, what would that look like and how might it respond?
Users can interact with the bot in a couple of ways. First, if the code becomes publicly available, then users can run the scraper on their computers and use the data for their own analyses. They can also modify the scraper fairly easily if there is another team or conference of interest. This would require a user who is more well versed with coding and web scraping than the average person. Eventually, I hope to make a version of this bot where a user can interact with the data on a website, like Datasette. In that case, the user will be able to sort and filter the data by athlete, school, company, etc. to find NIL deals.

3. What's the best schedule for updates?
The best schedule for the bot to run its scraper would likely be once a day. Though new NIL deals are added to the On3.com tracker throughout the day, only a handful of them generally apply to Big Ten teams. In each of the last three weeks, the tracker has added an average of four Big Ten deals per week. It is possible that during football season, this number may increase, as football seems to be the main driver of NIL deals. If that is the case, then it may be appropriate for the scraper to run more frequently.

Update 04/01:
What I've gotten done: This week, I switched over from pulling HTML contents from the On3.com website to pulling JSON. This required rewriting many parts of my code. I've gotten to the point now where I have a broad understanding of the new code and have used an annotated version of my scrape.py file to keep track of notes. I have developed an initial dictionary of the attributes to scrape from the On3.com website, and the code works in multiple cases.

Next steps: I think a realistic expectation is that by the end of next week, I will hopefully have code that pulls the data for Big Ten teams without error messages. To do this, I plan to try and use the tutorials on the W3schools.com website to troubleshoot as best as I can on my own. Unfortunately, I am not sure that I will get to the point with this project that I will be able to work too much on the output and end user experience with the data. I had initially hoped to output this data to a Datasette.

Blockers: The main blocker is that Python feels very new and unfamiliar to me, and it takes a lot of time and effort to figure out what are probably basic problems. There may also be some idiosyncrasies with the On3.com website that make it more cumbersome to run scraping code error-free. I am attempting to consult resources like W3schools.com, class examples (https://github.com/NewsAppsUMD/first-web-scraper-dwillis/blob/master/scrapers/wbb/roster.py, https://first-web-scraper-umd.readthedocs.io/en/latest/), and ChatGPT to problem-solve on my own, but it can be hard to decipher how to apply some of the directions to my particular problem.

I do feel some level of investment in this project and am interested in seeing it through a bit more than is likely by the end of next week. I am wondering if I can continue building this bot for my final project and work towards developing it into a news app.
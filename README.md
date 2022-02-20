# Resourceful
## _Take control of your future with Resourceful_

---

## About Resourceful

## Inspiration
* We were inspired to make this project after thinking about ways to level the playing field between those in poor and rich school districts

## What it does
  * Takes in a list of keywords (interests and skills)
  * Outputs a list of URLs and summaries of the webpages deemed most similar to the user’s interests
  * Calculates Wu-Palmer Similarity and Levenshtein Distances to assess how similar a website is to the wants of the user
  * Uses Beautiful Soup in order to get a summary of the activity (generally) as well as the time it takes to complete the course and who the course is offered by for Coursera

## How we built it
* We built the project using python, beautiful soup, NLTK, HMNI, Fuzzy Wuzzy, and Flutter

## Challenges we ran into
* We had trouble in implementing the code that used Levenshtein distances and Palmer similarity, leading to words that had nothing to do with each other being assigned high similarity values.
* We also had trouble with the UI as the version of Tensorflow that HMNI uses was incompatible with mac(the system that our frontend member was using)

## Accomplishments that we're proud of
  * Each member was working with tools they were not familiar with, yet we still completed the product
  * We were able to overcome an issue where Tensorflow would not work with macOS
  * The UI is intuitive and minimalistic

## What we learned
* We learned a lot about Beautiful Soup, selenium, NLTK, HMNI, and measuring abstract concepts like context-empowered text similarity

## What's next for Resourceful
- In Progress: Using multithreading to run Selenium search processes simultaneously
  - Subsequently running BeautifulSoup subprocesses simultaneously
  - Effect: Greatly reduce runtime
- Use of Machine Learning to more accurately find the description of any activity no matter the website
- Use of Machine Learning to compare user tags for skills and interests through categorizing them by field or topic and then choosing the more specific one
  - ML model will be a “Bag-of-words” model → Train using words correlated to category
  - Ex. “python” in skills replaces “coding language” in interests for the combined skills-interests array
- Main Goal: Host Flask API online on services like AWS and deploy flutter app to iOS, Android, web, and Windows

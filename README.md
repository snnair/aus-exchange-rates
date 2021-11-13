Problem Description:

To create an app that will show the latest foreign exchange rates, as well as historical exchange rates. 
Using the Open Exchange Rates API, we can request this data. The challenge also called for the use of a three-tier network architecture.
For scalability, it also calls for the use of the publisher/subscriber model.

General overview and solution:

I thought about the problem and approached it in a fairly straigtforward manner. I used Python and Flask to build this app. 
For the UI, I used HTML/CSS and jQuery along with Bootstrap for templating. I tried to make the UI as polished as possible, within the time that I had.

I tried to adhere to three-tier architecture and model the app in its likeness as much as possible. I do not have a data-tier, as I used the data service directly, and so, it may not be a 3 tier structure in the true sense of the term.
Initially, I did try to make the app with a single page and just one route. I tried writing it with AJAX as well. 
It did not go over too well, and having spent a considerable amount of time trying to get it to work, I settled for synchronous submits.

The learning curve was somewhat steep, as I haven't had the chance to do hands-on development for a while. I tried the best I could within whatever time I could dedicate to this challenge.

TODOS:
1. I could not write any test cases for the project, and it is a big regret for me personally, as I am familiar with writing test cases using selenium.
2. I could not properly go over the documentation for flask and jinja2, and therefore, I couldn't give the design and overall architecture a once-over. 
3. Implement a proper HTML page for the response that is sent back, if the user picks an invalid historical date. At the moment, JSON is returned. 
4. I could not implement a dynamic rendering of the HTML content for the historical data and present it on the same page. I created a separate route for the same. I would definitely want to reconsider this so as to facilitate a better UX.
5. I would also have made fetching the historical exchange rates data asynchronous, using AJAX. 
6. I would also rethink the architecture of the app. The current iteration calls the OER API for latest exchange rates everytime the page loads (or re-loads). This may end up being expensive with a surge in users/traffic. A better approach maybe to cache the results and only call the API periodically. 
7. I could not look into the publisher/subscriber model and think about how it would be implemented. I acknowledge that I lack the necessary systems design knowledge. I would definitely want to look into it and understand it better. It could enable me to think about the scalability of the app in this context.

The solution also includes a REST API that has two endpoints. It responds with latest exchange rates data and historical exchange rates data respectively. Therefore, the overall solution
is along the full-stack track. I tried my best to design it well and think about scalability and did the best I could with the time that I had. 


import pandas as pd

all_blog_posts = []

data = {}
data['time_created'] = "December 6, 2016"
data['url'] = "/blog/flask-plotly-overtime"
data['title'] = "Creating a Bar Graph Visualization With Flask and Plotly"
data['tags'] = ['flask', 'plotly', 'bar', 'graph', 'python', 'web', 'tutorial', 'reddit', 'javascript']
data['picture'] = "blog/flask-plotly-overtime/header.jpg"

all_blog_posts.append(data)

data = {}
data['time_created'] = "February 03, 2017"
data['url'] = "/blog/flask-d3-wordcloud"
data['title'] = "Word Cloud With Flask and D3-Cloud"
data['tags'] = ['flask', 'plotly', 'word', 'cloud', 'python', 'web', 'tutorial', 'reddit', 'javascript', 'd3', 'd3-cloud']
data['picture'] = "blog/flask-d3-wordcloud/header.jpg"
all_blog_posts.append(data)

data = {}
data['time_created'] = "February 07, 2017"
data['url'] = "/blog/flask-plotly-top-ten"
data['title'] = "Pie Chart With Flask and Plotly"
data['tags'] = ['flask', 'plotly', 'pie', 'chart', 'python', 'web', 'tutorial', 'reddit', 'javascript']
data['picture'] = "blog/flask-plotly-top-ten/header.jpg"
all_blog_posts.append(data)

data = {}
data['time_created'] = "March 4, 2017"
data['url'] = "/blog/flask-plotly-sentiment-analysis"
data['title'] = "Sentiment Analysis With Textblob, Plotly and Flask"
data['tags'] = ['flask', 'plotly', 'pie', 'chart', 'python', 'web', 'tutorial', 'reddit', 'textblob', 'sentiment', 'analysis']
data['picture'] = "blog/flask-plotly-sentiment-analysis/header.jpg"
all_blog_posts.append(data)

data ={}
data['time_created'] = "March 10, 2017"
data['url'] = "/blog/RL-multi-armed-bandit"
data['title'] = "Reinforcement Learning: Multi-Armed Bandit"
data['tags'] = ['python', 'reinforcement', 'tutorial', 'learning', 'RL', 'bandit']
data['picture'] = "blog/RL-multi-armed-bandit/header.jpg"
all_blog_posts.append(data)

data ={}
data['time_created'] = "March 15, 2017"
data['url'] = "/blog/RL-grid-world"
data['title'] = "Reinforcement Learning: Grid World"
data['tags'] = ['python', 'reinforcement', 'tutorial', 'learning', 'RL', 'grid', 'world']
data['picture'] = "blog/RL-grid-world/header.jpg"
all_blog_posts.append(data)


data ={}
data['time_created'] = "March 18, 2017"
data['url'] = "/blog/opencv-arrow-detection"
data['title'] = "OpenCV: Arrow Detection"
data['tags'] = ['python', 'open', 'cv', 'arrow', 'detection', 'computer', 'vision']
data['picture'] = "blog/opencv-arrow-detection/header.jpg"
all_blog_posts.append(data)


data ={}
data['time_created'] = "March 19, 2017"
data['url'] = "/blog/RL-multi-armed-bandit-2"
data['title'] = "Reinforcement Learning: Multi-Armed Bandit - Part II"
data['tags'] = ['python', 'reinforcement', 'tutorial', 'learning', 'RL', 'bandit']
data['picture'] = "blog/RL-multi-armed-bandit-2/header.jpg"
all_blog_posts.append(data)

data ={}
data['time_created'] = "May 15, 2017"
data['url'] = "/blog/RL-multi-armed-bandit-3"
data['title'] = "Reinforcement Learning: Multi-Armed Bandit - Part III (featuring Neural Networks!)"
data['tags'] = ['python', 'reinforcement', 'tutorial', 'learning', 'RL', 'bandit', 'neural', 'networks']
data['picture'] = "blog/RL-multi-armed-bandit-3/header.jpg"
all_blog_posts.append(data)


data={}
data['time_created'] = "June 8, 2017"
data['url'] = "/blog/crazy-taxi-1"
data['title'] = "Crazy \"Self Driving\" Taxi 1"
data['tags'] = ['python', 'open', 'cv', 'crazy', 'taxi']
data['picture'] = "blog/crazy-taxi-1/1.PNG"
all_blog_posts.append(data)

all_blog_posts_df = pd.DataFrame(all_blog_posts)
all_blog_posts_df["time_created_dt"] = pd.to_datetime(all_blog_posts_df["time_created"], utc=True)
all_blog_posts_df.sort_values(by="time_created", ascending=False).drop(columns="time_created_dt").to_json("db.json", orient="records")
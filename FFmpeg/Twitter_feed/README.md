# Using the twitter feed, construct a daily video summarizing a twitter handle day
- Convert text into an image in a frame
- Do a sequence of all texts and images in chronological order.
- Display each video frame for 3 seconds

# Steps and Result
## Preparation
- Sign up for the [Twitter Developer], get your own consumer_key, consumer_secret, access_token, access_token_secret.
- Choose the use_timeline you want to present in the video, and change the following line in the ```tweepy_get.py```
```
search_results = api.user_timeline('CNN')
```
- Prepare a background picture for your images, the image below is what I used in this demo.
<p align="middle">
  <img src= "https://github.com/BUEC500C1/video-zhangyanyu0722/blob/master/FFmpeg/Twitter_feed/origin1.png" width= 400>
</p>

## Making your own image sets
- Run the ```tweepy_get.py```, you can customize the user_name and the number of letters in one line. 
```
python tweepy_get.py
```
Explain : In my code, I used the tweepy API and get the latest 20 tweets from "CNN", and delate all emojis. Then add a return for every 50 letters. Finally saved each tweet in a prapared background.
- Run the ```image2video.py```, you need to change the path and the image size.
```
pyrhon image2video.py
```
Explain: In this code, I set the fps = 1/3, which means three seconds per image in the video.












[Twitter Developer]: https://developer.twitter.com/


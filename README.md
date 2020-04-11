# Twitter Word Cloud

Explore on your tweets and create a picture of your most common words!

<p align="center">
  <img src="cloud-red-bl.png" />
  <img src="twitter-blue.png" />
  <img src="cloud-green-ts.png" />
</p>

## Create Your Cloud

First of all, create a `.env` file exactly like `.env.example` file.

You should have a twitter developer account to run this project.
Add your **APP_KEY** and **APP_SECRET** to `.env` and run the project!

Answer the question like below:

    Do you have a twitter developer account? [y/n] y
    Enter username: MyUsername
    Use default font? [y/n] n 
    Enter font path: ./fonts/Roya.ttf   # You can add your own font under fonts directory
    Use default maximum word (500 words)? [y/n] n
    Enter number of maximum word: 200
    Use default image? [y/n] n
    Enter image path: ./twitter.jpg     # You can add your own image
    Choose color: 1.Blue 2.Red 3.Green 4.Yellow: 1

Your image with be save on the root of the project with name `my_own_cloud.png`

### I Am Tired :(

Are you tired to answer all these question every time?!

I have another choice for you! Fill the other field in your `.env` file as the same of the above question and then change `i_am_tired` variable on the top of the `functions.py` to `True`!

That's it ;)




from pytube import YouTube

# ask for the link from user
link = "https://youtu.be/37eRlmos1jQ"  # enter the link you want
yt = YouTube(link)

# Showing details
print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length)
print("Rating of video: ", yt.rating)
# Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

# Starting download
print("Downloading...")
ys.download()
print("Download completed!!")

# Youtube-Downloader

A YouTube Downloader In Python For Downloading Multiple HD Videos Using URL's.

1 => i have imported 3 modules pytube,os and ssl.pytube is the important one that we are using and other 2 modules is used to ignore a SSL certification error.

2 => i have created a list varibale named video_list to collect the multiple URL's.

3 => we are getting the input url's inside a while loop and appending it to the video_list until the input values is "stop"

4 => Using a for in loop we iterate through the video_list to get each url if you are entering multiple URL's.

5 => we created a object and stored it in a variable v.

6 => there will be many streams avalible for one video so are filtering the streams by itag using the method streams and get_by_itag.

7 => finally we used the download function to download each video and after the download is finished the message "downloaded" will be printed.

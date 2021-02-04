# Youtube Parse-n-Scrap
### How to run the script
1) Write all the Youtube video titles in the songs.txt file
    Example:    
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Never gonna give you up
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A flock of seagulls - i ran
    
    The name of the youtube videos doesn't have to be the exact video name, since it will scrap the first url of the search result, so typos are not a problem.
2) Run the script script.py using python3 
3) The script will generate the list of all the url of these songs one by one, using the same order they were written in the songs.txt file.
The output file will be the url.txt.
4) Run the youtube-dl python script using thwe follwing command:
    ###### youtube-dl --extract-audio --audio-format mp3 --audio-quality 0 -s url.txt

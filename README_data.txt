My end data in which the functions were performed was a csv file containing season number, episode number (in the season), guest stars, directors, writers, 
air date, viewer number for the premiere, a short-form number of viewers in millions (e.g. 2.7 would be 2,700,000 for this column), air year, air month, and
imdb rating (out of 10). I obtained information for every column besides the rating from wikipedia pages (the last column was obtained through imdb). 

Sources:
1. Family Guy information
ORIGIN: https://en.wikipedia.org/wiki/Family_Guy_season_*
  * = 1-18, as i got information for each of these seasons. 
FORMAT: the final format was a csv file, but originally was a wikipedia table 
HOW DATA WAS ACCESSED: I parsed through the episode table rows and obtained the season number, episode number, director, air date, and viewer count and then I 
wrote this information to a csv file. No caching was used.
SUMMARY OF DATA: This method obtained 348 rows with the 5 previously mentioned columns. 

2. Futurama information
ORIGIN: https://en.m.wikipedia.org/wiki/Futurama_season_*
  * = 1-8, as i got information for each of these seasons. 
FORMAT: the final format was a csv file, but originally was a wikipedia table 
HOW DATA WAS ACCESSED: I parsed through the episode table rows and obtained the season number, episode number, director, air date, and viewer count and then I 
wrote this information to a csv file. No caching was used.
SUMMARY OF DATA: This method obtained 159 rows with the 5 previously mentioned columns. 

3. South Park information
ORIGIN: https://en.m.wikipedia.org/wiki/South_Park_season_*
  * = 1-23, as i got information for each of these seasons. 
FORMAT: the final format was a csv file, but originally was a wikipedia table 
HOW DATA WAS ACCESSED: I parsed through the episode table rows and obtained the season number, episode number, director, air date, and viewer count and then I 
wrote this information to a csv file. No caching was used.
SUMMARY OF DATA: This method obtained 306 rows with the 5 previously mentioned columns. 

4. The Simpsons information
ORIGIN: https://en.wikipedia.org/wiki/The_Simpsons_season_*
  * = 1-29, as i got information for each of these seasons. 
FORMAT: the final format was a csv file, but originally was a wikipedia table 
HOW DATA WAS ACCESSED: I parsed through the episode table rows and obtained the season number, episode number, director, air date, and viewer count and then I 
wrote this information to a csv file. No caching was used.
SUMMARY OF DATA: This method obtained 617 rows with the 5 previously mentioned columns. 

After gathering the base information, I downloaded the csv to my local machine and manually entered information on guest stars and episode ratings. 
The sources for the information are listed below. I also manually created other date columns indicating the month and year each episode aired and a
column showcasing the short-form viewer count

5. Guest Star information
ORIGIN: 
*   https://en.wikipedia.org/wiki/List_of_Family_Guy_guest_stars
*   https://en.wikipedia.org/wiki/List_of_Futurama_guest_stars
*   https://en.wikipedia.org/wiki/List_of_The_Simpsons_guest_stars_(seasons_1%E2%80%9320)
*   https://en.wikipedia.org/wiki/List_of_The_Simpsons_guest_stars_(seasons_21%E2%80%93present)
FORMAT: the final format was a csv file, but originally was a wikipedia table 
HOW DATA WAS ACCESSED: I manually added in this column/information into my dataset. No caching was used.
SUMMARY OF DATA: this method added an extra variable for 937 of the 1435 total observations in the dataset

6. IMdB rating information
ORIGIN: 
*   https://www.imdb.com/title/tt0096697/episodes/?ref_=tt_eps_sm
*   https://www.imdb.com/title/tt0182576/episodes/?ref_=tt_eps_sm
*   https://www.imdb.com/title/tt0121955/episodes/?ref_=tt_eps_sm
*   https://www.imdb.com/title/tt0149460/episodes/?ref_=tt_eps_sm
FORMAT: the final format was a csv file, but originally was listed by episode on the website
HOW DATA WAS ACCESSED: I manually added in this column/information into my dataset. No caching was used.
SUMMARY OF DATA: this method added an extra variable for all 1435 observations in the dataset


7. FINALIZED DATASET:
ORIGIN: mentioned above
FORMAT: csv file
HOW DATA WAS ACCESSED: for analysis, I manually imported the dataset/file to my code and parsed the CSV file. No caching was used. How I accessed
the origin files is mentioned above. 
SUMMARY OF DATA: there are 1435 observations of 4 long-running adult cartoons (Family Guy, Futurama, South Park, and The Simpsons). There
are 11 variables of interest for each episode - show,	season,	episode,	guest star,	directors,	writers,	air date,	viewer count,	shortened viewer
count, air month,	air year,	and imdb rating. 






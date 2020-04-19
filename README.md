# Election-Analysis

## Project Overview
A Colorado Board of Elections employee has implored me to finish the elction audit of a local comgressional election
1. I was able to calculate the total number of votes cast
2. I then got the complete list of candidates who received votes
3. Then I calculated the number of votes each candidate received
4. I calculated the percentage of votes after calculating the number of votes receieved
5. Lastly, I determined the victor of the election based on popular vote

## Resources
-Data Source: election-results.csv
-Software: Python 3.7.6 and VS Code 1.44.1

## Summary
The analysis of the election:
- There were 369,711 votes in total
- The candidates were:
  1. Charles Casper Stockham
  2. Diana DeGette
  3. Raymon Anthony Doane
- The results were as follows:
  1. Charles Casper Stockham receieved 23.0% of the vote and 85,213 total votes.
  2. Diana DeGette receieved 73.8% of the vote and 272,892 total votes.
  3. Raymon Anthony Doane receieved 3.1% of the vote and 11,606 total votes.
_The Winner of the Election was:
  Diana Degette who received 73.8% of the vote and the overwhelming majority of popular vote in 272,892 total votes.
  
## Challenge Overview
- The Colorado Board of Elections employee then wanted me to find the number and percentages of votes in each of the three counties: Arapahoe, Denver, Jefferson

## Challenge Summary
  1. I first created variables and lists to differentiate the for loops I was about to create concerning each of the counties
  2. I then specified to VS Code which rows to grab the number of votes from with county_name = row[1]
  3. Inside the previous for statement I created in the module work, I coded two if statements to specifically count the number of votes that each county had
  4. After that, I created a for loop to show the vote_percentage and then county_results using an f-string : (f"{county}: {vote_percentage:.1f}% ({i:,})\n") and then had it print the results.
  5. I then used text_file.write(county_results) to write the text in the file
  6. After completing, I wrote in a quick if statement showing the county with the majority of the votes
  
  RESULTS:
  1. Jefferson County had 38,855 total votes which encompassed 10.5% of the total votes
  2. Denver County had 306,055 total votes which came out to be the overwhelming majority of 82.8% of the total votes
  3. Arapahoe County had 24,801 total votes which was 6.7% of the total votes.
  Denver County had the majority of the total votes in the congressional election.
  This challenge was difficult with all of the different conditions that had to be met and the spacing as well made it challenging. Having my previous module work helped immensely as I had a blueprint in order to refactor and make everything work together.

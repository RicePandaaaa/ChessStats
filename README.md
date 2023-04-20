# What is this?
It is simply a collection of various programs that display random statistics using lichess' public game database. This code was originally made in 2020 as my first venture into data visualization, but hopefully I can update this to better represent my skills in data pre-processing and visualization.

### Databases Used and Output
You can find the databases that were used at https://database.lichess.org/. The programs will be using the large database. The large database has 1.2 million games stored and is listed under November 2014. 

However, there will be two outputs shown (in the outputs folder) per program. Not only will there be one output for the large database, there will be one for the small database. This small database has 121 thousand games stored and is listed under January 2013. 

### Required Modules
So far, these are the only modules you will need to import for the programs to work:
 - chess.pgn
 - numpy
 - matplotlib
 
### What data am I analyzing and what will I use it for?
I will be analyzing the following: ELO of both players, moves played, final score, openings used, color of the player, and time control.

The data, used either individually or in conjunction with each other, will be or have been used to figure out the following:
 - White's chance of winning based on their first move ([DONE](https://github.com/AnthonyHPham/lichess-Data-Analysis/blob/master/Programs/WinningFirstMoves.py))
 - Black's chance of winning based on their response to White's first move ([DONE](https://github.com/AnthonyHPham/lichess-Data-Analysis/blob/master/Programs/WinningResponseMoves.py))
 - Number of games won by checkmate/resignation or time
 - Number of captures between a certain range of moves (such as from move 10 to 20, or even the entire game)
 - Most and least popular openings
 - Average amount of moves given the time control
 - Chance of an upset (person A beats person B where person B has at least 100 more ELO points than person A)
 - Chance of a walkover (person A beats person B where person B has at least 100 less ELO points than person A)
 - Number of times a specific piece has been moved
 - Popularity of time controls (will use other databases)
 
 Please note that this is not a final list of what I want to figure out with the data!

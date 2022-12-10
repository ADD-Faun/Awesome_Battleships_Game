# Battleships Game

Battleships Game is a python terminal game, which runs in Code institute mock terminal Heroku

users choose a grid square on the computers board to try and find the computers ships before the 
computer finds theirs. The user can see there ships and where the computer has shot on their grid
and can see where they have shot on the computers grid.

![Responsice Mockup](assets/images/responsiveness-readme.png)

## Features 

### Existing Features

- __Grid generation__

  - A square grid is generated for each side to be displayed during the game.
  - ships are randomly placed on each grid. 
  - users can not see the computers ships.
  - Grid has letters and numbers along sides to help choose square.
  - Grid locations are stored in a dictionary.

![Nav Bar](assets/images/Navigation-mock-up.png)

- __User input and validation__

  - Users are asked for a grid square by row and column with prompts of possible choices. 
  - If selected row or column is not on the grid they are asked to resubmit that data.
  - If user selects a square they have already guessed they are asked to resubmit data.
  - Incorrect inputs return "' ' is invalid" and asks them to resubmit.
  

![Landing Page](https://github.com/lucyrush/readme-template/blob/master/media/love_running_landing.png)

- __Data control__

  - Data for each sides board and ships is contained in a class.
  - The scores, grid size and number of ships stored in a dictionary. 
  - there are some permanent variables. 

![What We Do](assets/images/what-we-do-readme.png)

- __Grid size and ship number__ 

  - Allows player to choose number of ships between 1 and 26 as long as it doesn't fill
    the board.
  - Allows player to choose grid size between 2 and 7.
  - 

![Footer](assets/images/footer-readme.png)

- __Score__

  - How many shots there have been and how many ships they hit is told to the user at
    the end of every turn.
  - Users are told how many ships they have left and how many they have left to sink.
  - Users are told if they hit or missed every turn.

### Features Left to Implement

- Allow players to place there own ships 
- Ships of different sizes 
- Having the computer make better quesses when ships are bigger than one square

------
## Testing 

__How testing was done__

- Testing in my local terminal
- Passed code through a PEP8 linter and confirmed there are no problems 
- Given invalid data
    - letters where numbers are expected and the reverse
    - no data entered
    - Blank spaces and random symbols like ! {} []
- Set a debug_mode in the print_grid function to show computer ships when
  Debug_mode is True. Allowing to test hit, miss and win messages and 
  test score tracking.

__Bugs fixed__

- Enteries such as symbols ] , } and empty space were being accepted when not in the accepted 
  range and caused crashes when trying to change to an interger. I fixed this by adding a list 
  of unexcepted characters.
- Grid size can't be bigger than 26 as it runs out of letters. fixed by limiting grid size.
- Grid size can't be bigger that 9 as it miss aligns the row with the column. fixed by limiting
  choice of grid size.
- Input request was to long inside while and if statements, so set to a variable.
- Using user input of letters made for too long code or crashes. fixed by changing letter input
  recieved into a number using ord(x) - 65 .

__Remaining Bugs__

- No bugs remaining

------

## Deployment

Widnes Climbers was deployed using github pages. 

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigated to the Settings tab 
  - Navigated to the pages section under Code and automation
  - Source chosen was deploy from branch
  - Main branch was chosen and saved, page refreshed with a working link to indicate the successful deployment. 

The live link can be found here - https://add-faun.github.io/Climbers/index.html


## Credits 

Lots of inspiration was taken from the love running website project taught by Code institute 

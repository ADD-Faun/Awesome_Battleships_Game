# Battleships Game

Battleships Game is a python terminal game, which runs in Code institute mock terminal Heroku

users choose a grid square on the computers board to try and find the computers ships before the 
computer finds theirs. The user can see there ships and where the computer has shot on their grid
and can see where they have shot on the computers grid.

![Responsice Mockup](assets/images/responsiveness-readme.png)

## Features 

### Existing Features

- __Grid generation__

  - A 5 by 5 grid is generated for each side to be displayed during the game
  - ships are randomly placed on each grid 
  - users can not see the computers ships 

![Nav Bar](assets/images/Navigation-mock-up.png)

- __User input and validation__

  - Users are asked for a grid square by row and column with prompts of possible choices 
  - If selected row or column is not on the grid they are asked to resubmit that data
  - If user selects a square they have already guessed they are askked to resubmit data
  

![Landing Page](https://github.com/lucyrush/readme-template/blob/master/media/love_running_landing.png)

- __Data control__

  - Data for each grid maintained in a dictionary 
  - Most data is only active during game time 
  - there are some permanent variables 

![What We Do](assets/images/what-we-do-readme.png)

- __The Footer__ 

  - The footer section includes links to the relevant social media sites for Widnes Climbers. The links will open to a new tab to allow easy navigation for the user. 
  - The footer is valuable to the user as it encourages them to keep connected via social media
  - The footer was made to always be at the bottom of the page so larger screen sizes don't have blank at the bottom when there is not enough content.

![Footer](assets/images/footer-readme.png)

- __Where We Go page__

  - The Where We Go page will provide the visitor with supporting images to see what the indoor facilities are like. 
  - The Where We Go page will provide the visitor with supporting images to see what the outdoor locations are like.
  - This section is useful for the visitor to imagine what it would be like to join the group.
  - Reviews the places the group goes

![Where We Go](assets/images/where-we-go-readme.png)

- __Join Us Page__

  - This page will allow the visitor to signed up for Widnes Climbers to receive a welcome letter and information on which part they are interested in. The user will be able specify if they are interested in bouldering , rope climbing or outdoor climbing. 
  - The visitor may select one , two or three types of climbing but must select one.
  - The visitor will be asked to submit their full name and email address. 

![Join Us](assets/images/join-us-readme.png)

### Features Left to Implement

- Allow player to choose grid size without it being too big for the screen
- Allow players to place there own ships 
- Ships of different sizes 
- Having the computer make better quesses when ships are bigger than one square

## Testing 

__How testing was done__

- Testing in my local terminal
- Passed code through a PEP8 linter and confirmed there are no problems 
- Given invalid data
    - letters where numbers are expected and the reverse
    - no data entered
    - Blank spaces and random symbols like ! {} []

__Bugs fixed__

- Enteries such as symbols ] , } and empty space caused crashs when code tryed to use it.
  I fixed this by adding list of unexcepted characters.
- Crashed when trying to change non number into int. Fixed by confirming data is number
  before changing to int.





------
In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your project’s features and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.


### Validator Testing 

- HTML
  - Section without heading, heading not needed, changed to div.
   No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fadd-faun.github.io%2FClimbers%2F)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fadd-faun.github.io%2FClimbers&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)

### Unfixed Bugs

Join us page image quality is low. Different file sizes and larger quality uploads did not work.

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

### Code & Styling

- Footer code to keep it at the bottom of the page and not have it overlap other content was taken from https://developer.mozilla.org/en-US/docs/Web/CSS/Layout_cookbook/Sticky_footers . This code was free use.
- Background pattern done using css is from free to use code from https://github.com/Yuvrajchandra/CSS-Background-Patterns
- The style of the form and join us page was taken from the Love running project 

### Content 

- The style of the form and join us page was taken from the Love running project (provide more links)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media
##### General

- Cover/hero image used on home page taken from free open source site pexel.com (pexels-m-venter-1659437)
- Join us page background image taken from free open source site pexel.com (pavel-danilyuk-7591309)
##### Where we go

- Where we go 1st image, matchworks climbing center, used to review and advertise the location we visit. Taken from their facebook https://www.facebook.com/TCHLiverpool/photos/5308587909198965/  & website https://www.theclimbinghangar.com/media/3103/hangar_swansea_l-lonsdale__0508-2-edit-x2.jpg?center=0.483091787439614
- Where we go 2nd image, boardroom climbing center, used to review and advertise the location we visit. Taken from their website https://www.theboardroomclimbing.com/
- Where we go 3rd image showing outdoor bouldering taken from subscription image site dreamstime.com https://www.dreamstime.com/stock-photo-couple-bouldering-happy-boulders-women-climbing-men-spotting-image55085115
- Where we go 4th image showing man climbing a mountain from image site getty.com
- Where we go 5th image showing people at a pub taken from free open source site pexel.com
##### What we do 

- What we do 1st image showing indoor bouldering, used for education, taken from xxxx
- What we do 2nd image showing two types of rope climbing taken from https://www.vdiffclimbing.com/basic-top-rope/
- What we do 3rd image showing two women bouldering outdoors taken from climbinghouse.com
- What we do 4th image showing man climbing a mountain from image site getty.com
# [Are you a gamer quiz]
> A short one-line tagline for your quiz or questionnaire

## Overview
> This quiz is to test the knowledge of gaming and technology use of the user.
> The user will answer five multiple choice questiones. Each answer would be stored in a variable and checked using conditional statments.
> Correct answers will be increase the users score. At the end of the quiz the user total score will determine the final message they received.

## Sample Questions and Responses
> 1 What company makes the Playstation?
> 1. Microsoft
> 2. Sony
> 3. Nintendo


> 2 How many players are able to play on the court in basketball?
>  1. 10
>  2. 8
>  3. 5


>  3 Which device is manly used to controll a game?
>  1. controller
>  2. printer
>  3. pen


> 4 which game features the My career game mode?
> 1. NBA 2k
> 2. MarioKart
> 3. Fortnite

> 5 Which of these are a gaming console?
> 1. Macbook
> 2. lenox
> 3. PS5



## Variables
> answer one (str)stores the user response to question one
> answer two (str)stores the user response to question two
> answer three (str)stores the user response to question three
> answer four (str)stores the user response to question four
> answer five (str)stores the user response to question five
> score (int) keeps track of user total correct answer

## Conditional Logic Outline
>Conditional statement one - Checks the answer to question 1 about which company makes
>playstation.
  - if the user chooses Sony display a correct message and increase score by one
  - elif the user chooses Microsoft  or Nintendo display a incorrect message 
  - else display invalid choice message

> Conditional statement 2 checks the answer to question 2 about how many basketball players
> from one team are able to be on the court.
   - if the user chooses 5 display a correct message and increase score by 1 
   - elif the user chooses 6 or 7 display an incorrect message 
   - else display an invalid choise message 

> Conditional statement 3 checks the answer to question 3 about which device is used to control
> a video game
  - if the user chooses controller display a correct message and increase score by one
  - elif the user chooses chooses printer or scanner display an incorrect message 
  - else display an invalid choice message

  > Conditional statement 4 checks the answer to question 4 about which game has My career .
    - if the user the chooses Nba 2k display correct message and increase score by one 
    - elif the user chooses MarioKart or Fortnite display incorrect message 
    - else display an invalid choice message

> Conditional statement 5 checks the answer to question 5 about which device is a gaming console
  - if the user chooses PS5 display a correct messag and increase score by one
  - elif the user chooses lenox or Macbook display incorrect message 
  - else display an invlaid choice message

> Conditional statement 6 checks user final score 
  - if the score is 5 display perfect score message 
  - elif the score is greater than or equal to 3 and less than 5 display good job message
  - else display a message saying keep practicing

## How to Run
1. Clone this repo
2. Run `python3 main.py` or `python main.py`

## Demo Video
[DELETE AND REPLACE ME: link to your 5-minute explanation video]

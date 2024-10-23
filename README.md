# Who Wants to Be a Millionaire API

This project is a backend API for a "Who Wants to Be a Millionaire" style quiz game built using the Banjo framework.

## Overview

The API allows users to play a quiz game similar to the popular TV show "Who Wants to Be a Millionaire". Players can start a new game, answer questions, and potentially win virtual prize money up to £1,000,000.

## Features

- Start a new game
- Get random questions
- Answer questions
- Add new questions to the database
- Get hints for questions
- Add hints to existing questions

## API Endpoints

|
 Endpoint 
|
 Method 
|
 Description 
|
 Arguments 
|
|
----------
|
--------
|
-------------
|
-----------
|
|
`/millionaire/start_game`
|
 GET 
|
 Starts a new game session 
|
 None 
|
|
`/millionaire/next_question`
|
 GET 
|
 Retrieves the next random question 
|
 None 
|
|
`/millionaire/answer`
|
 POST 
|
 Submit an answer to a question 
|
`id`
 (int), 
`answer`
 (str) 
|
|
`/millionaire/add_question`
|
 POST 
|
 Add a new question to the database 
|
`question_statement`
 (str), 
`option_a`
 (str), 
`option_b`
 (str), 
`option_c`
 (str), 
`option_d`
 (str), 
`correct_answer`
 (str), 
`hint`
 (str) 
|
|
`/millionaire/get_hint`
|
 GET 
|
 Get a hint for a specific question 
|
`id`
 (int) 
|
|
`/millionaire/add_hint`
|
 POST 
|
 Add a hint to an existing question 
|
`id`
 (int), 
`hint`
 (str) 
|

## Setup

1. Ensure you have Banjo installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory.

## Running the Server

To start the Banjo server, run the following command in your terminal:
banjo --debug
The server will start, and you can access the API endpoints using the base URL followed by the specific endpoint paths.

## Playing the Game

1. Start a new game by sending a GET request to `/millionaire/start_game`.
2. Retrieve the next question by sending a GET request to `/millionaire/next_question`.
3. Answer the question by sending a POST request to `/millionaire/answer` with the question `id` and your `answer`.
4. Continue playing until you either answer all questions correctly or provide an incorrect answer.

## Contributing

Feel free to contribute to this project by adding more questions or hints. You can use the `/millionaire/add_question` endpoint to add new questions to the game and the `/millionaire/add_hint` endpoint to add new hints to the game.

## Model

The main model in this project is the `Question` model, which includes the following fields:

- `question_statement`: The text of the question
- `option_a`, `option_b`, `option_c`, `option_d`: Multiple choice options
- `correct_answer`: The correct answer to the question
- `answered_correctly`: Boolean indicating if the question has been answered correctly
- `prize_money`: The amount of money associated with the question
- `hint`: An optional hint for the question
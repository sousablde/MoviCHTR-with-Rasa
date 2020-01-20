
![MovieCHTR](https://github.com/sousablde/MoviCHTR-with-Rasa/blob/master/MoviCHTR%20Logo.png)
# MoviCHTR
## A conversational bot on movie thematics
- the bot finds:
  - movies a director is known for
  - movies and actor is known for
  - the release date of a movie if the movie title is provided
  - the overview/plot of a movie if a title is provided
  - searches for the rating of a movie based on movie title
  - Finds popular movies by year
  - engages in basic chit-chat

  
## The project goal was to:
- Understanding the Rasa framework
- Installing the Rasa framework
- Experience with manipulating language based data

## Software used
Everything is programmed in python, to follow this project you need the following
- Python <=3.6.8
- Jupyter Notebook
- Ngrok
- Slack

## The source tools used within Jupyter notebook are
- rasa nlu
- rasa core
- rasa x

## Additional support from:
- text editor
- web browser
- terminal

## File overview:
`data/core/` - contains stories 

`data/nlu` - contains example NLU training data

`demo` - contains custom action/api code

`domain.yml` - the domain file 

`config.yml` - the Rasa config file

`events. ` - files related to rasa x usage

## Testing
- Within jupyter notebooks comment out slack related code from within the loading assistant definition, engage with load_assistant()
- outside of notebook launch rasa x for a webbrowser based testing and interactive learning
- from slack: request server start and engage with @movichtr


## More extended step by step information and visual tutorials provided within the notebook.

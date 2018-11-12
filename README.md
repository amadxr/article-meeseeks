# Article Meeseeks

> Article gatherer chatbot for Telegram.


Chatbot for Telegram platform that pulls every link it receives and saves it in a Google Drive spreadsheet to build a knowledge database and share it with the rest of your team.

The purpose of this chatbot is to take advantage of the already existing information sharing platforms in your team by gathering all the juicy articles and creating a knowledge repository from where you can choose to share to social media, internally or just save them for later.

![Look at me!](https://s3.amazonaws.com/helpbucket.tektonlabs.com/uploads/960684c3-4a3c-432b-b25a-5d7f4405283b/c8758ba4-7f27-4a4a-8950-1084ee158cd5/meese.jpg)

## Installation / Development setup

Run this in a terminal:

```sh
git clone https://github.com/joamadorrr/article-meeseeks.git

cd article-meeseeks

cp .env.example .env

```

We just created a file with all the environment variables you will require:

* BOT_TOKEN: Once you've created your bot, talk to the BotFather and ask him for your bot's token
* SHEETS_SCOPE: Unles you want to do something weird, leave the default
* SPREADSHEET_ID: To get the id for your spreadsheet read this: https://developers.google.com/sheets/api/guides/concepts#spreadsheet_id
* RANGE_NAME: Read the A1 notation part in the link above

If you are setting up a development environment I highly recommend you use pipenv. Otherwise, you can install the requirements from the requirements.txt file.

### Pipenv

Here we create an environment for the chatbot in python 3 and copy the last version of the development environment from the pipfile.lock

```sh
pipenv --three

pipenv shell

pipenv install --ignore-pipfile

```

After installing all the requirements, the Google Sheets API needs to be enabled.

### Google Sheets API

* Follow the Step 1 instructions in: https://developers.google.com/sheets/api/quickstart/python
* After you create your new Google Sheets Project, download the configuration file and move it to the chatbot's root folder under the name credentials.json

## Usage example

Hmm basically just talk to it and send him links to cool articles you wanna share with your team. A really cool feature of Telegram bots is that you can make them join group conversations, so the Article Meeseeks can infiltrate different conversations and gather articles from those too.

## Release History

* 0.1.0
   * The first proper release
   * Environment variables support added
* 0.0.1
   * It works but a lot of things need to be enhanced before "official launch"


## Meta

Jo Amador – [@joamadorrr](https://twitter.com/joamadorrr)

Distributed under the MIT license. See `LICENSE` for more information.

[https://github.com/joamadorrr](https://github.com/joamadorrr/)

## Contributing

1. Fork it (<https://github.com/joamadorrr/article-meeseeks/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

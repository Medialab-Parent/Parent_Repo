# White Knight Browser Extension

This is the parent repository of all submodules of our White Knight Browser Extension which we developed as part of the Medialab course at the University of Applied Science St. Pölten (BA Creative Computing, 2024). 

## Purpose
With this project we want to contribute to making our day-to-day social media experience, for now only YouTube, safer. 

## Platform
- Browser: Chromium
- Social Media Site: YouTube

## Features
1. Analyze YouTube comments
2. Detect if they are hateful or not
3. Let user's generate counter speech for these hateful comments
4. Let user's marke hateful comments on their own, if they are not detected by our extension

## Running the project using Docker

### Open up the folder of this project in a git terminal and then switch into the AI_Frontend folder to generate a "dist" folder using the following commands
1. `cd AI_Frontend` 
2. `npm i`
3. `npm i vue-i18n --save-dev` 
4. `npm run build`
   
### Next up, to run the backend of this project through docker, go back into the parent folder and execute the following commands
1. `cd ..`
2. `docker compose up --build`

### Lastly, load the extension into your chromium browser 
1. navigate to your extension list
2. enable developer mode
3. load the dist folder, you've generated before
  

## License
- This project is licensed under the MIT License.

## All extension repositories:
- Frontend: https://github.com/Medialab-Parent/AI_Frontend
- API-Wrapper: https://github.com/Medialab-Parent/AI_API-Wrapper
- Database: https://github.com/Medialab-Parent/AI_Database
- Server: https://github.com/Medialab-Parent/AI_Server
- Filter: https://github.com/Medialab-Parent/AI_Filter

## Contact
- For any questions or issues, please contact [cc211002@fhstp.ac.at].

# Dota2Matches
Exploration of Dota 2 matches, including but not limited to match prediction. Continues project from graduate school.

## LICENSE
This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

## STRUCTURE
- v1_2019Project
-- In 2019, I explored this dataset as part of a grad school project. The models are built from two distinct datasets that cover player skills using TrueSkill, player performance, character selection, and match scores. Results show that models with player skill features and in-game performance metrics perform much better than models based solely on character selection. 
- v2_TrueSkillDataset
-- In 2022, I returned to this project for a second look, again with Logistic Regression. Adding new tools and focusing (almost) exclusively on TrueSkill brought clarity and simplicity to the project. Still, both v1 and v2 relied on datasets provided by Kaggle. I chose to go back to the original API myself to create an end-to-end solution that does not rely on old data.
- v3_ETLtoModel
-- The goal is the following:
1. Pull from Dota2 API, store in Postgres
2. Query Postgres for ML
3. Query Postgres for dashy
-- Extensions to v3:
1. Put postgres on cloud server (Heroku?) (python anywhere?) and automate data pulls, updates, truncates, etc. every day
2. Test ML regularly, when threshold met rerun
3. Use Dashy over time to watch for trends
4. Organize the workflow with Airflow

## TO UNDERSTAND THIS PROJECT
- Start by opening v1 and check out the PDF grad paper. This walks through the entire 2019 project.
- Then jump into v2 to see the simplified 2022 recreation of the project focusing on TrueSkill.
- Finally, head into v3 to see the end-to-end solution taking shape.

## TO REPLICATE
- v1: Please refer to the 2019 Paper in 2019_Project for a description of work and outcomes.
- v2:
-- Download the Data Source (below)
-- Using Anaconda 2022.05 or later
-- Using Python 3.9.12 or later
- v3:
-- Using Anaconda 2022.05 or later
-- Using Python 3.9.12 or later
-- Using Postgres 15
-- This project is not yet in Docker. You must have a Postgres server set up to read/write data, etc.

## DATA SOURCE
- v1 and v2: Both projects build from a Kaggle dataset (https://www.kaggle.com/datasets/devinanzelmo/dota-2-matches) made available by Devin Anzelmo (https://www.kaggle.com/devinanzelmo) using a CC BY-SA 4.0 License. My project also uses a CC BY-SA 4.0 License to meet the requirements of the data source.
4.0 requirements:
-- Creator of Kaggle dataset: Devin Anzelmo. Original source of data: Opendota (formally Yasp)
-- Copyright notice: None
-- Title: "Dota 2 Matches"
-- Notice of Public License: previous work licenses as CC BY-SA 4.0
-- Link to material supplied: https://www.kaggle.com/datasets/devinanzelmo/dota-2-matches
-- Indication of modification: I have not modified the data from the original project. I used the 'Download' option on Kaggle go collect the dataset on July 31, 2022 (455MB at the time)
-- Indication of material availability: See above
-- Removal of attribution information upon request: N/A
-- All reasonable information to medium, means, and context: See above.
- v3: Details here https://docs.opendota.com/ and here https://www.opendota.com/api-keys 
-- In v3, for now, data are stored in my Postgres db for use in this project. I'm still working with the API and will eventually be setting up an Airflow.
-- When it comes to actual insight generation later (ex: claims of ML accuracy), I will work to make data used in modeling available to reproduce results.
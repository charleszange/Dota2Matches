## End to end solution
1. Pull from Dota2 API, store in Postgres
2. Query Postgres for ML
3. Query Postgres for dashy

## Extensions
1. Put postgres on cloud server (Heroku?) (python anywhere?) and automate data pulls, updates, truncates, etc. every day
2. Test ML every day, when threshold met rerun
3. Use Dashy over time to watch for trends
4. Organize the workflow with Airflow
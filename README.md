
[![app](https://github.com/wheeleruniverse/wheelerrecommends-scraper/actions/workflows/app.yml/badge.svg)](https://github.com/wheeleruniverse/wheelerrecommends-scraper/actions/workflows/app.yml)
[![analytics](https://github.com/wheeleruniverse/wheelerrecommends-scraper/actions/workflows/analytics.yml/badge.svg)](https://github.com/wheeleruniverse/wheelerrecommends-scraper/actions/workflows/analytics.yml)

## Wheeler Recommends Scraper -- Serverless Web Scraper

This repository contains a serverless web scraper designed to collect data from wheelerrecommends.com. It leverages Python, Beautiful Soup, and Selenium to scrape website content and stores the data in S3 for further analysis using AWS Glue and Athena. 


### Features

- Serverless Scraping: Executes scraping tasks via AWS Lambda functions, enabling scalable and cost-effective data extraction.

- Scheduled Execution: Scrapes data on a defined schedule using AWS EventBridge (e.g., cron jobs for home page, rate-based for movie details).

- Data Storage: Stores scraped data as TSV files in a versioned S3 bucket (wheelerrecommends-scraper-data).

- Data Cataloging: Automatically catalogs scraped data using AWS Glue Crawlers, making it queryable.

- Data Analysis: Integrates with Amazon Athena for running SQL queries on the collected data stored in S3.

- Analytics API: Provides a serverless API for querying the scraped data via Athena using ODBC connectivity.

### Technologies Used

- Programming Language: Python

- Libraries:
    - Beautiful Soup: For parsing HTML and XML documents.
    - Selenium: For browser automation, enabling scraping of dynamic content.
    - pyodbc: Python library for ODBC database access, used to connect to Athena.

- AWS Services:
    - Lambda: Runs the scraping and analytics functions. 36
    - S3 (Simple Storage Service): Stores raw scraped data (wheelerrecommends-scraper-data) and Athena query logs (wheelerrecommends-scraper-logs).
    - EventBridge: Schedules the Lambda functions for scraping tasks.
    - Glue:
      - Glue Crawlers: Automatically discover schema and partition data in S3, cataloging it in the Glue Data Catalog.
      - Glue Data Catalog: A metadata repository for the scraped data, making it accessible to Athena.
    - Athena: A query service to analyze data directly in S3 using standard SQL.
    - API Gateway: Exposes the analytics API for querying data from Athena.
    - ECR (Elastic Container Registry): Stores Docker images for Lambda functions.

- Deployment:
    - Docker: Lambda functions are deployed as container images.
    - Serverless Framework: Used to define and deploy the serverless application. 
    - GitHub Actions: Automates the build and deployment of the scraper and analytics components. 

### Architecture

The scraping process is initiated by AWS EventBridge, which triggers Lambda functions on a schedule (e.g., every 15 minutes for the home page, every 9 minutes for movie details). These Lambda functions then perform the web scraping and upload the extracted data to an S3 Data bucket. From there, AWS Glue Crawlers run hourly to discover new data and update the Glue Data Catalog. Finally, Amazon Athena can query the data in the S3 Data bucket via the Glue Catalog, and these queries can be exposed through an API Gateway-backed Lambda function.

### Deployment

The wheelerrecommends-scraper is deployed using a Docker image that includes Python, Beautiful Soup, Selenium, and the Amazon Athena ODBC driver. The Dockerfile details the installation of necessary dependencies and the Athena ODBC driver.

The serverless.yml configuration defines Lambda functions (e.g., api for analytics) with event triggers (e.g., httpApi for the analytics API, schedule for scraping). It also specifies IAM role statements to grant necessary permissions for Athena, Glue, and S3 operations.

GitHub Actions workflows (e.g., analytics.yml) manage the build and deployment process, including building the Docker image and deploying it to AWS.

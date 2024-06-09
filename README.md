# Carbon Connect

Welcome to **Carbon Connect**, an app to help users, enterprises, and NGOs reduce their carbon footprints and give insight on their emissions. This README provides an overview of the app and its features

## Table of Contents

1. [Features](#features)
2. [User Personas](#user-personas)
3. [Technologies Used](#technologies-used)
4. [License](#license)

## Features

- **User Survey**: General users can take a survey to calculate their predicted carbon footprint based on heat energy used and fuel consumption.
- **Comparison with Averages**: Users and enterprises can compare their carbon footprint with the average person/enterprise in their country.
- **Survey History**: Users/enterprises can view their past survey results.
- **NGO Matching**: Users and enterprises can match with NGOs based on selected tags and problem areas.
- **Text Similarity Model**: The app uses a text similarity model to suggest matches based on user and NGO bios.
- **Enterprise Emissions Input**: Enterprises can input their emissions data and view matching NGOs.
- **Tag Management**: Both enterprises, users and NGOs can add or delete tags.
- **NGO Management**: NGOs can edit their information, manage tags, and view matches with users and enterprises.

## User Personas

1. **General Users**:

   - Take surveys to calculate carbon footprint.
   - View survey history.
   - Edit user info (country, bio, tags)
   - Match with NGOs based on problem areas.
   - Receive suggestions based on bio similarities.

2. **Enterprises**:

   - Input and see emissions data history.
   - Match with NGOs based on tags.
   - Add or delete tags.
   - Compare emission with average company in country.

3. **NGOs**:
   - Edit organizational information.
   - Add or delete tags.
   - View matches with users and enterprises.
   - View consenting matching users email

## Technologies Used

- **Front End**: Streamlit
- **Backend**: Flask
- **Database**: MySQL
- **Containerization**: Docker (with three containers: front-end, web-api, and mysql_db)

## Running the App with Docker

To run this app using Docker, follow these steps:

### Prerequisites

Make sure you have Docker installed on your machine. You can download Docker from [here](https://www.docker.com/products/docker-desktop).

### Build the Docker Image

First, you need to build the Docker image from the Dockerfile. Navigate to the root directory of the project and run the following command:

**docker compose build**

To stop or down the containers you can use the following commands:

**docker compose down**

**docker compose stop**

To start the containers you can use the following command:

**docker compose up -d**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Thank you for using Carbon Connect!

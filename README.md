# STRATA-VCT (Back-end)

This repository contains the backend code for the StratAssist VCT.It aims to revolutionize the way esports teams are managed and prepared for competitions, providing a competitive edge through detailed analytics and AI-powered insights. The tool not only supports team managers in making informed decisions but also promotes a deeper understanding and appreciation of the strategic aspects of VALORANT esports.. It utilizes Node.js with Express for the web server and integrates with a Python service using LangChain for advanced language processing.

## Getting Started

These instructions will get your copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

- [Node.js](https://nodejs.org/en)
- [npm (Node Package Manager)](https://www.npmjs.com/)
- [Express.js](https://expressjs.com/)
- [LangChain](https://js.langchain.com/v0.1/docs/get_started)

Certainly! A well-organized project structure is crucial for maintainability, scalability, and collaboration, especially when working with technologies like Node.js and Python. Below is a suggested project structure for your StratAssist VCT Backend, which includes both Node.js and Python components:

### Suggested Project Structure

![image](https://github.com/user-attachments/assets/b1cfd504-bde5-4fa9-84a0-8285f3e2adc1)


### Description of Key Components

- **src/**: Contains the source code for the Node.js application, organized into subdirectories for better separation of concerns.
    - **config/**: Stores configuration files, such as configuration for different environments (development, production, etc.) and management of environment variables.
    - **controllers/**: Houses the logic responding to web requests. Controllers parse the incoming requests and respond accordingly, interacting with models or external services as needed.
    - **middleware/**: Contains functions that handle the requests between receiving a request and executing a controller action, such as authentication and error handling.
    - **models/**: If using a database with ORM (Object-Relational Mapping), models define the schema and database interactions.
    - **routes/**: Defines the API endpoints and associates them with controller functions.
    - **utils/**: Utility functions and helpers that can be used across the application.
  - **tests/**: Contains tests for the Node.js application using libraries like Jest or Mocha.
  - **server.js**: The main entry point for the Node.js application which sets up and starts the Express server.

### Installing

A step-by-step series of examples that tell you how to get a development environment running.

#### Setting up the Node.js Server

1. Clone the repository:
   ```sh
   git clone https://github.com/dhrumilp12/STRATA-VCT.git
   cd stratassist-backend
   ```

2. Install NPM packages:
   ```sh
   npm install
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add the following line to specify the port number:
     ```
     PORT=3000
     ```

4. Start the server:
   ```sh
   npm start
   ```

   You should see the following output indicating the server is running:
   ```
   Server running on http://localhost:3000
   ```


### Usage

To test if your installation is correct, navigate to `http://localhost:3000` in your web browser or use a tool like Postman to send a request to the server.

### Contributing

Please read [CONTRIBUTING.md](https://github.com/dhrumilp12/STRATA-VCT/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.


### Authors

- **Dhrumil** - *Initial work* - [dhrumilp12](https://github.com/dhrumilp12)

See also the list of [contributors](https://github.com/dhrumilp12/STRATA-VCT/contributors) who participated in this project.

### License

This project is licensed under the Apache License - see the [LICENSE.md](LICENSE.md) file for details

### Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc


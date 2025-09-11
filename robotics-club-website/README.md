# Robotics Club Website

This project is a website for the school's robotics club, designed to provide information about the club's purpose, the different teams available, and the schedule for upcoming competitions.

## Project Structure

The project consists of the following main directories and files:

- **public/index.html**: The main HTML file that serves as the entry point for the website. It includes links to stylesheets and scripts.
- **src/components**: Contains the React components for the website:
  - **AboutMe.tsx**: Displays information about the robotics club, including its purpose and operations.
  - **Teams.tsx**: Lists the different teams offered by the robotics club, detailing their roles and activities.
  - **Schedule.tsx**: Presents the schedule for competitions, including times and locations.
- **src/App.tsx**: The main application component that imports and renders the AboutMe, Teams, and Schedule components.
- **src/index.tsx**: The entry point for the React application, rendering the App component into the root DOM element.
- **tsconfig.json**: Configuration file for TypeScript, specifying compiler options and files to include in the compilation.
- **package.json**: Configuration file for npm, listing dependencies, scripts, and metadata for the project.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd robotics-club-website
   ```

3. Install the dependencies:
   ```
   npm install
   ```

4. Start the development server:
   ```
   npm start
   ```

5. Open your browser and go to `http://localhost:3000` to view the website.

## Overview

The Robotics Club website aims to engage students by providing them with essential information about the club's activities, teams, and competition schedules. It serves as a platform for communication and organization within the club, fostering a sense of community among members.
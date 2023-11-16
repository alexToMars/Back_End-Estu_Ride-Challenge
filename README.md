# Backend Coding Challenge: Simple Reservation API

## Overview
Develop a basic REST API for a simple booking system using either FastAPI or Django. The API should support creating, viewing, updating, and deleting reservations. Additionally, you'll need to write tests to verify the functionality of your API endpoints.

---

## Requirements

### API Endpoints
- `POST /reservations`: Create a new reservation.
- `GET /reservations`: List all reservations.
- `GET /reservations/{id}`: Retrieve a specific reservation by ID.
- `PUT /reservations/{id}`: Update a specific reservation by ID.
- `DELETE /reservations/{id}`: Delete a specific reservation.

### Data Model
- Include fields like `id`, `name`, `date`, and `number_of_guests` in the Reservation model.

### Validation
- Implement basic validation (e.g., no past dates, valid number of guests).

### Testing
- Write tests to validate the functionality of each endpoint.

### Documentation
- Document your API (use FastAPI's built-in feature or Django REST framework documentation tools).

---

## Instructions

- **Choose Your Framework**: You can choose either FastAPI or Django for this project.
- **Set Up Your Project**:
  - For FastAPI, set up a virtual environment and install FastAPI and Uvicorn.
  - For Django, set up a project using Django and Django REST framework.
- **Develop the API**:
  - Implement the required endpoints.
  - Use an in-memory database or a simple SQLite database for simplicity.
- **Write Tests**:
  - Ensure each endpoint is tested for basic functionality.
- **Document Your API**:
  - Provide clear documentation for your API endpoints.

---

## Deliverables

- Source code with all the implemented API endpoints and data models.
- Test files for your API.
- A README file with:
  - Instructions on how to set up and run your project.
  - A description of the API endpoints and their functionalities.

---

## Evaluation Criteria

- Functionality: All endpoints should be functional.
- Code Quality: Clean, readable, and well-organized code.
- Testing: Comprehensive and effective tests.
- Documentation: Clear and useful documentation.
- RESTful Principles: Adherence to RESTful practices and design.

---

## Steps to Fork and Share the Repository
1. Fork the Repository:

    - Go to the GitHub repository page.
    - Click the 'Fork' button on the top right corner of the page. This creates a copy of the repository in your GitHub account.

2. Clone the Forked Repository:

    - On your forked repository page, click the 'Code' button and copy the URL.  
    - Open your terminal or command prompt.  
    - Run git clone [URL] to clone the repository to your local machine.

3. Implement the Challenge:

    - Make the necessary changes and improvements to the codebase as per the challenge requirements.  
    - Include the steps for the reviewer to run your application, you can delete or modify the content of this README file to include instructions.

4. Push Changes:

    - After making your changes, commit them and push them back to your forked repository.
    - Use git add ., git commit -m "Your commit message", and git push origin main.

5. Share Your Work:

    - Once you've pushed your changes, share the link to your forked repository as your submission for the challenge.

---

## Submission
Share the link to your forked repository as your submission.

---

## Note

- This project is for educational and assessment purposes. No real-world transactions are processed.
# Publisher-Subscriber Notification System

## Overview

This project implements a basic Publisher-Subscriber Notification System using Flask.

## API Endpoints

1. **Subscribe**
   - **URL**: `/subscribe`
   - **Method**: POST
   - **Request Body**:
     ```json
     {
         "topicId": "topic1",
         "subscriberId": "subscriber1"
     }
     ```
   - **Response**:
     ```json
     {
         "message": "Subscriber subscriber1 subscribed to topic topic1"
     }
     ```

2. **Notify**
   - **URL**: `/notify`
   - **Method**: POST
   - **Request Body**:
     ```json
     {
         "topicId": "topic1"
     }
     ```
   - **Response**:
     ```json
     {
         "notifications": [
             "Notification sent to subscriber subscriber1 for topic topic1"
         ]
     }
     ```

3. **Unsubscribe**
   - **URL**: `/unsubscribe`
   - **Method**: POST
   - **Request Body**:
     ```json
     {
         "topicId": "topic1",
         "subscriberId": "subscriber1"
     }
     ```
   - **Response**:
     ```json
     {
         "message": "Subscriber subscriber1 unsubscribed from topic topic1"
     }
     ```

## Postman Collection

The Postman collection can be found in the repository as `PubSubSystem.postman_collection.json`.

## Running Locally

To run the application locally:
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. Access the endpoints at `http://localhost:5000`

## Hosting

The application is hosted on Heroku and can be accessed 

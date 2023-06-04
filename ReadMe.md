# Django API Template

This is a Django API Template that you can use to quickly spin up your `API` development.

The files lie under the `project` folder.

This template gives you the basic setup with:

- Auth - customauth app
- Account - account app
- MainApp - mainapp app

These apps contains the basic setups ie

## Auth
Provides you with:

- Email/Account verification
- Login
- Password Reset
  
    - Requesting password reset
    - Validating password reset token
    - Resetting the password using the confirm URL

## Account
This app has `Profile` as model and you can expand the model to add more properties and also edit the serializer class 
to take thos properties into account

To update an account, you can also pass the `profile` being nested and it will as well update it.

The `serializer` class inherits nested model class and therefore, you can take advantage of that to do a single query
from your frontend to update your profile too.

> To Learn more about the api, kindly use the provide `postman json` in order to see all the endpoints and how to use 
> them.
> 
> If the environment is not created, create an `environment` and give it: 
>   ```
> BASE_URL: localhost:8000
> TOKEN: some token value from login

Anyways, `Hooray`


> Coding is more fun when debugging becomes difficult
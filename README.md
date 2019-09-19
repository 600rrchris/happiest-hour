# Title

[Happiest ](https://deaf-friendly.herokuapp.com/posts)

## Overview
 A place where you can search for deaf-friendly businesses in your area or share your consumer experience and insights as deaf, deafblind, and hard of hearing individuals, friends/family of the deaf and those with a special interest in creating a deaf-friendly world.
  
The aim is to promote deaf-friendliness in your community via awareness and feedback.

## Entity Relationship Diagram
![image description](../master/public/images/erd.jpg)

## Wireframe

![image description](../master/public/images/wireframe.jpg)

## Screenshots

![image description](../master/public/images/home.jpg)

![image description](../master/public/images/business.jpg)

![image description](../master/public/images/reviews.jpg)

![image description](../master/public/images/form.jpg)


## Pseudocode
1. Set up Oauth verification 

2.  Set up models with user, post, and review schema.

3. Assign properties within schemas. 

	User properties include:
	
		Name
    	Email
    	Avatar
    	Google ID
	
	Post properties include:
	
		Name
		Location
		Review
	
	Review properties include:
	

4. Require models in routes. 

5. Create index view, controller and routes. 

6. Show posts, create and add new post.

6. Set routes to get post put edit and delete.  

7. Set controller to render index. Set controller to render new. Set controller to post new to index. Set controller to get show. Set controller to create post. 

8. Set route to delete selected id. Set controller to delete selected id.

9. Set route to get to edit view. Create edit view. Set controller to get to edit view. Set route to put update on id.

## User Stories

As a user, I can log in via Google authentication. 

As a user, I can create a post for any existing business and identify it by name and location.

As a user, I can find existing posts, left by previous users, for the business I am interested in.

As a user, I can read reviews left by previous users.

As a user, I can rate the business from a scale of one to five stars. 

As a user, I can check off a set of accomadations offered at said business.

As a user, I can leave a comment of my experience with that business. 

As a user, I can edit or delete my review.


## Technologies Used
HTML, CSS, Javascript, Express, Node.js, MongoDB, Mongoose, Materialize, Heroku

## Stretch Goals

Change number rating to star rating

Authorization

## Next Steps

Implement Google Maps API

Implement search feature
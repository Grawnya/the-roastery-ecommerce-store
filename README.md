# The Roastery E-Commerce Store

## Introduction

Welcome to the coding repository dedicated to the "The Roastery"'s Ecommerce Store; A website which not only provides details about a made up coffee ecommerce website, but also allows users to buy coffee from the website.

The project is very relevant as online shopping is becoming increasingly popular, therefore, people are keen to buy everything they used daily including the coffee for their coffee machines or french presses. The flexibility of the website ensures that its design can be utilised for any ecommerce store that requires the user to purchase the products with a card in advance of receiving them.

[Visit the Website Here](https://the-roastery-1abb0b0a677e.herokuapp.com/)

[Visit the Project's GitHub Repository Here]( https://github.com/Grawnya/the-roastery-ecommerce-store)

![Responsive Image](documentation/responsive_image.png)

# Table of Contents

* [UX](#ux "UX")
	* [Strategy](#strategy "Strategy")
    	* [Purpose](#purpose "purpose")
   		* [User Stories](#user-stories "User Stories")
   	        * [For This Sprint](#for-this-sprint "For This Sprint")
   	        * [For Future Sprints](#for-future-sprints "For Future Sprints")    
	* [Scope](#scope "Scope")
		* [Sprint 1](#sprint-1 "Sprint 1")
		* [Sprint 2](#sprint-2 "Sprint 2")
    	* [Future Sprints](#future-sprints "Future Sprints")
	* [Structure](#structure "Structure")
    	* [Project Applications](#project-applications "Project Applications")
    	* [Project Database](#project-database "Project Database")
		    * [Blog Model](#blog-model "Blog Model")
		    * [Order Model](#order-model "Order Model")
		    * [OrderItem Model](#orderitem-model "OrderItem Model")
		    * [Product Model](#product-model "Product Model")
		    * [Favourites Model](#favourites-model "Favourites Model")
		    * [WebsiteUser Model](#websiteUser-model "WebsiteUser Model")
		    * [OurStory Model](#ourstory-model "OurStory Model")
	* [Skeleton](#skeleton "Skeleton")
		* [Wireframes](#wireframes "Wireframes")
	* [Surface](#surface "Surface")
        * [Font](#font "Font")
	    * [Icons](#icons "Icons")
        * [Colours](#colours "Colours")
	    * [Responsive Screens](#responsive-screens "Responsive Screens")

\
&nbsp;

# UX
User Experience of UX focuses on how accessible the website is to the user and it’s ease of use, which is pivotal the website’s success.

Therefore, the UX aspect of the project can be broken down into 5 Planes:
* The Strategy Plane
* The Scope Plane
* The Structure Plane
* The Skeleton Plane
* The Surface Plane
\
&nbsp;

## Strategy
In order to ensure the project aligns with these planes, it is vital to keep the target audience at the forefront at all times.

The target audience consists of:
* Age: 25-45 years old
* Location: Built up cities
* Income Level: Middle - high income i.e. have extra monthly disposable income.
* Occupation: Working professionals, students, and coffee industry workers
* Lifestyle: Coffee fanatics who value good quality coffee and actively seek out different coffee roasts, blends, and flavours.
* Interests: They would be more interest in high quality coffee than the average person on the street. The savour coffee rather than drink it quickly on the go as a form of energy, therefore, appreciating coffee culture, fair trade practices and sustainable practices. They are therefore willing to pay a bit more for a cup of coffee. They follow coffee blogs and social media accounts – particularly Instagram.

As a result, users will expect:
* A website with easy navigation and a logical progression to its flow.
* Plenty of information with regards to various coffees from around the world.
* The ability to order the coffee via an easy checkout process.

\
&nbsp;

### Purpose
The purpose of this website is to promote a coffee ecommerce store with the help of a fun blog and allow users to buy coffee from around the world.
\
&nbsp;

### User Stories
#### For This Sprint
| id  |  Content | Label |
| ------ | ------ | ------ |
| [1](https://github.com/Grawnya/the-roastery-ecommerce-store/issues/1) | As a user, I can navigate through the website easily so that I can get more information about the coffees available to buy. | Must Have |
| [2](https://github.com/Grawnya/the-roastery-ecommerce-store/issues/2) | As a user I can get information regarding the coffee company's story and the coffee they sell so that I can decide whether I want to purchase from them or not. | Could Have |
| [3](https://github.com/Grawnya/the-roastery-ecommerce-store/issues/3) | As a user, I can find the coffee company's social media accounts so that I can keep up-to-date with any news. | Must Have |
| [4](https://github.com/Grawnya/the-roastery-ecommerce-store/issues/4) | As a user, I can easily use the navbar to navigate the website so that I can find all relevant content. | Must Have |
| [5](https://github.com/Grawnya/the-roastery-ecommerce-store/issues/5) | As a user, I can easily reach the home page in case I get an error so that I am not stuck on an error page and have to select the back button. | Must Have |
| [6](https://github.com/Grawnya/the-roastery-ecommerce-store/issues/6) | As a user, I can access the website on mobile, tablet or larger screens so that I can view the information regardless of the device. | Must Have |
| [7](https://github.com/Grawnya/the-roastery-ecommerce-store/issues/7) | As a user, I can view all coffee products that are available to purchase. | Must Have |
| [8](https://github.com/Grawnya/the-roastery-ecommerce-store/issues/8) | As a user, I can filter all the coffees by the different categories so that I can view what I prefer. | Should Have |
| [9](https://github.com/Grawnya/the-roastery-ecommerce-store/issues/9) | As a user, I can find all the product details so that I can decide whether I want to add it to my shopping bag. | Must Have |
| [10](https://github.com/Grawnya/the-roastery-ecommerce-store/issues/10) | As a user, I want to preview my order so that I can make a final selection before I purchase it. | Must Have |
| [12](https://github.com/Grawnya/the-roastery-ecommerce-store/issues/12) | As a user, I can purchase the items in my shopping bag by card so that I can successfully buy them. | Must Have |
| [13](https://github.com/Grawnya/the-roastery-ecommerce-store/issues/13) |As a user, I can register or log in so that I can manage my orders. | Must Have |
| [14](https://github.com/Grawnya/the-roastery-ecommerce-store/issues/14) | As a user, I can see if I am logged in so that I can easily log out or log in. | Must Have |
| [15](https://github.com/Grawnya/the-roastery-ecommerce-store/issues/15) | As a user, I can edit my user details when logged in so that I can ensure that my details are up-to-date and can be used for shipping and billing. | Should Have |
| [16](https://github.com/Grawnya/the-roastery-ecommerce-store/issues/16) | As a user, I can enter my email to sign up the coffee company's newsletter to keep up-to-date with any news. | Could Have |
| [17](https://github.com/Grawnya/the-roastery-ecommerce-store/issues/17) | As a site owner/admin, I can log in so that I can access the website's backend. | Must Have |
| [18](https://github.com/Grawnya/the-roastery-ecommerce-store/issues/18) | As a site owner/admin, I can add, edit and delete items from the store so that I can ensure that the website is up-to-date. | Must Have |
| [19](https://github.com/Grawnya/the-roastery-ecommerce-store/issues/19) | As a site owner/admin, I can promote my facebook page so that I can try to increase traffic to my store. | Should Have |
| [20](https://github.com/Grawnya/the-roastery-ecommerce-store/issues/20) | As a site owner/admin, I can implement Search Engine Optimisation tactics so that I can try to increase traffic to my store. | Should Have |

\
&nbsp;

#### For Future Sprints
| id  |  Content | Label |
| ------ | ------ | ------ |
| [11](https://github.com/Grawnya/the-roastery-ecommerce-store/issues/11) | As a user, I want to receive an order confirmation via email so that I know that my order went through. | Should Have |

\
&nbsp;

## Scope
In order to ensure that the current sprint (i.e. the elements required for the current project submission) are completed, the focus was as follows:
\
&nbsp;

### Sprint 1
This sprint focuses on the “Must Haves” and the marking criteria:
* A homepage with basic details on the ecommerce website and the coffee available to buy.
* Navbar enabling the user to easily navigate through the website.
* The ability of the user to login and create a profile.
* Applications that allow the user to put coffee into their shopping basket and place that order.
\
&nbsp;

### Sprint 2
This sprint builds on Sprint 1:
* Integrate the Stripe API with the website to successfully make the order.
* Allow the user to get confirmation of order in the profile page and via a notification.
* Creating a blog page to allow the user to view relevant and engaging content.
* Adding extra details to the blog page such as allowing the user to select their favourite roast.
\
&nbsp;

### Future Sprints
Elements to add to the site in the future:
* Incorporate additional email confirmation.
* Use profile data to create a data model which can influence the best types of coffee to advertise, promote and sell.
\
&nbsp;

## Structure
Having a well-worked out project structure ensures that creating the project would occur in a more logical manner and the sprint steps can be closely followed. Therefore, the content was broken into applications to account for the various tasks and into database tables to organise how the data obtained from the user will be stored.
\
&nbsp;

### Project Applications
For this project, 6 applications were created:
* blog – To provide the user with interesting coffee centric content and allows the website owner to share interesting information and offers with the user.
* checkout – To purchase the items in the shopping bag and place an order successfully.
* home – To provide details regarding the coffee ecommerce store and encourages users to go to other parts of the website. A solely static app with no models.
* products – To view the available products on the ecommerce store and to allow the website owner to add, edit or delete existing products. 
* profile_app – To let the user put in personal details for a faster checkout if the checkout form is prepopulated and to provide useful information for the website user re demographic, favourite coffee etc.
* shopping_bag – To place products inside and therefore can ready a user’s final order.

\
&nbsp;

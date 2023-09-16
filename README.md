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

### Project Database
7 tables/models can be found in total throughout the project, which enable the user to create the profile required, successfully order coffee and read coffee based content. The website owner can also readily add, edit and delete content within the website. The schematic below provides the relationship between all of the tables within the project.

![Database Tables](documentation/database_schematic.png)
\
&nbsp;

#### Blog Model
The Blog model is used by the website owner to create, edit and delete relevant blog content for the website. These blogs provide either relevant information regarding “The Roastery” ecommerce store or fun and interesting coffee centric posts, which encourage the user to buy coffee.

It can be broken down as follows:
* `heading` - Heading of the blog post.
* `blog_body` - Body of the blog post.
* `created` - Date of when the blog was created.
\
&nbsp;

#### Order Model
The Order model is used to record the order made by a website user. It incorporates all relevant info about the user and what they have specifically ordered.

It can be broken down as follows:
* `order_id` - Unique order ID that is created when the order is made.
* `profile_id` - A Foreignkey to link the order to a profile if it exists.
* `full_name` - Full name of user.
* `email` - User's email.
* `phone_number` - User's phone number.
* `street_address1` - User's first address detail.
* `street_address2` - User's second address detail.
* `town_or_city` - User's town or city they live in.
* `county` - User’s county location.
* `postcode` - User's postcode.
* `country` - User's country location.
* `order_date` - Date that the order was made.
* `items_total` - Order product value.
* `delivery_cost` - Order delivery cost.
* `final_total` - Final total of the entire order i.e. `items_total` + `delivery_cost`.
* `original_shopping_bag` - User's first shopping bag to ensure that a duplicate.
* `stripe_pid` - Stripe payment intent.
\
&nbsp;

#### OrderItem Model
The OrderItem model looks at the specific items within the order and uses them to log how much they add to the overall order.

It can be broken down as follows:
* `product_id` - Product foreign key.
* `order_id` - Order foreign key.
* `quantity` - The number the user has ordered.
* `item_total_price` - Total price that the user has to pay for that item.
\
&nbsp;

#### Product Model
The Product model provides information for available product on the ecommerce store and is used to influence the product filter on the website.

It can be broken down as follows:
* `sku` - Unique number to represent the product.
* `name` - Name of product.
* `roast` - Roast type.
* `location` - Continent where the coffee is found.
* `origin` - Country of origin.
* `bag_100g_USD` - Coffee cost in USD per 100g bag. 
* `rating` - Coffee rating out of 100.
* `review` - Description of the coffee.
* `image` - Image of the coffee.
\
&nbsp;

#### Favourites Model
The Favourites model allows the user to put extra info about themselves into the profile page which can later be used to influence the marketing strategy with targeted ads.

It can be broken down as follows:
* `website_user` - WebsiteUser foreign key.
* `birthday` - User’s birthday.
* `coffee_type` - User’s favourite coffee origin.
* `roast` - User's favourite roast.
\
&nbsp;

#### WebsiteUser Model
The WebsiteUser model is used to obtain more information from the user than just their username, email and password. It provides relevant information with regards to the person who made the coffee purchase and can be used to influence business decisions.

It can be broken down as follows:
* `website_user` - Unique username that user has chosen when registering.
* `profile_full_name` - First name of user.
* `profile_email` - User's email that they didn't use to login.
* `profile_phone_number` - User's phone number.
* `profile_street_address1` - User's first line of their street address.
* `profile_street_address2` - User's second line of their street address.
* `profile_town_or_city` - User's town or city.
* `profile_county` - User’s county.
* `profile_postcode` - User's postcode.
* `profile_country` - User's country.
\
&nbsp;

#### OurStory Model
The OurStory model is used to show the timeline of “The Roastery” and can be edited by the superuser/website’s admin.

It can be broken down as follows:
* `event_id` - Unique event ID.
* `date_occurred` - When the event occurred.
* `event` - Event name.
\
&nbsp;

## Skeleton
The skeleton provides a broad initial idea that is further refined and built on. It enables the creation of a plan that aligns with the requirements of the [user stories](#user-stories "User Stories") and the [sprints](#scope "Sprints"). Therefore, wireframes can be created to act as a design aid and provide the website skeleton.
\
&nbsp;

### Wirefames
[Balsamiq](https://balsamiq.com/wireframes/ "Balsamiq") was used to create the conception for the website appearance and flow. I initially created a mobile version in-line with my mobile-first approach and then followed with a medium and large screen version. The key is to make sure that the website is responsive on various screens.

Basic wireframes can be found below (Note that these vary slightly from the final website design):

#### [Home Page](documentation/home-page.png "Home Page")
#### [Products Page](documentation/products-page.png "Products Page")
#### [Blog Page](documentation/blog-page.png "Blog Page")
\
&nbsp;

## Surface
The surface plane refers more to the aesthetics and the interface itself. It’s important to select the right colour, font and icons for your website to ensure it is as appealing as possible.
\
&nbsp;

### Font
To deviate from the standard fonts, [Google Fonts](https://fonts.google.com/ "Google Fonts") was used to obtain a font style, which would be reminiscent of a “hipster” yet slightly sophisticated coffee ecommerce website.
* [Roboto Slab]( https://fonts.google.com/specimen/Roboto+Slab?preview.text=the%20roastery&preview.text_type=custom&query=rob) fulfilled the criteria for the logo as the primary font, due to its readability and flair.
* [Quicksand]( https://fonts.google.com/specimen/Quicksand?query=quicksand) is used as the secondary font due to its clean style that matches the colour scheme well.
\
&nbsp;

### Icons
In order to obtain some icons for the website, [Font Awesome](https://fontawesome.com/ "Font Awesome") will be utilised. Icons were used to prompt the website owner to edit or delete items.
\
&nbsp;

### Colours
To select the colour palette for the project, I was inspired by a [Pinterest Post](https://www.pinterest.com/pin/69946600455034413/) that I came across with mellow coffee colours and complimenting shades. When checking the contrast of the colours on [Web AIM](https://webaim.org/resources/contrastchecker/ "Web AIM"), the khaki with the orange passed, as well as the coffee and beige match up. Therefore the following colours were selected for the project where:

*  #354129 (also known as --khaki) is used for the background of the navbar, as well as the font for many aspects of the website.
*  #8b593e (also known as --coffee) is used for various buttons.
*  #d0d3cc (also known as --beige) is used for the font of the navbar of the website and for a couple of buttons.
*  #d8d6d7 (also known as --light-grey) is used for the background of the website.
*  #ed9112 (also known as --orange) is used often for buttons in their hover state and hover state font on the home page.

![Colours](documentation/colours.png)
\
&nbsp;

### Responsive Screens
The website will be built for a small mobile screen of width 320px and then will also meet the requirements for a medium/tablet, large and extra-large screen, as shown in the table below.

| Screen Size   | Breakpoint |
| -----------   | ---------- |
| small/mobile  |    320px   |
| medium/tablet |    768px   |
| large         |   992px    |
| extra-large   |   1400+px  |

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;


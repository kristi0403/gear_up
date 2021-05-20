# Gear Up / Ecomerce App

The brief was to create a web application using django that allows users to buy products from an ecomerce store.
The products are to be stored in a database which can be viewed by a user in the website or can
filtered using the categories or platforms or special categories.

As the page is loaded you are introduced to the home page which consists of the page logo on the left top corneer ,
the search bar in the middle of the nav bar , and 3 buttons :
* Home
* My acount 
* Basket
Underneath this are the 5 main options for the products. So you have:
* All products    * PS4    * Xbox 1  * New Arrivals    * Clearence
Every each one of them opens the subcategories for each one of them .
* All Games:
    - By price(all games by price in ascending order),
    - By rating (all games by rating in a desc order),
    - By category (all games sorted by category in adc order )
    - All games (displays all games)
* Ps4 :
    - Has all the game genres for the ps4 platform including:
        1) action-adventure
        2) car-race
        3) fps (first person shooter)
        4) sport
        5) horror 
        6) platforma
    - And an option to display all ps4 games .
* Xbox 1 :
    - Has the same game categories as the ps4 but related with xbox platform 
    - And an option to display all the xbox one games available
* New Arrivals :
    Direct filter for the games that are put on the database a recently added 
* Clearence :
    Filter for games that have been put in the database as low price de to Clearence
After the product categories a carousel is displayed showing 3 pictures one for new titles one for clearence and one for deals .Each one of them
has a button that can take you to the category the image is showing . At the bootom of the carousel is also a button saying "Shop Now" that
can take you to the all products page .
At the bottom of the page is the footer tat contains :
- A quote
- Links to gaming pages 
- Adress of the store (just my adress at the moment as the page is still in development)
- Social media link (at the moment the just take you to the homepage of the social medias as the page is not used yet for comercial purpuse)
As you clik on the shop now you are directed to the all products page where you can use the main categories navigations to take you in what 
area platform on genre you desire and also use the sort box to sort them by price or rating or name inside the category you are in .
Every page will display number of products 12 and you can use the pagination at the botom to go to the next page .
There is also a back to top button to take you back at the head of the paga for you not to stay scrolling . The footer and the navbar ar available.
When a user selects an image of a product it will open the products page showing the image , rating ,title ,price and 2 buttons one to add it to the bag 
and another to go back shoping. Also you have the option to increase the quantity of the product you are buying.
* The superuser will allso have 2 extra options one to delete item that can make him delete the item from the products and one to edit .
When you press the add to basket button the item moves to the basket the basket changes colour to white and shows the sum of the products cost that are in it
and a toast will show saying that the item was succesfully added tot he basket and will show an image of the item , price and how much you need 
to spend so you have a free delivery . You have the option to go to the security checkout and pay or press the x and continue navigating.


* Recipes Name
* An image
* Recipes description
* Preparation time
* Cooking time
 and 3 buttons :
    * view
    * edit
    * delete
The users that are visitors do not have an acount or are not loged int can access only the view button 
and by pressing it can open the recipe page where are shown the ingredients and the preparation steps.
The users that have an acount and are logged in can view all the recipes but can only delete and edit
the recipes done by them.
After the card grid system is the footer which includes a quote and media link that at the moment just 
point to the home page of the media links when pressed as no media links for the app still exist.
After seeing the homepage there is the log in and the register button.
By pressing the log in you will be redirected to the log in page where you have to options log in or register.
If you have an acount just press the log in instead button at the bottom of the log in form.
If you don't have an acount just go for register and you can create a new acount witht the username and password criterias.
When you log in you are redirected to the profile page, where it shows you the user profile name, profile picture and the 
recipes made by the user, you in this case.Than you have new recipes that you can press to create new recipes.
The create new recipe template comes with text filds of ingredients , recipes description, recipe name, preparation steps,
cooking time and preparation time.
Everytime you pressed the edit buton you are redirected to the edit recipe page where you have the elements for the curent 
recipe from the database and you chose what you what to change. after presing edit a message flashes telling changes recipe updated 
than you can press done to be redirecter to the recipes homepage.
You also have the delete option which you can use to delete the recipe that will be deleted from database as well.
Users can use even the search bar to write text to find in the matching recipes name and description.

## UX
  The app is in general for avery audience because it does not contain any harmful content or adult content .
  If i would take int consideration four different users and how they may behave when they inconter the app or is it useful to them.
1) So first we have a person who is interested to try learning how to cook. 
   The app itself consent of recipes made by everyday people so most of the recipes are not really hard to try to learn them.
2)The second user might be a person that likes to learn new recipes and store them somewhere.
    The app has the profile with the collection of recipes that are made by the user.
3)A person that wants to it someting but cant make up hist mind.
    With only on writing "pasta" on the search and all the pasta recipes will show up to you.
    More easily to chose when you have more than 1 to look for.
4)The users can edit their recipes without needing to delete the entire recipe only changing particular components .
5)A person that is entusiastic for cooking and want to shere their love and ideas with the rest of the world.


 ## Design process
 Above are the first ideas of the webpage shown in wireframes
![New Wireframe 1 (1)](https://user-images.githubusercontent.com/63249988/113645217-62a5a280-967e-11eb-8241-d1d4a498cb20.png)
![New Wireframe 1 (2)](https://user-images.githubusercontent.com/63249988/113645221-646f6600-967e-11eb-9e08-1deabab6ea18.png)
![New Wireframe 1 (3)](https://user-images.githubusercontent.com/63249988/113645223-646f6600-967e-11eb-9bba-8fea5cfe7360.png)
![New Wireframe 1](https://user-images.githubusercontent.com/63249988/113645227-6507fc80-967e-11eb-9828-ee41ec5a3067.png)
![New Wireframe 2 (1)](https://user-images.githubusercontent.com/63249988/113645229-65a09300-967e-11eb-846a-9f975ee72521.png)
![New Wireframe 2 (2)](https://user-images.githubusercontent.com/63249988/113645231-65a09300-967e-11eb-93cc-3e1cf83d945e.png)
![New Wireframe 2 (3)](https://user-images.githubusercontent.com/63249988/113645233-66392980-967e-11eb-93f4-928ced236b75.png)
![New Wireframe 2 (4)](https://user-images.githubusercontent.com/63249988/113645234-66392980-967e-11eb-8279-8f1c3f8e9630.png)
![New Wireframe 2](https://user-images.githubusercontent.com/63249988/113645235-66d1c000-967e-11eb-9121-a0e1fa7cde8f.png)
![New Wireframe 3](https://user-images.githubusercontent.com/63249988/113645236-66d1c000-967e-11eb-8552-a4245e0dcc5c.png)
![New Wireframe 4](https://user-images.githubusercontent.com/63249988/113645238-676a5680-967e-11eb-9996-a53096a73051.png)

how the actual app was finished

![Screenshot 2021-04-05 at 23 54 40](https://user-images.githubusercontent.com/63249988/113645708-4fdf9d80-967f-11eb-8b55-9876a3bd0b03.png)
![Screenshot 2021-04-05 at 23 55 00](https://user-images.githubusercontent.com/63249988/113645713-51a96100-967f-11eb-9be5-f0f7c1b49049.png)
![Screenshot 2021-04-05 at 23 54 37](https://user-images.githubusercontent.com/63249988/113645716-5241f780-967f-11eb-876a-0dbc36b0029b.png)
![Screenshot 2021-04-05 at 23 54 48](https://user-images.githubusercontent.com/63249988/113645720-52da8e00-967f-11eb-843f-41e7ed5ec719.png)
![Screenshot 2021-04-05 at 23 55 05](https://user-images.githubusercontent.com/63249988/113645723-540bbb00-967f-11eb-9454-8df510ca4ca2.png)
![Screenshot 2021-04-05 at 23 55 48](https://user-images.githubusercontent.com/63249988/113645727-54a45180-967f-11eb-8fd7-38e89ef7d9bb.png)
![Screenshot 2021-04-05 at 23 54 45](https://user-images.githubusercontent.com/63249988/113645730-55d57e80-967f-11eb-9a3d-931c12fcd9e5.png)

The images dispaly the app on pc screen tablet and phone both landscape and portrait


Colour Scheme

I through to use more the background image to look more like the citchen with the marble and the ingredients.
Also the main color used for the page is orange but in different shades using the lighten atribute.


Typography

The main font family used is "Roboto" for the buttons and  'Gloria Hallelujah' for the titles.

## Features
The page is been programed to work in 3 different screen sizes.
1)PC
2)Tablet
3)Smartphone
The elements are responsible designed to suit the changes made to the screen.

1. Navbar - Consist of the name which returns the user to home page everytime pressed.There are also links to home, profile, new recipe,
   log in, log out.
2. Home - The homepage consist of 4 sample recipes.
   Shows the user "All Recipes" from ALL users which have been entered on the site.
   The user can then filter or browse through the recipes.
    The can view more information on each recipe by selectign the "View" link which delivers the user to the "View recipe" page.
3.  My Recipes - kocated on the profile,  provides the user with the recipes that they have added themselves.
    The user's recipes can be edited and deleted by using the buttons displayed under the recipes.
4.  Login/profile - When first selected the user will be prompted to create a username to login to the application so that they can add recipes to the database.
    Once logged in the user will be presented with their Profile which provides all of their recipes.
5.  Social Links - Provides users with links to the website social media pages.
    (Links NOT LIVE as this project is for learning purpose ).


 //Features to add//
1. Make users abble to add their profile picture as for the moment the app is using a default one.
2. Make users abble to add photos taken by them to their recipes as for the moment the app is using a default one.
3. Make users abble to add videos made by them to to show the preparation steps of the recipes.


## Technologies Used

Languages Used
-HTML : divs are used more to group different section 
-CSS3 : used to style the html elements
-JS : used to start some of the elements of materialize
-Python : all the logic of retriving elements from database or puting elements on the database or login in checking Users,
register, loging, editing recipes, geting recipes, geting user recipes, are done using python.

Frameworks, Libraries & Programs Used

Bootstrap 4.4.1:
(Bootstrap was used to assist with the responsiveness and styling of the website.)

Font Awesome:
(Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.)

Flask: as python micro-framework.

Git
(Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.)

Materiaalize CSS

Heroku
This project uses Heroku, a web hosting service that supports Python applications, for final project deployment.

GitHub
This project uses GitHub, for version control and final project backup.

mongoDB as database to store the recipes and the users.


## Testing
* Add Recipe Page:

    * Go to the "New Recipe" page
    * Try to submit the empty form and verify that the recipe will not submit without a RECIPE NAME.
    * Try to submit the empty form with no description and verify that the recipe will not submit without a RECIPE DESCRIPTION.
    * Try to submit the empty form with no category and verify that the recipe will not submit without a CATEGORY SELECTED.
    * Try to submit the empty form with no name and verify that the recipe will not submit without a RECIPE NAME.
    * Try to submit the empty form with no preparation and verify that the recipe will not submit without a RECIPE PREPARATION STEPS.
    * Try to submit the empty form with no cooking time and verify that the recipe will not submit without a RECIPE COOKING TIME
    * Try to submit the empty form with no preparation and verify that the recipe will not submit without a RECIPE PREPARATION TIME.
    * Try to submit the empty form with no ingredients and verify that the recipe will not submit without  RECIPE INGREDIENTS.

* Log In Page:

    * Try to loog in when no register and verify that will not login without registe.

* Register Page:
    * Try to register when already have acount and veryfied that cant register if already registered.

* Edit/delete recipe:
    * Try to edit/delete when no created by you and verified you can only edit them ore delete them if they were creeated by you


The app was tested on iphone 7 and iphone 11 and also using google chrome inspect on all the devices available on the inspector.
Both landscape and portrait doesn't seem to have any problem on responsiveness only in some screens the recipe cards move e bit more on
the left that it should .

## Bugs
When i had the first add recipe loyout i had the ingridients an array that included 2 arrays one ingridients name and one ingridients quantity.
When retriving the data from the database they showed as 2 arrays of elements and i couldn't slice them or join them.

I changed the data type and at the moment they are presented as strings.

## Deployment

Used git add to add files and after that git commit to coment the files addeted and deleted and git push 
at the end to move the files to the github pages.
Heroku was conected to github throug github pages so every time you push updates on Heroku aswell

The final project deployment is been done by Heroku:
    1.The following section describes the process to deploy this project to Heroku.
    2.Ensure all required technologies are installed locally, as per the requirements.txtfile.
    3.Via Linux Terminal, login to Heroku, using 'heroku login' command. Input Heroku login details.
    4.Create new Heroku app, using 'heroku apps:create appname' command.
    5.Push project to Heroku, using 'push -u heroku master' command.
    6.Create scale, using 'heroku ps:scale web=1' command.
    7.Login to Heroku and select newly created app.
    8.Select settings. Select ‘Reveal Config'. Add IP 0.0.0.0 and PORT 5000.
    9.From 'More' menu on the top right, select 'Restart all dynos'.
   10.View app: In settings, select Domain URL, NOT Git URL to view your hosted application.
   11.Upon successful deployment Heroku will give you the URL that is hosted your app


## Credits

### Content

    * The recipes were obtained from bbcgoodfood.com

### Media

    * The photos used for the recipes and the profile were obtained from google images

## Acknowledgements

    - My Mentor for continuous helpful feedback.
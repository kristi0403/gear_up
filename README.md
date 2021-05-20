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
once to the bag you can remove the item you have selected or update the quantity or keep shoping or just check out .
If you go to the checkout it will ask for he adress and the card number to make the payment .
After everything is done . it is going to show you a briefing of the order summary and a toast pop up telling that the order was succesfully proceeded.
From there you have a link where you can enter to check out the latet deals .


The user as visitor can look throug the page , register if they want by going to my profile and pressing register or continue as a guest and 
check out as a guest without opening an account.
If you have an acount you can view the orders history from your profile as well as update the shipping information so you dont have to put them every
time you do a purchase.If they already have an acount and want to log in . They just press log in instead of the register button in the my profile tab.


The user as superuser or owner has the abillity to add , delete and edit the products , through a form that can be accesed by going to my 
profile and pressing manage products . He also has the access to the edit or delete buttons at each product to make changes to the image , 
price rating descripton category etc.
If a non image product is being added to the page. A non image placeholder photo is going to to take the place of the missing photo.

Besides the categories users ca even search for games by writing text in the search box matching description name or genre or platform .

## UX
The app is in general for avery audience because it does not contain any harmful content or adult content . Even if it is
navigated by a person under 18 and might have games for adult audience , the fact that the games can be purchased only by card payment 
make's it require a consent of an adult to use the card.
If i would take into consideration four different users and how they may behave when they inconter the app or is it useful to them.
- 1) So first we have a person who is interested into gaming he might not be interested into buying but just having a quick look at the 
    prices and content and why not geting any updates in the gaming industri by having a look around at the links provided .
- 2)The second user might be a person that is looking for a game but cant decide which one to try.
    He can use one of the links of the social media to see the page forums and discusions (future planing)
- 3)A person that wants to buy a game:
    The content is straight forward . Each game easy to find because they are sorted well into categories .
    (comming soon category feauture planing)
- 5)And why not a developer :
    The app it's easy to build not very complicated and i think might be an help to someone that looks for inspiration for it's new project


 ## Design process
 Above are the first ideas of the webpage shown in wireframes
![IMG_3994](https://user-images.githubusercontent.com/63249988/118945727-a19d6800-b94d-11eb-8156-d843966e108b.JPG)
![IMG_3993](https://user-images.githubusercontent.com/63249988/118945738-a530ef00-b94d-11eb-9a19-16a8c4e8e064.JPG)
![IMG_3991](https://user-images.githubusercontent.com/63249988/118945746-a6fab280-b94d-11eb-844f-ae5707ba1383.JPG)
![IMG_3995](https://user-images.githubusercontent.com/63249988/118945753-a82bdf80-b94d-11eb-9cca-e36283a245f0.JPG)
![IMG_3992](https://user-images.githubusercontent.com/63249988/118945759-a95d0c80-b94d-11eb-8fac-a5cfab2373b0.JPG)

how the actual app was finished

![Screenshot 2021-05-20 at 09 17 43](https://user-images.githubusercontent.com/63249988/118944593-9c8be900-b94c-11eb-89a9-44663858b5d7.png)
![Screenshot 2021-05-20 at 09 16 27](https://user-images.githubusercontent.com/63249988/118944603-9eee4300-b94c-11eb-949c-54cc3455dd6e.png)
![Screenshot 2021-05-20 at 09 17 27](https://user-images.githubusercontent.com/63249988/118944607-a0b80680-b94c-11eb-8285-33c94d7e16e2.png)
![Screenshot 2021-05-20 at 09 16 21](https://user-images.githubusercontent.com/63249988/118944615-a1e93380-b94c-11eb-93b7-fa0355ca865b.png)
![Screenshot 2021-05-20 at 09 15 28](https://user-images.githubusercontent.com/63249988/118944622-a3b2f700-b94c-11eb-8620-b08cd07b07bf.png)
![Screenshot 2021-05-20 at 09 16 34](https://user-images.githubusercontent.com/63249988/118944647-a9a8d800-b94c-11eb-80c4-e45235f85e50.png)
![Screenshot 2021-05-20 at 09 17 36](https://user-images.githubusercontent.com/63249988/118944655-aada0500-b94c-11eb-8407-6089fe1dd850.png)
![Screenshot 2021-05-20 at 09 15 35](https://user-images.githubusercontent.com/63249988/118944659-ac0b3200-b94c-11eb-9ccb-cdcc7f86d36f.png)
![Screenshot 2021-05-20 at 09 15 51](https://user-images.githubusercontent.com/63249988/118944664-ad3c5f00-b94c-11eb-81df-9544c223fdfd.png)
![Screenshot 2021-05-20 at 09 15 57](https://user-images.githubusercontent.com/63249988/118944671-ae6d8c00-b94c-11eb-8782-c9cfd6f3dd40.png)
![Screenshot 2021-05-20 at 09 16 10](https://user-images.githubusercontent.com/63249988/118944676-af9eb900-b94c-11eb-8634-7f2b5b32bca0.png)

The images dispaly the app on pc screen tablet and phone both landscape and portrait


Colour Scheme

I through to use more the background image to look more interesting than a plain color background.
Also the main color used for the page is black code #100 and blue code #3354AA.


Typography

The main font family used is "Lato".

## Features
The page is been programed to work in 3 different screen sizes.
1)PC
2)Tablet
3)Smartphone
The elements are responsible designed to suit the changes made to the screen.

1. Navbar - Consist of 2 navbars one made spacially for the large screens and one made for the smaller screens.
    they both have the same elements only difference is the Logo of the page in large screen is substituted with Title in the mobile
    navbar. They both have the the home button to take you alwasys to the home page, the acount that you can use to log in or register or manage 
    products if you are the admin the basket and the search nav. The mobile navbar uses the category items as dropdown elements while the main nav have them
    display as flex element 
2. Home - The homepage consist of the navbar the fotter and a carousel thet displays images.
3.  My profile - Defines the user's profile giving him the abillity to see orders he has already done and update his adress.
4.  log-in/register - is not mandatory as you can checkout as a guest but you cant axxes the profile if you don't have a log-in
5.  Social Links - Provides users with links to the website social media pages.
    (Links NOT LIVE as this project is for learning purpose ).


 //Features to add//
1. Make a blog conected to the website where people get ideas or post their own about different discusions about games
2. Make user's able to add profile pictures to their acoun's
3. Make users able to sell thir own games to the page.
4. Add more platforms PC/ Nintendo
5. Make a subscription for 5 pound a month every month and get a free game every month

## Technologies Used

Languages Used
-HTML : divs are used more to group different section 
-CSS3 : used to style the html elements
-JS : used to deal with stripe and increase and decrease quatity in inside the bag
-Python : all the logics has been done by pyhon mostly conections between views and urls

Frameworks, Libraries & Programs Used

Bootstrap 4.4.1:
(Bootstrap was used to assist with the responsiveness and styling of the website.)

Font Awesome:
(Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.)

Django : as a framework

Git: (Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.)

Gmail services for the email verifications

Heroku :This project uses Heroku, a web hosting service that supports Python applications, for final project deployment.

GitHub This project uses GitHub, for version control and final project backup.

Amazon S3 bucket : used to hold the media and static files 

Stripe is used to deal with the payments and webhooks for the incoplete payments



## Testing
* Sign up

    * If you try to register with a n pasword with entirly numbers it won't accept it
    * If the password is similar to the username it wont accept it
    * If you submit an empty register form it will ask to fill the form first
    
    

* Log In Page:

    *  If you sign in with different account that has no order history the orfer history will be empty
    * If you sing with a normal user you can't accesh the product management or the edit and delete product page.
    *  If you are signed in and you have items in your shopping list when you log of it will make the basket 0
    * If you try to log in with existing user it will tell you this user is already taken 




The app was tested on iphone 7 and iphone 11 and also using google chrome inspect on all the devices available on the inspector.
Both landscape and portrait doesn't seem to have any problem only in safari broswer for some reason the bag and the navbar in mobile does'nt seem to 
respond to the css which the respond prity well in google chrome. Besides that testing have been made with the stripe acount and the test credit card
stripe complets the payment at it is shown in the system as payment been made . As well as the webhook is giving positiv behaviour . I have tried to make
a payment and quit it before it was fully fone and the webhook handled the payment . The verifcation emails have benn tested as well when you 
register you recieve a link in the email you have put as your email and when you press that link the confirmation is done and you can access your acount.
Tht bucket database is tested all the products are displaying correctly and everytime you add or delete a product it updates in both sides. If deleted from page
deleted from the database as well and if you delite it fro database is gone from page as well.
The edit add and delete functionality works. The product no image is functional everytime you add a produkt that has no image the default no image 
logo will be aded to the product .

## Bugs
During development and testing this bugs were present. :
1) During development the webhook was not sending test webhoos . Fixed (I read on Slack that you have to make the port i was working with 
public and after that everything fine)
2)During development heroku would shut down and prevent the automatic deployment (fixed restated a couple of time and is working fine now)
3)After deployment in Heroku safari is having slightly isues with the css more the mobile small screen size especialy iphone 5c( acording to google dev tools )
4)Another bug is that the pagination sometimes insted of giving the pages of one category  sdkrf, returns all the pages.
5)I Couldn't login to heroku from the terminal as normaly so  used 'heroku login -i' instead

## Deployment
The first thing was the first commit done on the git .
After that been working regurly on the git pod and trying to commit often.Using git add and file name to add the filea and git commit
-m to add coments to the commits and git push as well to push to github.
After that started to make the database of the products and categories using ficturines json files.
After the products and categories were done and the page was responsible and everything working fine the deployment started .
First istall dj_database_url . After we need to get the database set up . So we do that by using the comand python3 manage.py loadtada categories,
sub_categories, special_categories and last ptoducts.
After that we create our ptocfile and we have to disable collections so that heroku wont collect static files.
After that conected github to heroku through github pages and made automatic update on so everytime you push on gitpod it updates automatic at heroku.
To make the deployment to Herkou:
    1.The following section describes the process to deploy this project to Heroku.
    2.Ensure all required technologies are installed locally, as per the requirements.txtfile.
    3.Via Terminal, login to Heroku, using 'heroku login' command or if it is not working heroku login -i. Input Heroku login details. 
    4.Create new Heroku app, using 'heroku apps:create appname' command.
    5.Push project to Heroku, using 'push -u heroku master' command.
    6.Login to Heroku and select newly created app.
    7.Select settings. Select ‘Reveal Config'. Add IP 0.0.0.0 and PORT 5000.
    8.From 'More' menu on the top right, select 'Restart all dynos'.
   9.View app: In settings, select Domain URL, NOT Git URL to view your hosted application.
   10.Upon successful deployment Heroku will give you the URL that is hosted your app
After done the conection to heroku we need to set up the AS3 bucket for the meadia files
1)We login to AWS or creat an acount,
2)Ope S3 and create a new bucket,
3)Create a user ,
4)Than we create a group,
5)To conect django to the s3 bucket we need boto3 and django storages
6)Than ad storages to the install apps,
7)After done all that and set the parameters to settings .py when we push the code , Heroku is going to look for static files,
8)after the static files are done it's time for the media so we open s3 and create a new folder called Media.
9)We put our media files all in there and thats it we set the s3 bucket.


## Credits

### Content
    * The images and descriptions were taken from https://uk.webuy.com/ which i used as ispiration for the project
    * The butique ado project as well has helped a loot on the way of developing Gear Up
    

### Media

    * THe background photo is the one uset from sony ps4

## Acknowledgements

    - My Mentor for continuous helpful feedback.
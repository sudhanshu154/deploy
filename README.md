## HarvardX CS50W: Web Programming with Python and JavaScript
# -by sudhanshu154

    
    
### Requirements
The final project is your opportunity to design and implement a dynamic website of your own. So long as your final project draws upon this course’s lessons, the nature of your website will be entirely up to you, albeit subject to the staff’s approval.

In this project, you are asked to build a web application of your own. The nature of the application is up to you, subject to a few requirements:

  - Your web application must utilize at least two of Python, JavaScript, and SQL.
  - Your web application must be mobile-responsive.
  - In README.md, include a short writeup describing your project, what’s contained in each file you created or modified, and (optionally) any other additional information the staff should know about your project.
  - If you’ve added any Python packages that need to be installed in order to run your web application, be sure to add them to requirements.txt!

        - Your web application must be sufficiently distinct from the other projects in this course (and, in addition, may not be based on the old CS50W Pizza project), and more complex than those.
                o A project that appears to be a social network is a priori deemed by the staff to be indistinct from Project 4, and should not be submitted; it will be rejected.
                o A project that appears to be an e-commerce site is strongly suspected to be indistinct from Project 2, and your README.md file should be very clear as to why it’s not. Failing that, it should not be submitted; it will be rejected.
            - Your web application must utilize Django (including at least one model) on the back-end and JavaScript on the front-end.
            - Your web application must be mobile-responsive.
Beyond these requirements, the design, look, and feel of the website are up to you!


### Final project
The Final project is a online shopping web-site. where you can shop, add product to your cart,Buy it and place the order to your profile address.
    
The project was built using Django as a backend framework and JavaScript as a frontend programming language. All generated information are saved in database (SQLite by default).

All webpages of the project are mobile-responsive.

#### Installation
  - Make and apply migrations by running `python manage.py makemigrations` and `python manage.py migrate`.
  - Create superuser with `python manage.py createsuperuser`. This step is optional.
  - Go to website address and register an account.

#### Files and directories

  - `app` - main application directory.
    - `static/djangoapp` contains all static content.
        -`css` all css files in it.
           -`all.min.css`
           -`owl.carousel.min.css`
           -`style.css`
        -`images` images of all banners & images of payment ways
        -`js` contians all javascripte files
    - `templates/app` contains all the html files.
    - `admin.py` - here I added some admin classes and re-registered User model.
    - `models.py` contains four models I used in the project. `Customer` model takes the details of customer ,`Product` model takes the details of Product ,`Cart` model takes the ditails which user have what in there cart and how much,`OrderPlaced` model takes the details where the ordered product/productes has/have to be delivered,
    - `urls.py` - all application URLs.
    - `views.py` respectively, contains all application views.
  - `Kart` - project directory.    
  - `media`- this directory contains all product images

### What you can do with it -

At home page:


    * There are many section with sliders.
    * Banners of sale and product.
    * Category wise separated products.
    * At nav.
* From drop down button you can go to specifically to that product category.

*search bar Is not active.

* login and registration are in working state.

In drop down (Electronics -> mobile):

    - Their at LHS filter are their to filter according to the options present on it
    - Similarly, In all the dropdowns  

### For more features you have login/register.

 - The registration form is full secured with tight validation process(using django in build features )
 - If your successfully registered it will show you successful message 
 - Now you can login with the credential you provided in registration form
 - In case you, forgot your password you can rest password by clinking 

##### *To reset you password –
 - In log in form there is a link displayed “forgot password” go to that link.
 - The page will ask you for your registered mail id.
 -  Provide your correct mail id .
 -  if mail is correct then you will get a link in you cmd saying
 
 For Exampal - 

         “ You're receiving this email because you requested a password reset for your user account at 127.0.0.1:8000. 

        Please go to the following page and choose a new password:                                                     

        http://127.0.0.1:8000/password-reset-confirm/Nw/axru84-ccfecb23153f2884bb773fa6641e5a78/

        Your username, in case you’ve forgotten: xxxxxxx ”

- Go to the link.

  - It will take you to a new window asking  "New PAssword & Confirm New Password".
  - IF YOUR PASSWORD satisfy the conditions it will show you “password Change Successfully” massage.
-  After Login –
  - IT WILL show you profile of your account. You can fill it for registering your address.
  - If the address details are add Successfully will show you Successfully saved message.
  - At LHS, you can go to address and see the address which you filled in profile section.
  - You can add multiple address.


### At top RHS drop down with you username
    - Profile- which seen at first when logged in
    - Orders – to get the details of your ordered products
    - Change password – It’s fully functional.(change password in different from reset password)
    - Log out – to make you logout.
    
##### Just side of your username there is a Cart option
  - You can add go to any product shown and you will see an options like “ add to cart” and “Buy Now”.
  - But, after you add the product to cart you will see “go to cart” in place of “add to cart” which will take you to the Cart.
  - At CArrt page you cann Increase the quantity of the product/products and just at the side you can see the bill amount.
  - There is “remove item” button which removes the product from the Cart
  - You add multiple product to Cart at a time
  - Below the bill there is a option to   Place your order which will take you to order summary page
  - You can select the address’s from which you provided and Buy the product
  - Then it will direct you to the orders page where you can sport you orders details.
  - After placing order, the product will be removed from the Card and shown in the orders section 
  - status of the product can only be changed from admin > order placeds > status 
  - change in the status of the ordered product will show the change in the color of bar in front of the product 
    
## In admin section
    •	In users – you will see one user
    •	But In customers – you will sport multiple customers because that user provided that many address’s
    •	Cart – the cart products are visible
    •	Order placed – the details of orders like – user,product,customer,quantity& status of the product.
    •	 Product – where we can add the product’s
    
  ##### *	After placing order, the product will be removed from the Card and shown in the orders section


### Course's link
See [here](https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript).

# Task

We will be displaying our shiny new products on our website!

## Setup

1. Fork and clone [this repository](https://github.com/JoinCODED/TASK-Django-Views-and-URLs).
2. Create a `virtual environment` and activate it.
3. Install the requirements using `pip install -r requirements.txt`.
4. Run migrations using `python manage.py migrate`.
5. Create an admin user using `python manage.py createsuperuser`.
6. Run the server using `python manage.py runserver`.
7. Go to the admin panel and create several products.

## Home View

1. Go to `views.py` and create a home view for your website:
   - Call the function `get_home`.
   - The function will receive a `request`, and return an `HttpResponse`.
   - The `HttpResponse` should contain an `h1` tag that welcomes the user to the website.
2. Go to `urls.py` and create a path for our home view.
   - Import our `get_home` view.
   - Add a `path` that starts with `home/`.
3. Go to `/` on your web browser and verify that you can see your `h1` tag.
4. Commit and push your code.

## Detail View

1. Go to `views.py` and create a detail view for your products.
   - Call the function `get_product`.
   - The function will receive a `request` and a `product_id`, and return an `HttpResponse`.
   - The function should use the `product_id` received from the parameters to fetch the `Product` from the database.
   - The `HttpResponse` should contain a [multi-line](https://www.programiz.com/python-programming/examples/multiline-string) string, which is also an [f-string](https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python), which displays the details of our product.
2. Go to `urls.py` and create a path for our product detail view.
   - Import our `get_product` view.
   - Add a `path` that starts with `products/` and contains an id in it.
3. Go to `/products/YOUR_ID/` on your web browser and verify that you can see your product.
4. Commit and push your code.

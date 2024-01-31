## Flask Application Design

### HTML Files

#### `index.html`
- Purpose: Homepage of the website.
- Content:
  - Header with shop's name, Cloud9.
  - Navigation bar with links to different sections of the website.
  - Image slider showcasing various cakes.
  - A welcome message with a brief description of Cloud9 and its offerings.
  - A section displaying featured cakes with images and descriptions.
  - Footer with contact information and social media links.

#### `shop.html`
- Purpose: The page where users can browse and purchase cakes.
- Content:
  - Navigation bar with links to different sections of the website.
  - Filters for sorting cakes based on type, price, or popularity.
  - Search bar for finding cakes based on keywords.
  - Product grid displaying cakes with images, names, descriptions, and prices.
  - Pagination controls for browsing through multiple pages of cakes.

#### `cart.html`
- Purpose: The page where users can view and manage items in their shopping cart.
- Content:
  - Navigation bar with links to different sections of the website.
  - A table displaying cart items, including images, names, quantities, and prices.
  - Buttons for updating quantities or removing items from the cart.
  - A section for applying coupon codes and calculating the total amount.
  - A button for proceeding to checkout.

#### `checkout.html`
- Purpose: The page where users enter their shipping and billing information.
- Content:
  - Navigation bar with links to different sections of the website.
  - A form for collecting user information, including name, address, email, and phone number.
  - A section for selecting shipping options and calculating the shipping cost.
  - A section for selecting payment methods, such as credit card or PayPal.
  - A button for placing the order.

### Routes

#### `/`
- HTTP Method: GET
- Purpose: Displays the homepage, `index.html`.

#### `/shop`
- HTTP Method: GET
- Purpose: Displays the cakes, `shop.html`.

#### `/cart`
- HTTP Method: GET
- Purpose: Displays the cart items, `cart.html`.

#### `/add_to_cart`
- HTTP Method: POST
- Purpose: Adds a cake to the shopping cart.

#### `/update_cart`
- HTTP Method: POST
- Purpose: Updates the quantity of a cake in the shopping cart.

#### `/remove_from_cart`
- HTTP Method: POST
- Purpose: Removes a cake from the shopping cart.

#### `/checkout`
- HTTP Method: GET
- Purpose: Displays the checkout page, `checkout.html`.

#### `/place_order`
- HTTP Method: POST
- Purpose: Places an order.
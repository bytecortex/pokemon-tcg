# Pokémon TCG E-commerce 🃏⚡

A simple e-commerce platform for buying and selling Pokémon TCG cards. Built with **Python**, **MySQL**, and **PokeAPI** for real-time card data.

## Features 
- 📦 **Buy & Sell Cards** – Users can browse, purchase, and list Pokémon cards for sale.
- 🔍 **Search & Filter** – Find cards by name, type, rarity, or set.
- 🖼 **Real-time Card Data** – Uses **PokeAPI** to fetch up-to-date Pokémon TCG details.
- 💳 **Secure Checkout** – Implements a secure payment flow.
- 📊 **Inventory Management** – Users can track their listed cards and sales.

## Technologies Used 🛠️
- **Backend:** Python (Flask/Django)
- **Database:** MySQL
- **API:** PokeAPI (for card details)
- **Frontend:** HTML, CSS, JavaScript (React/Vue)
- **Authentication:** JWT-based user authentication
- **Payment Integration:** Stripe/PayPal

## Installation 🚀
### Prerequisites:
- Python 3.x
- MySQL
- Node.js (if using a frontend framework)

### Steps:
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/pokemon-tcg-ecommerce.git
   cd pokemon-tcg-ecommerce
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up the database:
   ```sh
   mysql -u root -p -e "CREATE DATABASE pokemon_tcg;"
   ```
5. Run migrations (if using Django):
   ```sh
   python manage.py migrate
   ```
6. Start the development server:
   ```sh
   python app.py  # For Flask
   python manage.py runserver  # For Django
   ```

## Usage 🏪
- Visit `http://localhost:5000/` (Flask) or `http://localhost:8000/` (Django) to access the app.
- Sign up, browse available cards, and manage your collection!

## Contributing 🤝
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

## License 📜
This project is licensed under the MIT License.



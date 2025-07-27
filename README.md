# Pokémon TCG E-commerce 🃏⚡

A simple e-commerce platform for buying and selling Pokémon TCG cards. Built with **Vue.js**, **MySQL**, and **PokeAPI** for real-time card data.

<!-- 🌐 **Check it out live:** [poqg.live](https://poqg.live)-->

## Features 

- 📦 **Buy & Sell Cards** – Users can browse, purchase, and list Pokémon cards for sale.
- 🔍 **Search & Filter** – Find cards by name, type, rarity, or set.
- 🖼 **Real-time Card Data** – Uses **PokeAPI** to fetch up-to-date Pokémon TCG details.
- 💳 **Secure Checkout** – Implements a secure payment flow.
- 📊 **Inventory Management** – Users can track their listed cards and sales.

## Technologies Used 

- **Frontend:** Vue.js, Shadcn and Tailwindcss
- **Backend:** TBD (Node.js)
- **Database:** MySQL
- **API:** PokeAPI (for card details)

## Installation and Setting Up 

### Prerequisites:

- Docker
- Linux environment or WSL 

### Steps:

1. Using Linux or WSL, clone the repository and navigate to the project folder:
   ```sh
   git clone https://github.com/bytecortex/pokemon-tcg.git
   cd pokemon-tcg
   ```
2. Configure environment variables:

   - `.env` — located inside the `./backend` folder

3. Install the dependencies and start the project:
   ```sh
   docker compose up --build
   ```

## Usage 

- Visit `http://localhost:5173/` to access the app.
- Sign up, browse available cards, and manage your collection!

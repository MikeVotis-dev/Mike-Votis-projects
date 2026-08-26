
# My Budget Tracker

#### Video Demo: https://youtu.be/XjgTI4f_dSs

#### Description:

Hey everyone! For my CS50 final project, I decided to build something practical that I could actually use in daily life: a web-based Budget Tracker. Managing personal finances can sometimes get messy, so I wanted to create a simple, clean, and secure web application where people can keep track of their income and expenses without any hassle.

##How I Built It (Design Choices)

I wanted to stick to the core technologies we learned throughout the course while making sure the app felt modern and responsive:

- **Python & Flask:** I used Flask because it makes backend routing super straightforward and integrates brilliantly with HTML templates.
- **SQLite & CS50 Library:** For the database, I went with SQLite. It's lightweight, easy to set up, and perfect for handling user accounts and storing transactions locally. Using the CS50 SQL library also kept my queries clean and protected against basic vulnerabilities.
- **Security:** Security was a big priority, especially for handling user passwords. Instead of saving passwords in plain text, I used Werkzeug's security functions (`generate_password_hash` and `check_password_hash`) to securely hash and verify user credentials.
- **Bootstrap 5:** I'm not a CSS expert, so Bootstrap saved the day. It gave me a clean layout, nice cards, and a responsive table design out of the box, with nice color touches (green for income, red for expenses) so users can instantly see their financial status.

### Project Files Overview

Here is a quick breakdown of the files I wrote for this project and what each one does:

1. **`app.py`**: This is the main backend brain of the app. It sets up the Flask application, connects to the SQLite database, and handles all the routing (like logging in, registering, adding transactions, and logging out). It also checks if a user is logged in before letting them view the dashboard.
2. **`finance.db`**: The database file that holds two main tables: `users` (which saves usernames and password hashes) and `transactions` (which links each expense or income entry to the correct user ID, along with the category, type, and amount).
3. **`templates/layout.html`**: The layout template that wraps around all my pages. It includes the navigation bar, footer, and the necessary Bootstrap CSS/JS links to keep the design consistent.
4. **`templates/index.html`**: The main dashboard page. Once users log in, this file loops through their transaction history and displays it in a clean, color-coded table.
5. **`templates/login.html` & `templates/register.html`**: These are the login and registration pages. They feature centered Bootstrap cards with clean forms to give users a smooth onboarding experience.
6. **`templates/add.html`**: A simple form page where users can input a new transaction by choosing whether it's an income or expense, typing a category, and entering the amount.

### Wrapping Up

Working on this project was an awesome journey and a great way to wrap up CS50x. It combined everything I learned about web development, databases, and security into a real application. I hope you like it!

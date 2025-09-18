# Minimalist Caua Rego Website

This is a minimalist personal portfolio website for Caua Rego, built with Flask for the backend and a combination of HTML, CSS, and JavaScript for the frontend. The website showcases Caua Rego's profile, skills, projects, services, and certificates in a clean and interactive manner.

## Features

*   **Minimalist Design:** Clean and modern user interface.
*   **Dark/Light Theme Toggle:** Users can switch between dark and light modes, with preference saved in local storage.
*   **Dynamic Content Loading:** Flask dynamically injects content from individual HTML files into a base template.
*   **Interactive Cursor:** A custom cursor follower with visual effects on interactive elements.
*   **Page Transition Animations:** Smooth fade-in/fade-out effects when navigating between pages.
*   **Contact Form:** A functional contact form that logs submissions to a text file.
*   **Particles Background:** An animated particle background effect using `particles.js`.
*   **Profile Section:** Detailed information about Caua Rego's education, skills, and professional focus.
*   **Projects/Repositories Section:** Highlights key projects with links to GitHub repositories.
*   **Services Section:** Lists the services offered.
*   **Certificates Section:** Displays professional certifications.

## Technologies Used

**Backend:**
*   Python
*   Flask

**Frontend:**
*   HTML5
*   CSS3
*   JavaScript
*   `particles.js` (for background animation)

## Setup and Installation

To get this project up and running on your local machine, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/caua-rego/minimalist-caua-rego-website.git
cd minimalist-caua-rego-website
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

*   **Windows:**
    ```bash
    .\venv\Scripts\activate
    ```
*   **macOS/Linux:**
    ```bash
    source venv/bin/activate
    ```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

The application will typically run on `http://127.0.0.1:5000/`. Open this URL in your web browser.

## Project Structure

```
.
├── app.py                  # Main Flask application file
├── contact_log.txt         # Log file for contact form submissions
├── database.db             # SQLite database file (if used for other features)
├── requirements.txt        # Python dependencies
└── frontend/
    ├── about.html          # About page content
    ├── certificates.html   # Certificates page content
    ├── contact.html        # Contact page content with form
    ├── footer.html         # Footer content
    ├── home.html           # Home page content
    ├── index.html          # Base HTML template
    ├── profile.html        # Profile page content
    ├── repositories.html   # Repositories page content
    ├── script.js           # Frontend JavaScript for interactivity
    ├── services.html       # Services page content
    ├── style.css           # Frontend CSS for styling
    ├── audio/
    │   └── soundNatural.mp3 # Background audio
    └── img/
        ├── banner.png
        ├── hero_background.jpg
        ├── logo.jpeg
        ├── portrait.png
        └── white_hero.jpg
```

## Usage

Navigate through the website using the navigation bar.
*   **Home:** Introduction to the website.
*   **About:** Brief introduction to Caua Rego.
*   **Certificates:** View professional certifications.
*   **Services:** Explore the services offered.
*   **Contact:** Fill out the form to send a message.
*   **Profile:** Detailed profile information.
*   **Repositories:** Links to GitHub projects.

The theme can be toggled between dark and light mode using the "Toggle Theme" button in the navigation bar.

## Contact

For any inquiries, please use the contact form on the website or reach out via the social links provided in the footer.

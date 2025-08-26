# Django TOTP Authenticator

A simple, lightweight Django application that demonstrates how to build a Time-Based One-Time Password (TOTP) authentication system from scratch. This project is the practical implementation of the concepts explained in the blog post: [Understand How Google Authenticator Works by Building a Django App](https://blog.mukul.com.np/understand-how-google-authenticator-works-by-building-a-django-app).

This app provides a secure two-factor authentication (2FA) flow using authenticator apps like Google Authenticator or Authy, relying purely on Django's built-in features and standard Python libraries.

## 📌 About The Project

In today's digital world, passwords alone are not enough. Two-factor authentication (2FA) adds a critical second layer of security. This project serves as a hands-on guide to understanding and implementing one of the most common 2FA methods: TOTP.

Instead of relying on third-party packages like `django-otp`, this application is built from the ground up to demystify the underlying principles of TOTP. The goal is to show how a secure authenticator flow can be created using only Python's standard libraries (`pyotp` for the core logic) and Django's robust authentication framework.

## 🤔 How It Works: The TOTP Mechanism

The entire system is based on a shared secret key and the current time. Here’s a breakdown of the process, as detailed in the accompanying [blog post](https://blog.mukul.com.np/understand-how-google-authenticator-works-by-building-a-django-app).

1.  **Shared Secret Key**: When a user enrolls in 2FA, the server generates a unique, random secret key (e.g., `JBSWY3DPEHPK3PXP`). This key is shared with the user just once, typically via a QR code.
2.  **Time-Based Counter**: Both the server and the user's authenticator app use the same time-step (usually 30 seconds) to calculate a counter. This counter is derived from the current Unix time.
3.  **HMAC Generation**: The authenticator app uses the **shared secret key** and the **time-based counter** to generate a Hash-Based Message Authentication Code (HMAC).
4.  **One-Time Password**: This HMAC is truncated to produce the familiar 6-digit code you see in your app. Because the time-counter changes every 30 seconds, a new code is generated continuously.
5.  **Verification**: When the user enters the 6-digit code during login, the server performs the exact same calculation. If the generated code matches the user's input, access is granted.

This project implements this entire flow within a standard Django registration and login process.

## ✨ Key Features

*   **Educational Focus:** Built to be a clear and understandable implementation of TOTP.
*   **Self-Contained Logic:** The core authentication flow is written from scratch, using Django's native `auth`, `forms`, and `messages` frameworks.
*   **QR Code Onboarding:** Uses the `qrcode` library to present the secret key to the user for easy setup with any standard authenticator app.
*   **Secure by Design:** Leverages HMAC-SHA1, the standard algorithm for TOTP, to ensure codes are secure and verifiable.
*   **No External Dependencies:** Avoids complex third-party Django packages for the authentication logic.

## 🚀 Getting Started

Follow these steps to get a local copy up and running for development and testing.

### Prerequisites

*   Python 3.x
*   Django
*   pip

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/mukulboro/django-authenticator.git
    cd django-authenticator
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```sh
    python manage.py migrate
    ```

5.  **Create a superuser to access the admin panel:**
    ```sh
    python manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```sh
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000`.

## ▶️ Usage

Once the server is running, you can test the full authentication flow:

1.  Navigate to `http://127.0.0.1:8000/register/` to create a new user account.
2.  Log in for the first time. The application will generate a secret key and display it as a QR code.
3.  Scan the QR code with an authenticator app (Google Authenticator, Authy, etc.).
4.  You will be prompted to enter the 6-digit code to complete your first login.
5.  On all subsequent logins, you will need to provide your password and a valid TOTP code.

## 🛠️ Technology Stack

*   **Backend:** Django
*   **Core Logic:**
    *   `pyotp`: A library for generating and verifying one-time passwords. It handles the low-level TOTP algorithm.
*   **Utilities:**
    *   `qrcode`: For generating QR code images.
    *   `python-dotenv`: For managing environment variables.

# My Blog

This is a personal blog built using Django. The blog covers topics related to programming, cloud computing, and other technology-related subjects. Users can subscribe with their email to receive notifications about new content.

## Features

- **Blog Posts**: Create, update, and delete blog posts.
- **Categories**: Organize posts into categories for easy navigation.
- **Tags**: Add tags to posts for keyword-based organization.
- **Subscriptions**: Users can subscribe with their email address to get notified when new posts are published.

## Models

### 1. **Post**
- Represents a blog post with a title, content, author, and related metadata like categories and tags.
- Contains `is_published` flag to control whether the post is publicly visible.

### 2. **Category**
- Allows grouping of posts under specific categories for better organization.

### 3. **Tag**
- Enables the use of tags for better search and filtering of posts.

### 4. **Subscription**
- Allows users to subscribe via email to receive notifications about new posts.

## Setup Instructions

### Requirements

- Python 3.8+
- Django 4.0+
- SQLite (default), or any other database of your choice

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-blog.git
    cd your-blog
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the server:

    ```bash
    python manage.py runserver
    ```

7. Visit the blog at `http://127.0.0.1:8000/`.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, feel free to reach out to me on X at `https://x.com/EmmanuelSandjio`.


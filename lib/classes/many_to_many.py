class Article:
    all = []  # Class attribute to track all instances of Article

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title  # This will call the title setter

        # Add the article to the author's list of articles (if not already present)
        if self not in author.articles():
            author.articles().append(self)

        # Add the article to the magazine's list of articles (if not already present)
        if self not in magazine.articles():
            magazine.articles().append(self)

        # Add the article to the class-level list (if not already present)
        if self not in Article.all:
            Article.all.append(self)

    @property
    def title(self):
        """Returns the article's title."""
        return self._title

    @title.setter
    def title(self, value):
        """
        Validates and sets the article's title.
        
        Args:
            value (str): The title of the article.
        
        Notes:
            - The title must be a string between 5 and 50 characters.
            - The title cannot be changed after instantiation.
            - Silently ignores invalid assignments (non-string or invalid lengths).
        """
        if not isinstance(value, str):
            return  # Silently ignore non-string assignments
        if len(value) < 5 or len(value) > 50:
            return  # Silently ignore invalid lengths
        if hasattr(self, "_title"):
            return  # Title is immutable after instantiation
        self._title = value

    @property
    def author(self):
        """Returns the author of the article."""
        return self._author

    @author.setter
    def author(self, value):
        """
        Validates and sets the author of the article.
        
        Args:
            value (Author): The author of the article.
        
        Raises:
            ValueError: If the author is not of type Author.
        """
        if not isinstance(value, Author):
            raise ValueError("Author must be of type Author.")
        self._author = value

    @property
    def magazine(self):
        """Returns the magazine where the article is published."""
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        """
        Validates and sets the magazine of the article.
        
        Args:
            value (Magazine): The magazine where the article is published.
        
        Raises:
            ValueError: If the magazine is not of type Magazine.
        """
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be of type Magazine.")
        self._magazine = value


class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []  # List to store articles written by the author

    @property
    def name(self):
        """Returns the author's name."""
        return self._name

    @name.setter
    def name(self, value):
        """
        Validates and sets the author's name.
        
        Args:
            value (str): The name of the author.
        
        Notes:
            - The name must be a non-empty string.
            - The name cannot be changed after instantiation.
        """
        if not isinstance(value, str):
            return  # Silently ignore non-string assignments
        if len(value) == 0:
            return  # Silently ignore empty strings
        if hasattr(self, "_name"):
            return  # Name is immutable after instantiation
        self._name = value

    def articles(self):
        """Returns a list of all articles written by the author."""
        return self._articles

    def magazines(self):
        """Returns a unique list of magazines the author has contributed to."""
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        """
        Creates and returns a new Article instance associated with the author and magazine.
        
        Args:
            magazine (Magazine): The magazine where the article is published.
            title (str): The title of the article.
        
        Returns:
            Article: The newly created article.
        """
        new_article = Article(self, magazine, title)
        return new_article  # The Article class will handle adding to the author's and magazine's lists

    def topic_areas(self):
        """
        Returns a unique list of categories of magazines the author has contributed to.
        
        Returns:
            list: A list of categories (strings).
            None: If the author has no articles.
        """
        if not self._articles:
            return None
        return list(set(magazine.category for magazine in self.magazines()))






class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []  # List to store articles published in the magazine

    @property
    def name(self):
        """Returns the magazine's name."""
        return self._name

    @name.setter
    def name(self, value):
        """
        Validates and sets the magazine's name.
        
        Args:
            value (str): The name of the magazine.
        
        Raises:
            ValueError: If the name is not a string or is outside the length constraints.
        """
        if not isinstance(value, str):
            return  # Silently ignore non-string assignments
        if len(value) < 2 or len(value) > 16:
            return  # Silently ignore invalid lengths
        self._name = value

    @property
    def category(self):
        """Returns the magazine's category."""
        return self._category

    @category.setter
    def category(self, value):
        """
        Validates and sets the magazine's category.
        
        Args:
            value (str): The category of the magazine.
        
        Raises:
            ValueError: If the category is not a string or is empty.
        """
        if not isinstance(value, str):
            return  # Silently ignore non-string assignments
        if len(value) == 0:
            return  # Silently ignore empty strings
        self._category = value

    def articles(self):
        """Returns a list of all articles published in the magazine."""
        return self._articles

    def contributors(self):
        """
        Returns a unique list of authors who have contributed to the magazine.
        
        Returns:
            list: A list of Author instances.
        """
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        """
        Returns a list of titles of all articles published in the magazine.
        
        Returns:
            list: A list of article titles (strings).
            None: If the magazine has no articles.
        """
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        """
        Returns a list of authors who have written more than 2 articles for the magazine.
        
        Returns:
            list: A list of Author instances.
            None: If no authors have written more than 2 articles.
        """
        author_counts = {}
        for article in self._articles:
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1
        return [author for author, count in author_counts.items() if count > 2] or None






























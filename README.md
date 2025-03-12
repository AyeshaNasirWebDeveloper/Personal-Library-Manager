# Personal Library Manager

## 📌 Overview
The **Personal Library Manager** is a Streamlit-based web application that allows users to manage their personal book collection. Users can add, remove, search, and view statistics of their books. The data is saved in a JSON file for persistent storage.

## 🚀 Features
- 📖 **Add Books**: Store book details including title, author, year, genre, and read status.
- ❌ **Remove Books**: Delete books from the library by title.
- 🔍 **Search Books**: Find books by title or author.
- 📋 **Display All Books**: View the complete list of saved books.
- 📊 **Statistics**: Show total books and the percentage of books read.
- 💾 **Auto-Save**: Library data is automatically stored in `library.json`.

## 🛠 Installation
### 1️⃣ Prerequisites
Make sure you have Python installed on your system.

### 2️⃣ Install Dependencies
```bash
pip install streamlit
```

### 3️⃣ Run the Application
```bash
streamlit run main.py
```

## ⚙ How It Works
1. The app loads book data from `library.json`.
2. Users interact through the sidebar menu to manage books.
3. Any updates (add/remove) are automatically saved.
4. Statistics provide insights into reading habits.

## 🎯 Future Enhancements
- 📚 Categorization by tags
- 📊 Advanced analytics
- 🌐 Cloud-based storage

## 💡 Contribution
Feel free to contribute by submitting a pull request or reporting issues!

## 📜 License
This project is open-source and free to use.

Happy Reading! 📚✨
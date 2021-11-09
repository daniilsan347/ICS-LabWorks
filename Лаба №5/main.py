# Laba No5 -- OOP, Library

import csv
import sys

class Library:
  LibID   = None
  LibName = None
  books   = [0]
  genres  = []
  authors = []

  def __init__(self, LibID, LibName):
    self.LibID   = LibID
    self.LibName = LibName

  def addBook(self, bookObj):
    bookObj.bookID = self.books[0]
    self.books.append(bookObj)
    self.books[0] += 1
    if not bookObj.genre in self.genres:
      self.authors.append(bookObj.genre)    
    if not bookObj.author in self.authors:
      self.authors.append(bookObj.author)
    return bookObj.bookID

  def removeBook(self, bookID):
    for i in range(1, len(self.books)):
      if self.books[i].bookID == bookID:
        del self.books[i]
        return True
    return False

  # TODO: Genres and authros check and deletion 

  def getBooksNames(self):   return [f"{self.books[i].bookID} : {self.books[i].name} ({self.books[i].year})" for i in range(1, len(self.books))]
  def getBooksGenres(self):  return [bookObj.genre for bookObj in self.genres]
  def getBooksAuthors(self): return [bookObj.author for bookObj in self.authors]

  def getBookByID(self, bookID):
    for i in range(1, len(self.books)):
      if self.books[i].bookID == bookID:
        return self.books[i]
    return False

  def getBookByName(self, name):
    for i in range(1, len(self.books)):
      if self.books[i].name == name:
        return self.books[i]
    return False

  def getBooksByYear(self, year):
    result = []
    for i in range(1, len(self.books)):
      if self.books[i].year == year:
        result.append(self.books[i])
    return result
  def getBooksByGenre(self, genre):
    result = []
    for i in range(1, len(self.books)):
      if self.books[i].genre == genre:
        result.append(self.books[i])
    return result
  def getBooksByAuthor(self, author):
    result = []
    for i in range(1, len(self.books)):
      if self.books[i].author == author:
        result.append(self.books[i])
    return result

class Book:
  name   = None
  year   = None
  genre  = None
  author = None
  bookID = None
  
  def __init__(self, name, year, genre, author):
    self.name   = name
    self.year   = year
    self.genre  = genre
    self.author = author

print("Менеджер бібліотек")
lib1 = Library(0, "УкрСучЛіт")

with open(sys.path[0] + "/books.csv", "r", encoding="utf-8") as table1:
  reader = list(csv.reader(table1))
  del reader[0]
  for row in reader:
    lib1.addBook(Book(row[0], row[1], row[2], row[3]))

while True:
  print("1. Додати книгу")
  print("2. Показати список книг")
  print("3. Вивести книгу за ID")
  print("4. Пошук книги за...")
  print("5. Видалити книгу")
  
  userInput = input("$ ")
  if userInput == "1":
    name   = input("Назва: ")
    year   = input("Рік написання: ")
    genre  = input("Жанр: ") 
    author = input("Автор: ")
    print(f"ID Книги: {lib1.addBook(Book(name, year, genre, author))}")
  elif userInput == "2":
    print(lib1.getBooksNames())
  elif userInput == "3":
    bookIDInput = int(input("ID Книги: "))
    bookOutput  = lib1.getBookByID(bookIDInput)
    print("Назва       : " + bookOutput.name)
    print("Рік видання : " + bookOutput.year)
    print("Жанр        : " + bookOutput.genre)
    print("Автор       : " + bookOutput.author)
  elif userInput == "4":
    while True:
      print("1. Назва")
      print("2. Рік видання")
      print("3. Жанр")
      print("4. Автор")
      userInput = input("$ ")
      if userInput == "1":
        bookNameInput = input("Назва книги : ")
        bookOutput    = lib1.getBookByName(bookNameInput)
        if bookOutput:
          print("Назва       : " + bookOutput.name)
          print("Рік видання : " + bookOutput.year)
          print("Жанр        : " + bookOutput.genre)
          print("Автор       : " + bookOutput.author)
        else:
          print("Книги не знайдено")
      elif userInput == "2":
        bookYearInput = input("Рік видання книги: ")
        booksOutput   = lib1.getBooksByYear(bookYearInput)
        if booksOutput != []:
          for book in booksOutput:
            print("Назва       : " + book.name)
            print("Рік видання : " + book.year)
            print("Жанр        : " + book.genre)
            print("Автор       : " + book.author)
            print("=" * 13)
        else:
          print("Книг не знайдено")
      elif userInput == "3":
        bookGenreInput = input("Жанр книги: ")
        booksOutput   = lib1.getBooksByGenre(bookGenreInput)
        if booksOutput != []:
          for book in booksOutput:
            print("Назва       : " + book.name)
            print("Рік видання : " + book.year)
            print("Жанр        : " + book.genre)
            print("Автор       : " + book.author)
            print("=" * 13)
        else:
          print("Книг не знайдено")
      elif userInput == "4":
        bookAuthorInput = input("Автор книги: ")
        booksOutput   = lib1.getBooksByAuthor(bookAuthorInput)
        if booksOutput != []:
          for book in booksOutput:
            print("Назва       : " + book.name)
            print("Рік видання : " + book.year)
            print("Жанр        : " + book.genre)
            print("Автор       : " + book.author)
            print("=" * 13)
        else:
          print("Книг не знайдено")
      elif userInput == "0":
        break
      else:
        print("Не розпізнанно")
        continue
      break
  elif userInput == "5":
    bookIDInput = int(input("ID Книги: "))
    bookOutput  = lib1.removeBook(bookIDInput)
import mysql.connector


def Connect():
    try:
        connection = mysql.connector.connect(
            host='Localhost',
            user='root',
            password='',
            database='library'
        )

        return connection

    except mysql.connector.Error as err:
        print("Failed to access the Database!")
        return None



def Start():
    print("""
       MY LIBRARY
          
    [1] ADD TO READ 
    [2] I'M READING
    [3] UPDATE LISTS
    [4] SERACH BOOK
    [5] DELETE BOOK
    [6] EXIT
    
    """)

    return int(input("R = "))




def AddBook(connection):
    TitleBook = str(input("Enter the title of the book: "))
    AuthorBook = str(input("\ninform the author of the book: "))
    GenderBook = str(input("\nEnter the genre of the book: "))
    YearBook = int(input("\nEnter the year of the book: "))

    try:
        cursor = connection.cursor()
        command = f'INSERT INTO books (titlebook,authorbook,genderbook,yearbook) VALUES ("{TitleBook}","{AuthorBook}","{GenderBook}","{YearBook}")'
        cursor.execute(command)
        connection.commit()

    except mysql.connector.Error as err:
        print(f"error adding book: {err}")

    finally:
        cursor.close()



def ListBooks(connection):
    try:
        cursor = connection.cursor()
        command = f'SELECT * FROM books'
        cursor.execute(command)
        result = cursor.fetchall()

        for id,TitleBook,AuthorBook,GenderBook,YearBook in result:
            print(f'Id Book: {id}   Title Book: {TitleBook}   Author Book: {AuthorBook}   Gender Book: {GenderBook}   Year Book: {YearBook}')

    except mysql.connector.Error as err:
        print(f"error when listing books {err}")
    finally:
        cursor.close()


def UpdateBooks(connection):
    id = int(input("Enter the book code: "))

    print("repeat the name or year if you are not going to change it\n")
    NewTitle = str(input("New title: "))
    NewAuthor = str(input("\nNew author: "))
    NewGender = str(input("\nNew Gender: "))
    NewYear = int(input("\nNew Year: "))

    try:
        cursor = connection.cursor()
        command = f'UPDATE books SET titlebook = "{NewTitle}", authorbook = "{NewAuthor}", genderbook = "{NewGender}", yearbook = {NewYear} WHERE id = {id} '
        cursor.execute(command)
        connection.commit()

    except mysql.connector.Error as err:
        print(f"error when updating book: {err}")
    finally:
        cursor.close()



def DeleteBook(connection):
    id = int(input("Book ID to delete: "))

    try:
        cursor = connection.cursor()
        command = f'DELETE FROM books WHERE id = {id}'
        cursor.execute(command)
        connection.commit()
    
    except mysql.connector.Error as err:
        print(f"Error when deleting book: {err}")
    
    finally:
        cursor.close()




def SerachBook(connection):
    search = str(input("Enter the title, author or genre to search: "))

    try:
        cursor = connection.cursor()
        command = f''' 
                    SELECT * FROM books
                    WHERE titlebook LIKE %s OR authorbook LIKE %s OR genderbook LIKE %s'''
        search_pattern = f'%{search}%'
        cursor.execute(command, (search_pattern, search_pattern, search_pattern))
        result = cursor.fetchall()

        if result:
            for id, TitleBook, AuthorBook, GenderBook, YearBook in result:
                print(f'Id Livro: {id}   Título: {TitleBook}   Autor: {AuthorBook}   Gênero: {GenderBook}   Ano: {YearBook}')
        else:
            print("No book founds.")

    except mysql.connector.Error as err:
        print(f"Error when searching for books: {err}")
    finally:
        cursor.close()





def Main():
    connection = Connect()

    if not connection:
        return
    
    while True:
        option = Start()

        match option:
            case 1:
                AddBook(connection)
            case 2:
                ListBooks(connection)
            case 3:
                UpdateBooks(connection)
            case 4:
                SerachBook(connection)
            case 5:
                DeleteBook(connection)
            case 6:
                connection.close
                exit() 
            case _:
                print("Only numbers 1 to 5!")


if __name__ =='__main__':
    Main()


        

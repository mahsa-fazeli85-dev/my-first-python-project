
import csv


# =========================

class Book:

    def __init__(self, name, author, year, category):
        self.name = name
        self.author = author
        self.year = year
        self.category = category

    def show(self):
        print("نام کتاب:", self.name)
        print("نویسنده:", self.author)
        print("سال انتشار:", self.year)
        print("دسته‌بندی:", self.category)
        print("--------------------")


# =========================

class Library:

    def __init__(self):
        self.books = []
        self.filename = "books.csv"
        self.load_from_csv()

    # اضافه کردن کتاب
    def add_book(self, book):
        self.books.append(book)
        self.save_to_csv()

   
    def delete_book(self, number):

        if 1 <= number <= len(self.books):
            self.books.pop(number - 1)
            self.save_to_csv()
            print("کتاب با موفقیت حذف شد.")
        else:
            print("شماره وارد شده اشتباه است.")

  
    def show_books(self):

        if len(self.books) == 0:
            print("هیچ کتابی در کتابخانه وجود ندارد.")
            return

        print("\n===== کتاب‌های کتابخانه =====")

        for i, book in enumerate(self.books, start=1):
            print("شماره:", i)
            book.show()


    def save_to_csv(self):

        with open(self.filename, "w", newline="", encoding="utf-8-sig") as file:

            writer = csv.writer(file)

            writer.writerow([
                "name",
                "author",
                "year",
                "category"
            ])

            for book in self.books:
                writer.writerow([
                    book.name,
                    book.author,
                    book.year,
                    book.category
                ])

 
    def load_from_csv(self):

        try:

            with open(self.filename, "r", newline="", encoding="utf-8-sig") as file:

                reader = csv.DictReader(file)

                for row in reader:

                    book = Book(
                        row["name"],
                        row["author"],
                        row["year"],
                        row["category"]
                    )

                    self.books.append(book)

        except FileNotFoundError:
            pass



library = Library()


while True:

    print("\n===== مدیریت کتابخانه =====")
    print("1. اضافه کردن کتاب")
    print("2. حذف کتاب")
    print("3. نمایش کتاب‌ها")
    print("4. ذخیره کتاب‌ها")
    print("5. خروج")

    choice = input("انتخاب شما: ")

    # اضافه کردن کتاب
    if choice == "1":

        name = input("نام کتاب: ")
        author = input("نام نویسنده: ")
        year = input("سال انتشار: ")
        category = input("دسته‌بندی: ")

        book = Book(
            name,
            author,
            year,
            category
        )

        library.add_book(book)

        print("کتاب با موفقیت اضافه شد.")

    # حذف کتاب
    elif choice == "2":

        library.show_books()

        if len(library.books) > 0:

            number = int(input("شماره کتاب برای حذف: "))

            library.delete_book(number)

    
    elif choice == "3":

        library.show_books()

   
    elif choice == "4":

        library.save_to_csv()

        print("کتاب‌ها با موفقیت ذخیره شدند.")

    elif choice == "5":

        print("برنامه بسته شد.")
        break

    else:

        print("گزینه نامعتبر است.")


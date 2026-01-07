from Composite import File, Folder
class FileExplorerApp:
    @staticmethod
    def main():
        file1 = File('readme.txt', 10)
        file2 = File('profile.png', 100)
        file3 = File('employee.csv', 1000)

        documents = Folder('Documents')
        documents.add_item(file1)
        documents.add_item(file3)

        pictures = Folder('Pictures')
        pictures.add_item(file2)

        home = Folder('Home')
        home.add_item(documents)
        home.add_item(pictures)

        home.print_structure('')
        home.delete_item()

if __name__ == '__main__':
    FileExplorerApp.main()
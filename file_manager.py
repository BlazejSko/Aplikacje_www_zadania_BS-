class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        with open(self.file_name, "r") as file_reader:
            return file_reader.read()

    def update_file(self, text_data):
        with open(self.file_name, "a") as file_writer:
            file_writer.write(text_data)

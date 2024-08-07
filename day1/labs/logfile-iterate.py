# class LogFileIterator:
#     def __init__(self, file_path):
#         self.file_path = file_path
#         self.file = open(file_path, 'r')
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#
#         line = self.file.readline()
#         while line:
#             if line:
#                 if line.find("Health") != -1:
#                     return line.strip()
#             else:
#                 self.file.close()
#                 raise StopIteration
#
# # Usage
# log_file_path = 'large_log_file.txt'
# log_iterator = LogFileIterator(log_file_path)
#
# for line in log_iterator:
#     print(line)  # Process each line


# def log(path):
#     with open(path, 'r') as file:
#         for line in file:
#             if "Error" in line or "Exception" in line:
#                 yield line
#
# file = 'large_log_file.txt'
# for line in log(file):
#     print(line)


class LogFileIterator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(file_path, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if line:
            if 'Error' in line.strip():
                raise Exception("Error found")
            return line.strip()
        else:
            self.file.close()
            raise StopIteration


# Usage
log_file_path = 'large_log_file.txt'
log_iterator = LogFileIterator(log_file_path)

for line in log_iterator:
    print(line)  # Process each line

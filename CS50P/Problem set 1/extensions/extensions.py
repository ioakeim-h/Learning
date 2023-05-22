
import mimetypes

file_name = str(input("File name: ")).casefold().strip()
media_type = mimetypes.guess_type(file_name)[0]

print("application/octet-stream") if media_type == None else print(media_type)
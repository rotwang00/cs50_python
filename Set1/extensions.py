name = input("Enter the filename: ")

suffix = name.split(".")[-1]

match suffix:
  case "gif":
    print("image/gif")
  case "jpg" | "jpeg":
    print("image/jpeg")
  case "pdf":
    print("application/pdf")
  case "png":
    print("image/png")
  case "txt":
    print("txt/plain")
  case "zip":
    print("application/zip")
  case _:
    print("application/octet-strem")

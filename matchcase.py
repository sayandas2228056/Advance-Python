def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "Not Found "
        case 500:
            return "Internal Server Not Found "
        case _: #defalut case 
            return "Unidentified Error"
    
x :int =int(input("Enter your Error Input number"))
reply : str =http_status(x)
print(reply)

        
# Import socket module
from socket import *
import pandas as pd
#import pandas as pd
# Assign a port number

if __name__ == '__main__':
    serverPort = 12345
#Create a TCP server socket
# #(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind the socket to server address and server port
serverSocket.bind(('',serverPort))

#serverSocket.bind(('192.168.53.110', serverPort))

# Listen to at most 1 connection at a time
serverSocket.listen(1)
print("The server is ready to receive")
# Server should be up and running and listening to the incoming connections



while True:
    # Set up a new connection from the client
    connectionSocket, addr= serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    print(addr)
    print(sentence)
    ip = addr[0]
    port=addr[1]
    # list=sentence.split('/')
    request= sentence.split('/')
    R=request[1]
    print (R)

    port = addr[1]

    # Send the content of the requested 1 file to the client
    # when enter http://localhost:7000/1

    ss = R.split(' ')
    print ("*******************")
    rec = ss[0]
    print ("The Request")
    print (rec)
    print ("*******************")
    ss2=rec.split(".")

     # Handle redirects
    
    # to get index without HTTP


    if rec=='index.html'or rec==''or rec=="main_en.html" or rec =="en":
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        htmlFile = open("main_en.html",'rb')
        connectionSocket.send(htmlFile.read())

    elif rec=='ar':
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        htmlFile = open("main_ar.html",'rb')
        connectionSocket.send(htmlFile.read())   



    elif rec == 'SortByName':
        
        df = pd.read_csv("list.csv")
        sorted_df = df.sort_values(by=["name"], ascending=True)
        # to save data in a file after sorting
        sorted_df.to_csv('nameSort.csv', index=False)

        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())
        my_file = open("nameSort.csv", "r")
        content_list = my_file.readlines()
        html = " <html><head><title> sorted Name </title> <body> <h1><br><font color=\"red\"> Smart phone sorted name <br>  <font color=\"black\"> </h1> <h3><ol> <li> "+ content_list.__getitem__(0)  + "    <li>"+ content_list.__getitem__(1)  + " " \
            "   <li> "+ content_list.__getitem__(2)  + "   <li>  "+ content_list.__getitem__(3)  + "   <li> "+ content_list.__getitem__(4)  + "   <li> "+ content_list.__getitem__(5)  + " <li> "\
               + content_list.__getitem__(6)  + "  <li> "+ content_list.__getitem__(7)  + "  <li> "+ content_list.__getitem__(8)  + "  <li> "+ content_list.__getitem__(9)  + "  </ol>  </h3>"
        connectionSocket.send(html.encode())




    elif rec == 'SortByPrice':

        df = pd.read_csv("list.csv")
        sorted_df = df.sort_values(by=["price"], ascending=True)
        # to save data in a file after sorting
        sorted_df.to_csv('priceSort.csv', index=False)

        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: text/html \r\n".encode())
        connectionSocket.send("\r\n".encode())

        my_file = open("priceSort.csv", "r")
        content_list = my_file.readlines()
        html = " <html><head><title> sorted Price </title> <body> <h1><br><font color=\"red\"> Smart phone sorted Price <br>  <font color=\"black\"> </h1> <h3><ol> <li> " + content_list.__getitem__(0) + "" \
               "    <li>" + content_list.__getitem__(1) + "  <li> " + content_list.__getitem__(2) + "   <li>  " + content_list.__getitem__(3) + "   <li> " + content_list.__getitem__(4) + "" \
              "   <li> " + content_list.__getitem__(5) + " <li> " + content_list.__getitem__(6) + "  <li> " + content_list.__getitem__(7) + "  <li> " + content_list.__getitem__(8) + " " \
            " <li> " + content_list.__getitem__(9) + "  </ol>  </h3>"
        connectionSocket.send(html.encode())


    elif rec== 'azn':
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
        connectionSocket.send("Location: https://www.amazon.de/\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send("<html><body>Redirecting to Amazon Germany...</body></html>".encode())
        connectionSocket.close()

    elif rec== 'so':
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
        connectionSocket.send("Location: https://stackoverflow.com/\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send("<html><body>Redirecting to Stack Overflow...</body></html>".encode())
        connectionSocket.close()

    elif rec== 'bzu':
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
        connectionSocket.send("Location: https://ritaj.birzeit.edu//\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send("<html><body>Redirecting to Birzeit University...</body></html>".encode())
        connectionSocket.close()


    elif rec=='image.png':
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/png \r\n".encode())
        connectionSocket.send("\r\n".encode())
        s=open("laion1.png","rb")
        # Close the client connection socket
        connectionSocket.send(s.read())


    # Send the content of the requested 3 file to the client
    # when enter http://localhost:7000/3
    elif rec=='image.jpg':
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/jpeg \r\n".encode())
        connectionSocket.send("\r\n".encode())
        s=open("nature.jpg","rb")
        # Close the client connection socket
        connectionSocket.send(s.read())

    elif rec=='hope.jpg':
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/png \r\n".encode())
        connectionSocket.send("\r\n".encode())
        s=open("hope.jpg","rb")
        # Close the client connection socket
        connectionSocket.send(s.read())




    elif rec == 'gifback.gif':
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/png \r\n".encode())
        connectionSocket.send("\r\n".encode())
        s = open("gifback.gif", "rb")
        # Close the client connection socket
        connectionSocket.send(s.read())


    elif rec == 'me.jpg':
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/jpeg \r\n".encode())
        connectionSocket.send("\r\n".encode())
        s = open("me.jpg", "rb")
        # Close the client connection socket
        connectionSocket.send(s.read())

    elif rec == 'fxdatabase.png':
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/png \r\n".encode())
        connectionSocket.send("\r\n".encode())
        s = open("fxdatabase.png", "rb")
        # Close the client connection socket
        connectionSocket.send(s.read())


    elif rec == 'fxdatabase1.png':
        # Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send("Content-Type: image/png \r\n".encode())
        connectionSocket.send("\r\n".encode())
        s = open("fxdatabase1.png", "rb")
        # Close the client connection socket
        connectionSocket.send(s.read())

    elif len(ss2)==2:
       if ss2[1]=='html' :
          connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
          connectionSocket.send("Content-Type: text/html \r\n".encode())
          connectionSocket.send("\r\n".encode())
          htmlFile = open(rec,'rb')
          connectionSocket.send(htmlFile.read())
    

    else:
              connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
              connectionSocket.send("Content-Type: text/html; charset=ISO-8859-1\r\n".encode())
              n=addr[1]
              # Your HTML content
              html_content = f"<html><head><title> ERROR </title></head><body><h2>404 Not Found</h2><h1><font color=\"red\">The file is notfound</font></h1><h1><b>Mohamad Zaben, ID: 1202068</b></h1><h3>The IP:{addr[0]}</h3><h3>The PortNumber: {addr[1]}</h3></body></html>"

              # Send the Content-Length header
              connectionSocket.send(f"Content-Length: {len(html_content)}\r\n\r\n".encode())

            # Send the HTML content
              connectionSocket.send(html_content.encode())

               # Close the connection
              connectionSocket.close()
              #connectionSocket.close()


   


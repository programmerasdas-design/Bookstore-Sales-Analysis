import pandas as pd
import matplotlib.pyplot as plt 
data=pd.read_csv("Bookstore Sales Analysis.csv")
print(data.head())
print(data.tail())
plt.figure()
plt.plot(data["Day"],data["Revenue"],color="blue",marker="o")
plt.title("Total Revenue over time ")
plt.xlabel("Days")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()
plt.figure()
data_book=["Python Basics","Data Science Guide","Machine Learning","The Great Novel","Mystery Nights","World History"]
data1=[data[data["Book"]=="Python Basics"]["Revenue"].sum(),
    data[data["Book"]=="Data Science Guide"]["Revenue"].sum(),
    data[data["Book"]=="Machine Learning"]["Revenue"].sum(),
    data [data["Book"]=="The Great Novel"]["Revenue"].sum(),
    data[data["Book"]=="Mystery Nights"]["Revenue"].sum(),
    data [data["Book"]=="World History"]["Revenue"].sum()]
plt.bar(data_book,data1,color=["blue","skyblue","green","yellow","black","red"])
plt.title("Book Revenue Analysis")
plt.xlabel("books")
plt.ylabel("Revenue")
plt.show()
plt.figure()
data_book1=["Python Basics","Data Science Guide","Machine Learning","The Great Novel","Mystery Nights","World History"]
data2=[data[data["Book"]=="Python Basics"]["Quantity_Sold"].sum(),
       data[data["Book"]=="Data Science Guide"]["Quantity_Sold"].sum(),
       data[data["Book"]=="Machine Learning"]["Quantity_Sold"].sum(),
       data[data["Book"]=="The Great Novel"]["Quantity_Sold"].sum(),
       data[data["Book"]=="Mystery Nights"]["Quantity_Sold"].sum(),
       data[data["Book"]=="World History"]["Quantity_Sold"].sum()
    ]
plt.bar(data_book1,data2,color=["blue","skyblue","green","yellow","black","red"])
plt.title("Book Quantity sold Analysis")
plt.xlabel("BOOKS")
plt.ylabel("Quantity sold")
plt.show()
plt.figure()
category=["Programming","Fiction","Education"]
data3=[data[data["Category"]=="Programming"]["Quantity_Sold"].sum(),
       data[data["Category"]=="Fiction"]["Quantity_Sold"].sum(),
       data[data["Category"]=="Education"]["Quantity_Sold"].sum(),
        ]
plt.bar(category,data3,color=["red","green","orange"])
plt.title("category Quantity sold Analysis ")
plt.xlabel("Category")
plt.ylabel("Quantity sold")
plt.show()
plt.figure()
plt.scatter(data["Price"],data["Quantity_Sold"],color="blue")
plt.title("Price vs Quantity Sold")
plt.xlabel("price")
plt.ylabel("Quantity sold")
plt.show()
print(data[data["Category"]=="Fiction"]) #69
print(data[data["Category"]=="Education"]) #19
print(data[data["Category"]=="Programming"]) #101 

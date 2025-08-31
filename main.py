print("-------------------------------------------------------------------------------------")
print("------------------------------Welcome to Sales Data Summary--------------------------")
print("-------------------------------------------------------------------------------------")
print("\n")

# 📌 𝙎𝙩𝙚𝙥 1: 𝙎𝙩𝙤𝙧𝙞𝙣𝙜 𝙮𝙤𝙪𝙧 𝘿𝙖𝙩𝙖 🏬

sales =[
    {  "day": "Monday",
       "product": "Shirt",
       "amount": 1200
    },
    
    { "day": "Monday",
      "product": "Pant",
      "amount": 800
    },
    
    
    { "day": "Tuesday",
      "product": "Shirt",
      "amount": 1500
    },

    { "day": "Tuesday",
      "product": "Shoe",
      "amount": 2000
    },

    { "day": "Wednesday",
      "product": "Pant",
      "amount": 1000
    },

    { "day": "Wednesday",
      "product": "Shoe",
      "amount": 2500
    }
]

"""
📝 𝙉𝙤𝙩𝙚𝙨: 
👉 sales = [...] → আমাদের সব sales data একটা list এর মধ্যে রাখা হচ্ছে। আর এই second bracket মানেই বুঝবেন যে LIST!
👉 প্রতিটি item {} bracket এর মধ্যে dictionary আকারে → যেমন {"day": "Monday", "product": "Shirt", "amount": 1200}
আর সবসময় মনে রাখবেন Third Bracket {} মানে হচ্ছে Dictionary।
👉 "day": "Monday" → এর মানে যে কোন দিনে sale হয়েছে
👉 "product": "Shirt" → কোন product বিক্রি হয়েছে
👉 "amount": 1200 → কত টাকার বিক্রি হয়েছে
"""



# 📌 𝙎𝙩𝙚𝙥 2: 𝙁𝙞𝙜𝙪𝙧𝙚 𝙤𝙪𝙩 𝙏𝙤𝙩𝙖𝙡 𝙎𝙖𝙡𝙚𝙨 💰
total_sales = 0
for record in sales:
    total_sales += record["amount"]  
print("Total Sales: ", total_sales)
print("\n")
    

# 📌 𝙎𝙩𝙚𝙥 3: 𝙒𝙝𝙞𝙘𝙝 𝙋𝙧𝙤𝙙𝙪𝙘𝙩 𝙜𝙤𝙩 𝙢𝙤𝙨𝙩 𝙨𝙖𝙡𝙚𝙨 𝙩𝙞𝙡𝙡 𝙣𝙤𝙬? 🚀
product_sales = {}                      #faka  dictionary toiri korlam.record gula store kore rakhbo.
for record in sales:                    # sales list k record er moddhe niye aslam.
    product = record["product"]         # ekhon record er moddhe theke product name ta niye aslam.
    amount =  record["amount"]          # ekhon record er moddhe theke amount ta niye aslam.
    
    if product in product_sales:        # jodi product ta product_sales dictionary te thake tahole
        product_sales[product] += amount   # oi product er amount er sathe notun amount ta jog kore dibo.
    else:
        product_sales[product] = amount    # jodi product ta product_sales dictionary te na thake tahole oi product er amount ta set kore dibo.
       
 
print("Product Wise Sales: ", product_sales)     # product_sales dictionary ta print korlam.       
print ("Most Sold Product: ", max(product_sales, key=product_sales.get)) # max function er maddhome product_sales dictionary theke jeta beshi amount seta ber kore print korlam.
print("\n")


#📌 𝙎𝙩𝙚𝙥 4 : 𝙁𝙞𝙜𝙪𝙧𝙚 𝙊𝙪𝙩 𝘼𝙫𝙚𝙧𝙖𝙜𝙚 𝙎𝙖𝙡𝙚𝙨 🔥
average_sales = total_sales / len(sales)  # total_sales ke sales list er length diye vag kore average ber korlam.
print("Average Sales Per Record: ", average_sales)    # average_sales print korlam.
print("\n")


#📌 𝙎𝙩𝙚𝙥 5: 𝙏𝙝𝙚 𝘽𝙚𝙨𝙩 𝙎𝙖𝙡𝙚 𝘿𝙖𝙮 🗓

day_sales = {}                      # faka dictionary toiri korlam. record gula store kore rakhbo.

for record in sales:
    day = record["day"]              # ekhon record er moddhe theke day ta niye aslam.
    amount = record["amount"]        # ekhon record er moddhe theke amount ta niye aslam.
    
    if day in day_sales:             # jodi day ta day_sales dictionary te thake tahole
        day_sales[day] += amount     # oi day er amount er sathe notun amount ta jog kore dibo.
    else:
        day_sales[day] = amount      # jodi day ta day_sales dictionary te na thake tahole oi day er amount ta set kore dibo.
    
print("Day Wise Sales: ", day_sales)   # day_sales dictionary ta print korlam.
print("Best Sales Day: ", max(day_sales, key=day_sales.get))  
print("\n")

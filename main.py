from datetime import datetime,timedelta
import requests,time

def EnterQuery():
    while True:
             try:
                     print("Which topic you are interested in today?\n1.Technology\n2.Business\n3.Health\n4.Entertainment\n5.Anything else.")
                     choice=int(input("Enter your choice:"))
                     match (choice):
                         case 1:
                             
                             return "technology"
                         case 2: 
                                   return "business"
                         case 3: 
                             return "health"
                         case 4:
                             
                             return "entertainment"
                         case 5:
                               return input("Enter a topic to search for:")
                         case _:
                             raise ValueError
                     print("*"*70)
             except ValueError:
                  print("You entered the wrong input, try again")
             except Exception as e:
                  print("Some error occured!",e)
   
def fetch_data(main_url,trusted_publishers):
    
     i = requests.get(main_url)
     print("\n")
     data = i.json()
     
     articles = data["articles"]

     articles.sort(key=lambda x: 0 if any(pub.lower() in x['source']['name'].lower() for pub in trusted_publishers) else 1)

     for index,article in enumerate(articles[:30]):
          print("🏷️ ",index+1,"Title-",article["title"])
          print("🗞️  Publisher-",article["source"]["name"])
          print("🧾  Description-",article["description"])
          print("\n")
          print("🔗Click here to read full article:",article["url"])
          print("\n*********************************************************************\n")
          time.sleep(1)

def main():
     user_Query = EnterQuery()
     tech_publishers = [
         "TechCrunch", "Wired", "The Verge", "Engadget", "CNET",
         "Ars Technica", "Gizmodo", "Mashable", "Digital Trends",
         "ZDNet", "VentureBeat", "The Information", "Android Authority",
         "MacRumors", "9to5Mac"
     ]
     
     health_publishers = [
         "WebMD", "Healthline", "Mayo Clinic", "Medical News Today",
         "NHS", "Johns Hopkins Medicine", "Harvard Health Publishing",
         "The Lancet", "WHO", "CDC", "Verywell Health", "Medscape"
     ]
     
     business_publishers = [
         "Bloomberg", "Forbes", "CNBC", "Financial Times",
         "The Wall Street Journal", "Business Insider", "The Economist",
         "Fortune", "MarketWatch", "Yahoo Finance", "Reuters Business",
         "Economic Times", "Mint", "Barron's"
     ]
     
     entertainment_publishers = [
              "Variety", "Hollywood Reporter", "Entertainment Weekly",
         "Rolling Stone", "BuzzFeed", "MTV News", "Collider",
         "People", "E! News", "Billboard", "The Wrap", "Vulture"
     ]
     
     global trusted_publishers
     trusted_publishers = (
         tech_publishers +
          health_publishers +
          business_publishers +
          entertainment_publishers +
          ["BBC", "BBC News", "CNN", "Reuters", "The New York Times", "The Guardian"]
      )
     
     today = datetime.today()
     from_date =(today - timedelta(days=30)).strftime("%Y-%m-%d")
     api_key= "____"
    # 🔑 Please get your own (free) API key from <https://newsapi.org/> and insert it in the script above.
    
     url = f"https://newsapi.org/v2/everything?q={user_Query}&from={from_date}&sortBy=publishedAT&size=30&apiKey={api_key}"
          
     fetch_data(url,trusted_publishers)
     print("\n*********************************************************************")
     url1 = url
     return url1

trusted_publishers = ()

main_url = main()
use_again="yes"
while(True):
     use_again=input("Do you want to use News API again (yes/no):").strip().lower()
     if use_again==("yes"):
          main()
     else:
          print("BYE!!")
          break    

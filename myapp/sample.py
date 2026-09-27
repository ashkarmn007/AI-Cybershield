def requestReview(apk):
    from google_play_scraper import app, reviews
    def get_reviews(package_name, count=5):
        try:
            result, _ = reviews(package_name, lang='en', count=count)  # ✅ unpack correctly
            return result
        except Exception as e:
            print(f"Error: {e}")
            return None

    package_name = apk
    review_count = 200
    app_reviews = get_reviews(package_name, count=review_count)
    lst = []
    rating = []
    i = 0
    if app_reviews:
        print("App Reviews:")
        for review in app_reviews:
            try:
                i += 1
                print(i, "==============================")
                lst.append(review['content'])
                rating.append(float(review['score']))
                print("-" * 50)
            except Exception as e:
                print("Error parsing review:", e)
        if rating:
            print("----------------------------------------------------------------------------------------------------")
            avg_rating = sum(rating) / len(rating)
            print("Average Rating:", avg_rating,"***********************************************************************")
            if avg_rating >= 3.0:
                res="Non-Malicious"
            else:
                res="Malicious"
            print(res,"#############")

        else:
            avg_rating = None
    else:
        print("Failed to fetch reviews.")
        avg_rating = None
    p, n, nu = sent(lst)
    s = avg_rating if avg_rating is not None else "na"
    print(p, n, nu, "Sentiment Analysis Result")
    if rating:
        print("----------------------------------------------------------------------------------------------------")
        avg_rating = sum(rating) / len(rating)
        print("Average Rating:", avg_rating, "***********************************************************************")
        if avg_rating >= 3.1:
            res = "Non-Malicious"
        else:
            res = "Malicious"


    else:
        res = "Not Found"
    return res

def sent(k):
    import nltk
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    pstv=0
    ngtv=0
    ntl=0
    sid = SentimentIntensityAnalyzer()
    for sentence in k:
        ss = sid.polarity_scores(sentence)
        # print(ss)
        a = float(ss['pos'])
        b = float(ss['neg'])
        c = float(ss['neu'])
        if a==0 and b==0:
            ntl+=1
        elif a > b:
                pstv = pstv + 1
        else:
                ngtv=ngtv+1
    return pstv,ngtv,ntl

# print(requestReview("com.bitel.selfcare"))
# print(requestReview("com.whatsapp"))
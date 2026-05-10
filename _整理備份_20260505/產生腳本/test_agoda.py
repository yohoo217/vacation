import urllib.request
url = "https://www.agoda.com/zh-tw/richmond-hotel-obihiro-ekimae/hotel/tokachi-jp.html?countryId=140&finalPriceView=1&isShowMobileAppPrice=false&cid=1917614&numberOfBedrooms=&familyMode=false&adults=2&children=0&rooms=1&maxRooms=0&checkIn=2026-05-16&isCalendarCallout=false&childAges=&numberOfGuest=0&missingChildAges=false&travellerType=1&showReviewSubmissionEntry=false&currencyCode=TWD&isFreeOccSearch=false&los=1"
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    print("Status:", response.status)
except Exception as e:
    print("Error:", e)

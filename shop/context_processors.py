# 社交媒體連結處理器
# Social Media Links Processor
def social_links(request):
    # 返回社交媒體連結列表，包含名稱、URL和圖示
    # Return a list of social media links with name, URL and icon
    return {
        "social_links": [
            {"name": "ig", "url": "https://www.instagram.com/sunbirds_official/", "icon": "img/ig.png"},
            {"name": "X", "url": "https://twitter.com/sun_SUNBIRDS", "icon": "img/x.png"},
            {"name": "yt", "url": "https://www.youtube.com/channel/UCblYfXF_9LSpYgf2eZmmGKQ", "icon": "img/youtube.png"},
            {"name": "line", "url": "https://lin.ee/oNzYPlg", "icon": "img/line.png"},
            {"name": "tk", "url": "https://www.tiktok.com/@sunbirds_official", "icon": "img/tiktok.png"},
        ]
    }

# 關於我們連結處理器
# About Us Links Processor
def about_links(request):
    # 返回相關組織連結列表，包含名稱、URL和圖示
    # Return a list of related organization links with name, URL and icon
    return{
        "about_links":[
            {"name": "jva", "url": "https://www.jva.or.jp/", "icon": "img/jva.png"},
            {"name": "sv", "url": "https://www.vleague.jp/", "icon": "img/sv.png"},
            {"name": "sun", "url": "https://www.suntory.co.jp/culture-sports/sungoliath/", "icon": "img/sun.png"},
        ]
    }

def social_links(request):
    return {
        "social_links": [
            {"name": "ig", "url": "https://www.instagram.com/sunbirds_official/", "icon": "img/ig.png"},
            {"name": "X", "url": "https://twitter.com/sun_SUNBIRDS", "icon": "img/x.png"},
            {"name": "yt", "url": "https://www.youtube.com/channel/UCblYfXF_9LSpYgf2eZmmGKQ", "icon": "img/youtube.png"},
            {"name": "line", "url": "https://lin.ee/oNzYPlg", "icon": "img/line.png"},
            {"name": "tk", "url": "https://www.tiktok.com/@sunbirds_official", "icon": "img/tiktok.png"},
        ]
    }

def about_links(request):
    return{
        "about_links":[
            {"name": "jva", "url": "https://www.jva.or.jp/", "icon": "img/jva.png"},
            {"name": "sv", "url": "https://www.vleague.jp/", "icon": "img/sv.png"},
            {"name": "sun", "url": "https://www.suntory.co.jp/culture-sports/sungoliath/", "icon": "img/sun.png"},
        ]
    }

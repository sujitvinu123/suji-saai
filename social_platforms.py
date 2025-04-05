IMPORTANT_PLATFORMS = {
    # Major Social Networks
    'instagram': 'https://instagram.com/{}',
    'facebook': 'https://facebook.com/{}',
    'twitter': 'https://twitter.com/{}',
    'linkedin': 'https://linkedin.com/in/{}',
    'youtube': 'https://youtube.com/{}',
    'tiktok': 'https://tiktok.com/@{}'
}

SECONDARY_PLATFORMS = {
    # Professional Networks
    'github': 'https://github.com/{}',
    'medium': 'https://medium.com/@{}',
    'behance': 'https://behance.net/{}',
    'dribbble': 'https://dribbble.com/{}',
    
    # Photo & Video Sharing
    'pinterest': 'https://pinterest.com/{}',
    'snapchat': 'https://snapchat.com/add/{}',
    'twitch': 'https://twitch.tv/{}',
    
    # Other Major Platforms
    'reddit': 'https://reddit.com/user/{}',
    'tumblr': 'https://{}.tumblr.com',
    'discord': 'https://discord.com/users/{}'
}

OTHER_PLATFORMS = {
    # Professional
    'gitlab': 'https://gitlab.com/{}',
    'bitbucket': 'https://bitbucket.org/{}',
    'stackoverflow': 'https://stackoverflow.com/users/{}',
    'fiverr': 'https://fiverr.com/{}',
    'upwork': 'https://upwork.com/freelancers/{}',
    
    # Blogging
    'wordpress': 'https://{}.wordpress.com',
    'blogger': 'https://{}.blogspot.com',
    'wix': 'https://{}.wix.com',
    'weebly': 'https://{}.weebly.com',
    
    # Photo Sharing
    'flickr': 'https://flickr.com/photos/{}',
    '500px': 'https://500px.com/{}',
    'deviantart': 'https://deviantart.com/{}',
    'vsco': 'https://vsco.co/{}',
    
    # Video
    'vimeo': 'https://vimeo.com/{}',
    'dailymotion': 'https://dailymotion.com/{}',
    
    # Music
    'soundcloud': 'https://soundcloud.com/{}',
    'spotify': 'https://open.spotify.com/user/{}',
    'lastfm': 'https://last.fm/user/{}',
    
    # Gaming
    'steam': 'https://steamcommunity.com/id/{}',
    'xbox': 'https://xboxgamertag.com/search/{}',
    'playstation': 'https://psnprofiles.com/{}',
    
    # Others
    'quora': 'https://quora.com/profile/{}',
    'goodreads': 'https://goodreads.com/{}',
    'wattpad': 'https://wattpad.com/user/{}',
    'fanfiction': 'https://fanfiction.net/u/{}',
    'aboutme': 'https://about.me/{}',
    'angellist': 'https://angel.co/{}',
    'crunchbase': 'https://crunchbase.com/person/{}',
    'gravatar': 'https://gravatar.com/{}',
    'keybase': 'https://keybase.io/{}',
    'slideshare': 'https://slideshare.net/{}',
    'speakerdeck': 'https://speakerdeck.com/{}',
    'tripadvisor': 'https://tripadvisor.com/members/{}',
    'wikipedia': 'https://wikipedia.org/wiki/User/{}'
}

# Combine all platforms
SOCIAL_PLATFORMS = {**IMPORTANT_PLATFORMS, **SECONDARY_PLATFORMS, **OTHER_PLATFORMS} 
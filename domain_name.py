from tld import get_tld

def get_domain_name(url):
    domain_name = get_tld(url) #from https://www.facebook.com to facebook.com
    return domain_name
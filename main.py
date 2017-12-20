import pynder
import robobrowser
import re
import requests
import configparser

password = "Zoolander69"
phone = "64274699089"



def get_access_token(email, password, ua, url):
    s = robobrowser.RoboBrowser(user_agent = ua, parser = "lxml")
    s.open(url)
    ##submit login form
    f = s.get_form()
    f["pass"] = password
    f["email"] = email
    s.submit_form(f)
    ##click OK button on the dialog informing you that you have already authenticated with the tinder AppleWebKit
    f = s.get_form()
    s.submit_form(f, submit = f.submit_fields['__CONFIRM__'])
    #get access token from the http response
    access_token = re.search(r"access_token=([\w\d]+)", s.response.content.decode()).groups()[0]
    return access_token


def main():
    print("let's begin ok")
    requests.packages.urllib3.disable_warnings()  # Find way around this...
    config = configparser.ConfigParser(interpolation=None)
    config.read('config.ini')
    auth = str(config['DEFAULT']['FACEBOOK_AUTH_TOKEN'])





if __name__ == '__main__':
    main()

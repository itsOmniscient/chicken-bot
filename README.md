I have only made this bot to practice some of the features that Selenium offers, it is not made for anyone's use but mine. BUT, in case you want to use it yourself, first you need to make some changes.

1. Download and install Mozilla Firefox.
2. Download Geckodriver from https://github.com/mozilla/geckodriver/releases and place the folder in the root directory of this project.
3. Add the geckofolder to PATH
4. Open run.py with any editor and edit line 25, instead of using "firefox_path" which is a variable, put the path to your Mozilla Firefox profile directory, e.g fp = webdriver.FirefoxProfile('C:\\Users\\your_username\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\your_profile_name')
5. Run run.py :)

NOTE: If you are getting captcha error, on line 26 delete "options=options", and edit line 52 where instead of wait(), type time.sleep(60) or however many seconds, so a browser can open and you can solve the captcha before the bot proceeds. Also open Mozilla and type about:config, search for "dom.webdriver.enabled" and make sure its on False, this should essentially bypass the triggering of captcha, most of the times. It doesn't always work but its a 50/50 solution for now until a proper bypass comes in the future.

# Controls themes (light/dark mode)
class ThemeMgr:

    # True for dark mode, False for light mode
    darkMode = False

    # Can set up with light or dark mode
    def __init__(self, darkMode):
        self.darkMode = darkMode

    # True -> False, False -> True; switch between themes
    def toggleDarkMode(self):
        self.darkMode = not self.darkMode

    # Returns True if dark mode, False if light mode
    def getDarkMode(self):
        return self.darkMode

    # Returns the background color based on theme
    def getBgColor(self):
        if self.darkMode:
            return (51,51,51) # dark grey background
        else:
            return (255,255,255) # white background

    # Returns the font color based on themes
    def getFontColor(self):
        if self.darkMode:
            return (255,255,255) # white text
        else:
            return (0,0,0) # black text

    # Get the filename for images
    # Dark mode: return "images/" + "dark_" + default filename
    # Light mode: return "images/" + default filename
    def getFileName(self,defFilename):
        if self.darkMode:
            return "images/" + "dark_"+ defFilename
        else:
            return "images/" + defFilename

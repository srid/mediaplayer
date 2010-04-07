from abc import ABCMeta, abstractmethod, abstractproperty

import psutil


class IMediaPlayer:
    """API for accessing a media player"""
    __metaclass__ = ABCMeta
    
    def is_running(self):
        """Is the media player process running?"""
        return _psrunning(self.procname)
        
    @abstractmethod
    def is_playing(self):
        """Is the media player playing media?"""
        
    def get_volume(self): pass
    def set_volume(self, value): pass
    volume = abstractproperty(get_volume, set_volume,
                              doc="Return or set volume: 0..100")
        
        
class IAudioPlayer(IMediaPlayer): pass


class IVideoPlayer(IAudioPlayer): pass

    
class WinampWindows(IAudioPlayer):
    """http://www.shalabh.com/software/winamp.py"""
    
    procname = 'winamp.exe'
    
    
class iTunesWindows(IAudioPlayer):
    
    procname = 'iTunes.exe'
    
    
class VLCWindows(IVideoPlayer):
    
    procname = 'vlc.exe'
        
    
class TotemUnix(IVideoPlayer):
    pass
    
    
class iTunesOSX(IAudioPlayer):
    pass
    

def _psrunning(name):
    for proc in psutil.get_process_list():
        if proc.name == name:
            return True
    return False

def main():
    print "Hello World"

import vlc
import time

from scheduler_composer import SchedulerComposer
from scheduler_builder import build

scheduler_composer = SchedulerComposer()

if __name__ == '__main__':
    media_player: vlc.MediaPlayer = vlc.MediaPlayer()
    mrl = "test.mp4"
    media_player.set_mrl(mrl)

    time.sleep(5)
    media_player.play()
    filename = "example.json"
    schedule = build(filename)
    scheduler_composer.add(filename, schedule)
    schedule.start()

    # getting width at index 0
    value = media_player.video_get_width(0)

    # printing width
    print("Width at Index 0 : ")
    print(value)

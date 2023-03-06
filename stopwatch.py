import time

class Stopwatch:
    def __init__(self):
        self._start_time = None
        self._total_elapsed_time = 0
        self._is_running = False


    def start(self):
        if not self.has_started():
            self._is_running = True
            self._start_time = time.time()
        else:
            raise RuntimeError("Attempted to start an already running Stopwatch instance")


    def has_started(self):
        return self._is_running and self._total_elapsed_time == 0


    def pause(self):
        if self._is_running:
            self._is_running = False
            self._total_elapsed_time += time.time() - self._start_time


    def is_paused(self):
        return not self._is_running


    def resume(self):
        if not self._is_running:
            self._is_running = True
            self._start_time = time.time()


    def get_elapsed_time(self):
        if self._is_running:
            return self._total_elapsed_time + (time.time() - self._start_time)
        else:
            return self._total_elapsed_time
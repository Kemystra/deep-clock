import time

from deep_clock import stopwatch

watch = stopwatch.Stopwatch()

def test_start():
    now = time.time()
    watch.start()

    # Using round to account for CPU cycle delay
    assert round(time.time() - now) == round(watch.get_elapsed_time())

def test_time():
    prev_time = watch.get_elapsed_time()
    time.sleep(1)
    now_time = watch.get_elapsed_time()

    assert round(prev_time + 1) == round(now_time)

def test_pausing():
    watch.pause()
    prev_time = watch.get_elapsed_time()

    time.sleep(1)
    curr_time = watch.get_elapsed_time()

    assert curr_time == prev_time

def test_resuming():
    prev_time = watch.get_elapsed_time()
    watch.resume()

    time.sleep(1)
    curr_time = watch.get_elapsed_time()

    assert prev_time != curr_time
    assert round(curr_time) == round(prev_time + 1)
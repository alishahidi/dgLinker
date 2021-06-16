from modules import loading

# register signal
loading.signal.signal(loading.signal.SIGINT,loading.signal_exit_handler)

loading.loading();

run = True

while run:
    if loading.run() == False:
        run = False

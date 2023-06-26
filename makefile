.PHONY = install
.PHONY = uninstall
.PHONY = update

install:
	chmod +x main.py
	sudo cp ./main.py /usr/bin/mkmf
	sudo rsync -a makefiles/* /usr/share/mkmf/

update:
	sudo cp ./main.py /usr/bin/mkmf
	sudo rsync -a makefiles/* /usr/share/mkmf/

uninstall:
	sudo rm -rf /usr/share/mkmf/* /usr/bin/mkmf

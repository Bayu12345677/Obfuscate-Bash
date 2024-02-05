setup:
	apt-get update
	apt-get upgrade
	apt-get install python ruby ncurses-utils coreutils pv mc
	apt-get install ossp-uuid figlet toilet figlet bc xz-utils
	pip install -r mod.txt
	gem install lolcat
	@echo "[?] sukses silakan jalankan perintah make run"
	
run:
	python main.sh.py

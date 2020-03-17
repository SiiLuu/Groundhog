##
## EPITECH PROJECT, 2019
## CNA_groundhog_2018
## File description:
## Makefile
##

all:
	cp groundhog.py groundhog
	chmod +x groundhog

clean:

fclean: clean
	rm groundhog

re: fclean all
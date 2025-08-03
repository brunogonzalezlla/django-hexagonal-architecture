BLUE = \033[0;34m
NC = \033[0m
LINE = --------------------------------------------------------------------


start:
	@echo "\n${BLUE}Starting Django Hexagonal Architecture project.\n${LINE}${NC}"
	@python src/manage.py runserver

makemigrations:
	@echo "\n${BLUE}Running makemigrations.\n${LINE}${NC}"
	@python src/manage.py makemigrations

migrate:
	@echo "\n${BLUE}Running migrate.\n${LINE}${NC}"
	@python src/manage.py migrate

new-day: ## create new folder with empty files usage: make new-day name=name_of_directory
ifdef name
	mkdir $(name)
	cd $(name);touch "$(name).py";touch "input.txt"
else
	echo "Name argument is empty"
	echo "usage: make new-day name=name_of_directory"
endif

help: ## print this message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
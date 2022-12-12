def user_info(first_name, last_name = "unkown", age = 45):
    print(f"Your first name is {first_name}")
    print(f"Your last name is {last_name}")
    print(f"Your age is {age}")

user_info("harshit", "sarpal" , 18)
    
    # default parameter ham last me bna sakte ha 
    # for example if we make first name default kiya to eroor ayga

    # teno default ho agar

    # ---> if we make last thing defaut then if we give age in calling function 18 and default is 45
    # then default age is ove right calling age 
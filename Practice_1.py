email = input("Enter Your Email: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
print("The Username is:"+username)
print("The Domain is:"+domain_name.upper())
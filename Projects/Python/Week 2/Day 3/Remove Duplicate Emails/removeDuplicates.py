list = ['1', '2', '3']
str = ','.join(list)

print(str)


with open("Python/Week 2/Day 3/Remove Duplicate Emails/emails.txt") as file: 
  content = file.read() 

emails = content.split(",")

duplicate_free_emails = [] 

for individual_email in emails: 
  email_without_space = individual_email.strip()
  if email_without_space not in duplicate_free_emails:
    duplicate_free_emails.append(email_without_space)
  
print(duplicate_free_emails)

with open("Python/Week 2/Day 3/Remove Duplicate Emails/duplicate-free-email-list.txt","w") as file: 
  result = "\n".join(duplicate_free_emails)
  file.write(result)
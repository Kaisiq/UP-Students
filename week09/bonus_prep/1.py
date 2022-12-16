def generate_username(first_name, last_name, email):
    n = len(email)
    n_last_name = len(last_name)
    for i in range(n):
        if email[i] == '@':
            if email[i+1:n] == 'gmail.com':
                return email[:i] + '.' + last_name[2::-1]
            elif '.' in email[i+1:n]:
                return first_name[:5] + '_' + last_name[n_last_name - 5:]

    return "Wrong email! Can't make username without valid email"

print(generate_username('Kristian', 'Ivanov', 'kfivanov24@gmail.com'))
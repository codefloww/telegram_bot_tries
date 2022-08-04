def get_admins():
    admins = []
    with open("data/admins.txt", "r") as admins_file:
        for line in admins_file.readlines():
            line = line.strip()
            user_id = int(line)
            admins.append(user_id)

    return admins


def add_admin(user_id):
    if user_id in get_admins():
        return

    with open("data/admins.txt", "a") as admins_file:
        admins_file.write(str(user_id) + "\n")


def remove_admin(user_id):
    # Отримуємо список адмінів
    admins = get_admins()

    # Якщо адміна з таким айді немає, нічого не робимо
    if user_id not in admins:
        return

    # Видаляємо адміна зі списку
    admins.remove(user_id)

    # Очищуємо файл адмінів
    open("data/admins.txt", "w").close()

    # Додаємо назад всіх адмінів окрім видаленого
    for admin in admins:
        add_admin(admin)


def get_channels():
    channels = []
    with open("data/channels.txt", "r") as channels_file:
        for line in channels_file.readlines():
            line = line.strip()
            user_id = int(line)
            channels.append(user_id)

    return channels


def add_channel(user_id):
    if user_id in get_channels():
        return

    with open("data/channels.txt", "a") as channels_file:
        channels_file.write(str(user_id) + "\n")


def remove_channel(user_id):
    channels = get_channels()

    if user_id not in channels:
        return

    channels.remove(user_id)

    open("data/channels.txt", "w").close()

    for channel in channels:
        add_channel(channel)

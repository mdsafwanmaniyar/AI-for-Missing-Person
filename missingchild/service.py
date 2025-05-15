from missingchild.models import MissingPersonModel


def getmissingpersons(username):

    persons = []

    for person in MissingPersonModel.objects.all():

        if username not in "admin":
            if person.userid==username:
                person.image = str(person.image).split("/")[1]
                persons.append(person)
        else:
            person.image = str(person.image).split("/")[1]
            persons.append(person)

    return persons
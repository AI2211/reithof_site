from django.contrib.auth.models import BaseUserManager

class ProfileUserManager(BaseUserManager):
    def create_user(self, vorname, nachname, email, password):
        if not vorname:
            raise ValueError("Vorname muss eingetragen sein!")
        if not nachname:
            raise ValueError("Nachname muss eingetragen sein!")
        if not email:
            raise ValueError("Eine E-Mail-Adresse muss eingetragen sein!")
        if not password:
            raise ValueError("Passwort muss eingetragen sein!")


        user = self.model(
            email=self.normalize_email(email),
            vorname=vorname,
            nachname=nachname,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, vorname, nachname, email, password):
        user = self.create_user(vorname, nachname, email, password)
        user.username = email
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

    #def get_by_natural_key(self, email):
     #   return self.get(**{self.model.USERNAME_FIELD: email})
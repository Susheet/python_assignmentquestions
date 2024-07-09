APP_NAME = input("Enter app name :")
ORG_NAME = input("Enter org name :")
TEAM_NAME = input("Enter team name :")
APP_NAME = APP_NAME.strip().replace(" ", "-").replace("_", "-").replace("som-vdi-", "").replace("som-fss-", "").lower()
APP_NAME = f"{ ORG_NAME }-{ TEAM_NAME  }-{APP_NAME}"

print(APP_NAME)
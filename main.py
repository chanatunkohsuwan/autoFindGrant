from sys import exit
import fetcher # should we do fetcher import * instead?
test_mode = True


if __name__ == "__main__":
    if test_mode:
        team_number = 5190
        response = fetcher.gather_team_info(team_number)
        sponsors = fetcher.get_sponsors(response["website"])
        with open("output.out", "w", encoding="utf-8") as f:
            for key, value in response.items():
                f.write(f"{key}: {value}\n")
                f.write(f"\n\n\nSponsors: {sponsors}\n")

    else:
        try:
            team_number = int(input("Enter a FRC team number"))
        except TypeError:
            raise TypeError("Team number (input) must be an integer")
        if not 0 < team_number < 10000:
            raise ValueError("Invalid team number, range = 1 - 9999")

        teamData = {}
        teamData = fetcher.gather_team_info

        fetcher.get_sponsors(teamData["website_url"])





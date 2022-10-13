import C2Database
import main, color, banner

if __name__ == "__main__":
    banner.PrintBanner()
    banner.HelpBanner()
    conn = C2Database.ConnectDatabase.Connect()
    main.Start(conn)
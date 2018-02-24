# Schedule retrieval of Coinmarketcap data

this script get data from coinmarketcap and dumps it into sqlite database.
this script is scheduled using launchd on OSX.

this is the schedule file

    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
    <dict>
        <key>Label</key>
        <string>com.crypto.launched.coinmarketcap_data</string>
        <key>ProgramArguments</key>
        <array>
            <string>/Users/vincent/venv/bin/python</string>
            <string>/Users/vincent/Workspace/coinmarketcap_data/coinmarketcap_data.py</string>
            <string></string>
        </array>
        <key>RunAtLoad</key>
        <true/>
        <key>StartInterval</key>
        <integer>21600</integer>
        <key>StandardOutPath</key>
        <string>/tmp/turtle.out</string>
        <key>StandardErrorPath</key>
        <string>/tmp/turtle.err</string>
    </dict>
    </plist>

you can find the script, venv, interval, log files in the xml structure.

to schedule the task:


    launchctl load /Users/vincent/Library/LaunchAgents/com.crypto.launched.coinmarketcap_data.plist 
    launchctl start com.crypto.launched.coinmarketcap_data


to remove scheduled task:
    
    launchctl stop com.crypto.launched.coinmarketcap_data
    launchctl remove com.crypto.launched.coinmarketcap_data

to verify script:

    sudo tail -f /var/log/system.log &
    cat tmp/turtle.err
    cat tmp/turtle.out
    
more info check these links:

https://stackoverflow.com/questions/15990512/launchctl-minimal-working-example-with-python
http://killtheyak.com/schedule-jobs-launchd/



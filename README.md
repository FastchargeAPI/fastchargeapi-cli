# fastchargeapi-cli

Official CLI tool for managing accounts and apps on [FastchargeAPI](https://fastchargeapi.com). Visit the [official 
documentation](https://doc.fastchargeapi.com) for usage.


## Installation

```
pip3 install fastchargeapi-cli
```

## Basic usage

### API publishers

`fastcharge account info`: Show information regarding your account.

`fastcharge app create [APP_NAME]`: Create a new app.

`fastcharge api add [APP_NAME] --path /:path --destination https://myservice.com/:path`: Add a route mapping `[APP_NAME].fastchargeapi.com/:path` to your app at `https://myservice.com/:path`.

`fastcharge pricing add [APP_NAME] --name "Free" --monthly-charge 0 --charge-per-request 0 --free-quota 100`: Add a pricing plan for your app.

`fastcharge app publish [APP_NAME]`: Make your app discoverable by other users.

### API subscribers

`fastapi subscription add [APP_NAME] --plan "Free"`: Subscribe to an app.

`fastapi token create [APP_NAME]`: Create a token to authenticate HTTP requests.

`curl 'https://[APP_NAME].fastchargeapi.com/path' --data '{"Authorization": [TOKEN]}'`: Make an request.



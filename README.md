# TomatosPump.funKOTHtradingBot

NOTE: THIS IS A WORK IN PROGRESS AND IS NOT GUARENTEED TO MAKE YOU ANY MONEY. DO YOUR OWN RESEARCH AND DON'T INVEST MORE THAN YOU ARE WILLING TO LOSE. IF YOU LOSE ALL YOUR MONEY EXPECTING TO GET RICH THEN THAT IS YOUR FAULT. I AM NOT RESPONSIBLE FOR THAT HAPPENING.

Anyways, welcome to my pump.fun King of the Hill trading bot. This is a Work in progress bot that will automatically trade a pre-determined amount of solana with the current at that moment King of the hill coin on pump.fun.

Things you will need:
  1. A phantom Wallet
    -You will need the wallet address as well as the private key [NEVER GIVE YOUR PRIVATE KEY TO ANYONE]
  2. The phantom Wallet should be funded by some amount of Solana
  3. An X-RapidAPI-Key from https://rapidapi.com/yllvaranwar/api/pump-fun-king-of-the-hill. This is the API used to get the King of the Hill

Steps to get the program to run:
  1. Download the .env file and fill in the necessary values
    WALLET_ADDRESS=your solana wallet address
    PRIVATE_KEY=your private key
    SLIPPAGE=slippage for trade
    AMOUNT_TO_TRADE=Amount to trade in solana "ex: 0.005"
  2. Download the TradingBot.py
  3. Install any necessary dependencies
  4. Look for this section in the bot
    headers = {
          'x-rapidapi-key': "YOUR API KEY HERE",
          'x-rapidapi-host': "pump-fun-king-of-the-hill.p.rapidapi.com"
    }
  replace the "YOUR API KEY HERE" with the API from https://rapidapi.com/yllvaranwar/api/pump-fun-king-of-the-hill

What will happen when running:
  1. The program will get the current King of the Hill token from pump.fun
  2. It will then swap the predetermined amount in the .env file with that token
  3. The program will wait 30 seconds
  4. The program will swap the desired token back to solana
  5. The program will wait 10 seconds then repeat

LIKE I SAID. THIS IS A WORK IN PROGRESS AND IS NOT GUARENTEED TO MAKE YOU ANY MONEY. PLEASE DO NOT INVEST MORE THAN YOU ARE WILLING TO LOSE!

If this bot does make you money, consider sending a tip my way. My Solana address is 5XGKYheiijRPR9tQCPjiHRwMFqSHhm26VzriHxRESCfn

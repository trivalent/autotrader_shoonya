from autotrader import AutoTrader

at = AutoTrader()
at.configure(verbosity=1, show_plot=True, feed="finvasia")
at.add_strategy("ema_crossover")
at.backtest(start="1/1/2009", end="1/12/2023")
at.virtual_account_config(initial_balance=100000, leverage=1)
at.run()
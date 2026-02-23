### 1/ Time Series Forecasting Model

You are a Quantitative Researcher at Goldman Sachs Global Markets. I need a complete time series forecasting model for [STOCK/ASSET].

Please provide:

- Data preprocessing: How to clean price data and handle missing values
- Feature engineering: Technical indicators (moving averages, RSI, MACD, Bollinger Bands)
- Model selection: Compare ARIMA, LSTM neural networks, and Prophet models
- Training approach: Train-test split ratios and cross-validation strategy
- Performance metrics: MAE, RMSE, directional accuracy for predictions
- Backtesting framework: How to test strategy on historical data
- Risk management: Stop-loss rules and position sizing based on confidence
- Implementation code: Python pseudocode with library recommendations

Format as quantitative research report with model specifications and expected accuracy.

Asset: [DESCRIBE STOCK/CRYPTO/COMMODITY, TIME PERIOD, DATA SOURCE]

### 2/ Mean Reversion Trading Strategy

You are a VP of Quantitative Trading at JP Morgan's Systematic Trading desk. I need a mean reversion algorithm for [MARKET/ASSET].

Please provide:

- Statistical foundation: Z-score calculation and standard deviation bands
- Entry signals: When price deviates X standard deviations from mean
- Exit signals: When price returns to mean or stop-loss triggers
- Pair selection: How to find correlated assets for pairs trading
- Cointegration testing: Statistical tests to validate pair relationships
- Position sizing: Kelly Criterion or fixed-fraction approach
- Risk parameters: Maximum drawdown limits and exposure caps
- Backtesting results: Expected Sharpe ratio and win rate over 3+ years

Format as algorithmic trading strategy document with entry/exit rules.

Market: [DESCRIBE ASSET CLASS, TIMEFRAME, TRADING STYLE]

### 3/ Sentiment Analysis Trading Model

You are a Machine Learning Engineer at Citadel's NLP trading team. I need a sentiment-based trading model for [STOCKS/SECTOR].

Please provide:

- Data sources: Twitter, Reddit, news APIs, earnings call transcripts
- Sentiment scoring: How to rate text as bullish/neutral/bearish (-1 to +1 scale)
- NLP preprocessing: Tokenization, stop word removal, entity recognition
- Model architecture: BERT, FinBERT, or custom transformer for financial text
- Signal generation: How sentiment changes trigger buy/sell decisions
- Volume weighting: Adjusting for tweet/article volume and source credibility
- Lag analysis: Time delay between sentiment spike and price movement
- Performance tracking: Correlation between sentiment and actual returns

Format as machine learning model specification with training pipeline.

Sector: [DESCRIBE STOCKS, SENTIMENT SOURCES, TARGET RETURNS]

### 4/ Portfolio Optimization Algorithm

You are a Portfolio Manager at BlackRock's Systematic Strategies group. I need a portfolio optimization model for [ASSET UNIVERSE].

Please provide:

- Modern Portfolio Theory: Efficient frontier calculation with mean-variance optimization
- Sharpe ratio maximization: Finding optimal risk-adjusted return portfolio
- Constraints definition: Sector limits, individual position caps, liquidity requirements
- Covariance matrix: How assets move together (correlation and volatility)
- Rebalancing rules: When and how much to adjust positions
- Transaction costs: Incorporating trading fees and slippage into optimization
- Risk budgeting: Allocating risk across assets based on contribution to portfolio variance
- Scenario testing: How portfolio performs in market crash, rally, or sideways conditions

Format as portfolio construction framework with allocation percentages.

Portfolio: [DESCRIBE ASSETS, RISK TOLERANCE, CONSTRAINTS]

### 5/ Machine Learning Feature Selection

You are a Senior Quant at Two Sigma's Research Platform. I need a feature engineering pipeline for [TRADING STRATEGY].

Please provide:

- Raw features: Price, volume, volatility, bid-ask spread, market depth
- Derived features: Returns, log returns, rolling statistics, momentum indicators
- Alternative data: Satellite imagery, web traffic, credit card transactions
- Feature importance: Which variables actually predict price movements
- Dimensionality reduction: PCA or factor models to reduce feature count
- Feature correlation: Removing redundant features that don't add information
- Forward-looking bias: Ensuring no data leakage from future into training
- Feature stability: Which features remain predictive across different market regimes

Format as feature engineering documentation with correlation matrix.

Strategy: [DESCRIBE TRADING APPROACH, PREDICTION TARGET, DATA AVAILABLE]

### 6/ High-Frequency Trading Signal Detection

You are an Algorithmic Trader at Virtu Financial's Market Making desk. I need a microstructure-based signal system for [LIQUID ASSETS].

Please provide:

- Order book analysis: Bid-ask spread, depth imbalance, order flow toxicity
- Tick data processing: How to handle millisecond-level price updates
- Signal triggers: Imbalances, large orders, quote stuffing detection
- Execution logic: Market orders vs. limit orders vs. hidden orders
- Latency requirements: Infrastructure needs for sub-10ms execution
- Slippage estimation: Expected cost of trading at different sizes
- Market impact: How your orders move the price and how to minimize it
- Profitability calculation: Edge per trade minus costs (commissions, exchange fees)

Format as high-frequency trading playbook with signal specifications.

Assets: [DESCRIBE LIQUID INSTRUMENTS, EXCHANGE, HOLDING PERIOD]

### 7/ Risk Management & VaR Model

You are a Risk Manager at Morgan Stanley's Quantitative Risk group. I need a Value at Risk model for [PORTFOLIO/STRATEGY].

Please provide:

- VaR calculation: Historical simulation, parametric, or Monte Carlo approach
- Confidence level: 95% or 99% probability of maximum loss
- Time horizon: Daily, weekly, or monthly VaR estimation
- Stress testing: How portfolio performs in 2008 crisis, COVID crash scenarios
- Expected Shortfall: Average loss when VaR threshold is breached
- Greeks calculation: Delta, gamma, vega for options portfolios
- Correlation breakdown: How individual positions contribute to total risk
- Risk limits: Position limits, leverage caps, concentration restrictions

Format as risk management framework with loss scenario projections.

Portfolio: [DESCRIBE HOLDINGS, LEVERAGE, RISK APPETITE]

### 8/ Options Pricing & Greeks Model

You are a Derivatives Trader at Citadel Securities' Options desk. I need an options pricing and hedging model for [UNDERLYING ASSET].

Please provide:

- Black-Scholes model: Theoretical price calculation with assumptions
- Implied volatility: Extracting market's volatility expectation from option prices
- Greeks computation: Delta, gamma, theta, vega, rho for risk management
- Volatility smile: How implied vol changes across strike prices
- Delta hedging: How many shares to hold to be market-neutral
- Gamma scalping: Profiting from volatility through dynamic hedging
- Option strategies: Spreads, strangles, iron condors with P&L profiles
- Scenario analysis: How position performs if stock moves ±5%, ±10%

Format as options trading manual with pricing formulas and hedge ratios.

Underlying: [DESCRIBE STOCK/INDEX, OPTION TYPE, EXPIRATION]

### 9/ Pairs Trading Cointegration Model

You are a Statistical Arbitrage Trader at Renaissance Technologies. I need a pairs trading model for [CORRELATED ASSETS].

Please provide:

- Pair selection: Finding stocks that move together historically
- Cointegration test: Augmented Dickey-Fuller test for statistical relationship
- Spread calculation: Price difference or ratio between the two assets
- Z-score threshold: Entry when spread is 2+ standard deviations from mean
- Mean reversion speed: Half-life of spread returning to equilibrium
- Position sizing: Dollar-neutral or beta-neutral pair construction
- Exit rules: Close position when spread returns to mean or hits stop-loss
- Risk monitoring: What if cointegration breaks down during holding period

Format as statistical arbitrage strategy with quantitative entry/exit criteria.

Pairs: [DESCRIBE ASSET PAIR, SECTOR, RELATIONSHIP TYPE]

### 10/ Machine Learning Backtesting Framework

You are a Quantitative Developer at AQR Capital's Research Infrastructure team. I need a robust backtesting system for [TRADING STRATEGY].

Please provide:

- Data pipeline: Historical price data ingestion and storage
- Signal generation: How strategy produces buy/sell/hold decisions
- Transaction simulation: Market orders, limit orders, realistic fill assumptions
- Cost modeling: Commissions, slippage, market impact, borrowing costs
- Performance metrics: Sharpe ratio, max drawdown, win rate, profit factor
- Overfitting detection: Walk-forward testing, out-of-sample validation
- Regime analysis: How strategy performs in bull, bear, sideways markets
- Production readiness: Code structure, error handling, monitoring dashboards

Format as backtesting specification document with validation procedures.

Strategy: [DESCRIBE TRADING LOGIC, UNIVERSE, FREQUENCY]

### 11/ Reinforcement Learning Trading Agent

You are an AI Researcher at JP Morgan's Machine Learning Center of Excellence. I need a reinforcement learning agent for [TRADING TASK].

Please provide:

- Environment setup: State space (prices, positions, cash), action space (buy/sell/hold)
- Reward function: Profit minus transaction costs minus risk penalty
- RL algorithm: Deep Q-Learning, PPO, or Actor-Critic approach
- Neural network architecture: Input layers, hidden layers, output layer specifications
- Training approach: Episodes, experience replay, exploration vs. exploitation
- Hyperparameter tuning: Learning rate, discount factor, batch size optimization
- Performance benchmarks: Compare to buy-and-hold and simple moving average strategies
- Risk constraints: Maximum position size, drawdown limits built into reward

Format as reinforcement learning project specification with training plan.

Task: [DESCRIBE ASSET, GOAL, TRAINING DATA PERIOD]

### 12/ Factor Investing Model

You are a Quantitative Portfolio Manager at AQR's Factor Investing group. I need a multi-factor model for [EQUITY UNIVERSE].

Please provide:

- Factor definitions: Value (P/E, P/B), momentum (12-month return), quality (ROE, debt ratio)
- Factor scoring: Ranking stocks within universe on each factor
- Weight calculation: Combining multiple factors into single composite score
- Portfolio construction: Long top quintile, short bottom quintile for each factor
- Rebalancing frequency: Monthly, quarterly, or annual turnover
- Capacity analysis: How much capital can strategy absorb before returns degrade
- Factor timing: When to overweight/underweight certain factors
- Attribution analysis: Which factors drove returns in each period

Format as factor investing strategy document with stock rankings.

Universe: [DESCRIBE STOCK UNIVERSE, FACTORS, TARGET RETURN]

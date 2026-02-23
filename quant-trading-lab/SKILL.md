---
name: quant-trading-lab
description: A 12-function meta-skill for quantitative finance and algorithmic trading. Use for time series forecasting, mean reversion, sentiment analysis, portfolio optimization, feature engineering, HFT, risk management (VaR), options pricing, pairs trading, backtesting, reinforcement learning, and factor investing.
---

# Quant Trading Lab

This skill transforms Manus into a quantitative research and trading desk, providing 12 distinct functions that cover the entire lifecycle of algorithmic strategy development. Each function invokes a specific expert persona from a top-tier financial institution (Goldman Sachs, JP Morgan, Citadel, BlackRock, Two Sigma, Virtu, Morgan Stanley, Renaissance Technologies, AQR).

## Core Functions

This skill provides 12 expert-level functions for quantitative finance:

1.  **Time Series Forecasting**: Builds a complete forecasting model (ARIMA, LSTM, Prophet) for a given asset.
2.  **Mean Reversion Strategy**: Designs a mean reversion algorithm with statistical entry/exit rules.
3.  **Sentiment Analysis Model**: Creates a sentiment-based trading model using NLP on news, social media, and transcripts.
4.  **Portfolio Optimization**: Constructs an optimal portfolio using Modern Portfolio Theory and Sharpe Ratio maximization.
5.  **ML Feature Engineering**: Develops a feature engineering pipeline to identify predictive variables for a trading strategy.
6.  **High-Frequency Trading (HFT) System**: Designs a microstructure-based signal system for liquid assets.
7.  **Risk Management & VaR Model**: Builds a Value at Risk (VaR) model with stress testing and expected shortfall analysis.
8.  **Options Pricing & Greeks Model**: Creates an options pricing and hedging model using Black-Scholes and Greeks.
9.  **Pairs Trading Cointegration Model**: Develops a statistical arbitrage pairs trading strategy with cointegration testing.
10. **ML Backtesting Framework**: Designs a robust backtesting system with overfitting detection and cost modeling.
11. **Reinforcement Learning Agent**: Builds a reinforcement learning agent for a specific trading task.
12. **Factor Investing Model**: Creates a multi-factor investing model (Value, Momentum, Quality) for an equity universe.

## How to Use

To use this skill, specify the function you want to perform and provide the required inputs. The skill will automatically adopt the correct persona and execute the request according to the structured template for that function.

### Example Prompts

-   **Time Series Forecasting**: *"Use the quant-trading-lab to build a time series forecasting model for TSLA stock over the last 5 years."*
-   **Mean Reversion**: *"Design a mean reversion strategy for the EUR/USD forex pair on the 1-hour timeframe."*
-   **Sentiment Analysis**: *"Create a sentiment analysis model for the tech sector using Twitter and Reddit data."*
-   **Portfolio Optimization**: *"Optimize a portfolio of 60% stocks, 40% bonds with a moderate risk tolerance."*
-   **Options Pricing**: *"Build an options pricing model for AAPL calls with a 3-month expiration."*

## Reference Files

-   `references/prompt_templates.md`: Contains the full text of all 12 expert prompt templates used by this skill.

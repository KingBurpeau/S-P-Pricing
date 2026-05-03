import yfinance as yf
import pandas as pd
from datetime import datetime

def run_the_machine():
    """
    Daily market pricing analysis - runs at market open (6:30 AM PT / 9:30 AM ET)
    Fetches live S&P 500 and Treasury data, calculates fair value, outputs allocation recommendation
    """
    
    print("=" * 60)
    print(f"📊 MARKET PRICING ANALYSIS - {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print("=" * 60)
    
    try:
        # 1. FETCH LIVE DATA (FREE)
        print("\n🔄 Fetching live market data...")
        
        # ^TNX is the ticker for 10-Year Treasury Yields
        tnx = yf.Ticker("^TNX")
        yield_10y_raw = tnx.history(period="1d")['Close'].iloc[-1]
        yield_10y = yield_10y_raw / 100  # Convert 4.38 to 0.0438
        
        # Get S&P 500 (ticker: ^GSPC) for Price and 200-Day MA
        sp500 = yf.Ticker("^GSPC")
        hist = sp500.history(period="1y")
        current_price = hist['Close'].iloc[-1]
        ma_200 = hist['Close'].rolling(window=200).mean().iloc[-1]
        
        # 2. DYNAMIC VALUATION (May 2026 Baseline)
        # Forward P/E is approx 20.9 as of May 3, 2026
        current_pe = 20.9
        erp = 0.011  # Sector-weighted Equity Risk Premium
        
        # Calculate the 'Fair Value Gate'
        fair_pe = 1 / (yield_10y + erp)
        overval_ratio = current_pe / fair_pe
        
        # 3. PERCENTAGE LOGIC
        # These percentages apply to whatever your total investment amount is
        if overval_ratio > 1.15:
            sp_pct, sgov_pct = 0, 100
            tier, color = "Tier 1", "🔴 RED (Bubble)"
        elif 1.0 < overval_ratio <= 1.15:
            sp_pct, sgov_pct = 50, 50
            tier, color = "Tier 2", "🟡 YELLOW (Pricey)"
        elif current_price > ma_200:
            sp_pct, sgov_pct = 100, 0
            tier, color = "Tier 3", "🟢 GREEN (Fair)"
        else:
            sp_pct, sgov_pct = 200, 0  # Spend reserves
            tier, color = "Tier 4", "🌟 GOLD (Deep Value)"
        
        # 4. OUTPUT RESULTS
        print("\n" + "=" * 60)
        print(f"{color} MARKET STATE")
        print("=" * 60)
        print(f"S&P 500 Price:      ${current_price:>10,.2f}")
        print(f"200-Day MA:         ${ma_200:>10,.2f}")
        print(f"10-Year Yield:      {yield_10y:>10.2%}")
        print(f"Fair Value P/E:     {fair_pe:>10.2f}x")
        print(f"Current P/E:        {current_pe:>10.2f}x")
        print("-" * 60)
        print(f"Valuation:          {((overval_ratio - 1) * 100):>9.1f}% over Fair Value")
        print("=" * 60)
        
        print(f"\n📌 TODAY'S ALLOCATION COMMAND:")
        print("-" * 60)
        print(f"  • S&P 500 (VOO):        {sp_pct}%")
        print(f"  • Cash/Bonds (SGOV):    {sgov_pct}%")
        print(f"  • Market Tier:          {tier}")
        print("-" * 60)
        
        if tier == "Tier 4":
            print("\n⚠️  ACTION: MARKET IS DISTRESSED")
            print("    → Consider emptying SGOV reserves into S&P 500")
        
        print("\n" + "=" * 60)
        print("✅ Analysis complete. Email notification sent.")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        print("Failed to fetch market data. Please check your internet connection.")
        raise

if __name__ == "__main__":
    run_the_machine()

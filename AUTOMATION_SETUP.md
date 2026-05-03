# 🚀 S&P Pricing Automation Setup

## Overview
This automation runs your market pricing analysis **every weekday at 6:30 AM PT** (market open) and sends email notifications to `nathanburpeau@gmail.com`.

**Cost: Completely FREE** ✅

---

## 📋 What's Included

### Files Created:
1. **`run_pricing.py`** - Enhanced pricing analysis script
2. **`.github/workflows/market-open-pricing.yml`** - GitHub Actions workflow
3. **`AUTOMATION_SETUP.md`** - This file

---

## ⚙️ Setup Instructions

### **Step 1: Enable GitHub Actions**

1. Go to your repo Settings: https://github.com/KingBurpeau/S-P-Pricing/settings/actions
2. Under "Actions permissions," select:
   - ✅ **"Allow all actions and reusable workflows"**
3. Click **Save**

### **Step 2: Create GitHub Secrets**

Your email credentials need to be stored securely as GitHub Secrets.

1. Go to: **Settings** → **Secrets and variables** → **Actions**
2. Click **"New repository secret"**
3. Create two secrets:

   **Secret 1:**
   - Name: `EMAIL_USER`
   - Value: `nathanburpeau@gmail.com`
   - Click **Add secret**

   **Secret 2:**
   - Name: `EMAIL_PASSWORD`
   - Value: Your Gmail account password (or app-specific password)
   - Click **Add secret**

> **Note on Gmail Security:** If you have 2FA enabled on your Gmail, use your regular Gmail password. GitHub will handle authentication securely.

### **Step 3: Test the Workflow (Optional)**

1. Go to **Actions** tab in your repo
2. Click **"Market Open Pricing Analysis"** in the left sidebar
3. Click **"Run workflow"** → **"Run workflow"** button
4. Watch it run in real-time!

---

## ⏰ Schedule Details

- **Frequency:** Every weekday (Monday-Friday)
- **Time:** 6:30 AM PT (14:30 UTC / 9:30 AM ET)
- **What runs:** Your `run_pricing.py` script
- **Output:** Results emailed to `nathanburpeau@gmail.com`

### Cron Expression:
```
30 14 * * 1-5
```
- Minute: 30
- Hour: 14 (UTC, which is 6:30 AM PT)
- Day: * (every day)
- Month: * (every month)
- Day of Week: 1-5 (Monday-Friday)

---

## 📊 What You'll Receive

Each email contains:
- ✅ Current S&P 500 price & 200-day moving average
- ✅ 10-year Treasury yield
- ✅ Fair value P/E calculation
- ✅ Market valuation assessment (% over/under fair value)
- ✅ **Your allocation recommendation:**
  - % to invest in S&P 500 (VOO)
  - % to hold in Cash/Bonds (SGOV)
- ✅ Market tier status (🟢 Green, 🟡 Yellow, 🔴 Red, 🌟 Gold)
- ✅ Link to full results in GitHub Actions

---

## 🔧 Manual Testing

To run the analysis manually anytime:

```bash
python run_pricing.py
```

This will output the full analysis to your terminal.

---

## 📝 How It Works

### Workflow Steps:
1. **Checkout** - Pulls the latest code from your repo
2. **Python Setup** - Installs Python 3.11
3. **Dependencies** - Installs `yfinance` and `pandas`
4. **Analysis** - Runs your pricing script
5. **Results** - Saves output as an artifact (30-day retention)
6. **Notification** - Sends email with results link

### Data Sources (All Free):
- **S&P 500 Data:** Yahoo Finance API (via yfinance)
- **Treasury Yields:** Yahoo Finance API (via yfinance)
- **Computation:** GitHub Actions (free tier)

---

## 🆘 Troubleshooting

### "Workflow didn't send email"
- Check that GitHub Actions is enabled in Settings
- Verify both secrets (`EMAIL_USER` and `EMAIL_PASSWORD`) are created
- Check the Actions tab for error logs

### "yfinance not found"
- This is automatically installed by the workflow - no action needed

### "Can't find Actions tab"
- Your repo needs to have GitHub Actions enabled (done in Step 1)

### "Workflow shows as disabled"
- Go to Settings → Actions and re-enable workflows

---

## 📧 Email Customization

To change:
- **Email recipient:** Edit `.github/workflows/market-open-pricing.yml` line with `to:`
- **Email subject:** Edit the `subject:` line in the workflow
- **Run time:** Edit the `cron:` schedule in the workflow

---

## 💰 Cost Analysis

**Total Cost: $0** ✅

- GitHub Actions: Free tier (up to 2,000 minutes/month)
- This workflow: ~30 seconds per run = ~4 minutes/month
- Email: GitHub-native notifications (free)
- Data: Yahoo Finance API (free)

---

## 🎯 Next Steps

1. ✅ Enable GitHub Actions (Step 1)
2. ✅ Add email secrets (Step 2)
3. ✅ Test manually in Actions tab (Step 3, optional)
4. ✅ **You're done!** Automation starts tomorrow at 6:30 AM PT

---

## 📚 Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [yfinance GitHub](https://github.com/ranaroussi/yfinance)
- [GitHub Secrets Documentation](https://docs.github.com/en/actions/security-guides/encrypted-secrets)

---

**Questions?** Check the workflow file or GitHub Actions logs for detailed error messages.

Happy automating! 🚀

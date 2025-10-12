# Configuration settings
import os
from pathlib import Path

class Config:
    """Application configuration"""
    
    # Paths
    BASE_DIR = Path(__file__).parent
    DATA_DIR = BASE_DIR / "data"
    ASSETS_DIR = BASE_DIR / "assets"
    
    # Data files
    DATA_FILE = DATA_DIR / "Ecommerce Customers.csv"
    
    # Model settings
    TEST_SIZE = 0.3
    RANDOM_STATE = 42
    CV_FOLDS = 5
    
    # App settings
    PAGE_TITLE = "E-commerce Customer Analysis"
    PAGE_ICON = "🛒"
    LAYOUT = "wide"
    
    # Feature columns
    NUMERICAL_FEATURES = [
        'Avg. Session Length', 
        'Time on App', 
        'Time on Website', 
        'Length of Membership'
    ]
    TARGET_FEATURE = 'Yearly Amount Spent'
    
    # Model parameters
    DEFAULT_ALPHA = 1.0
    ALPHA_RANGE = (0.1, 10.0)
    
    # Visualization settings
    COLOR_PALETTE = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    PLOT_THEME = "plotly_white"
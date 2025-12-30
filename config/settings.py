import os
from dataclasses import dataclass

@dataclass
class Settings:
    """Application settings loaded from environment or defaults."""
    
    base_url: str = "https://www.saucedemo.com"
    timeout: int = 30000  # milliseconds
    slow_mo: int = 0  # milliseconds between actions
    headless: bool = False
    browser: str = "chromium"  # chromium, firefox, webkit
    
    # Test user credentials
    standard_user: str = "standard_user"
    locked_out_user: str = "locked_out_user"
    problem_user: str = "problem_user"
    performance_glitch_user: str = "performance_glitch_user"
    default_password: str = "secret_sauce"
    
    @classmethod
    def from_env(cls) -> "Settings":
        """Load settings with environment variable overrides."""
        return cls(
            base_url=os.getenv("BASE_URL", cls.base_url),
            timeout=int(os.getenv("TIMEOUT", cls.timeout)),
            slow_mo=int(os.getenv("SLOW_MO", cls.slow_mo)),
            headless=os.getenv("HEADLESS", "false").lower() == "true",
            browser=os.getenv("BROWSER", cls.browser),
        )


# Global settings instance
settings = Settings.from_env()
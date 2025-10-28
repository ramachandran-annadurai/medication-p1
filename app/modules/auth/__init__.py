"""
Authentication module
Handles user signup, login, OTP verification, password reset, and profile management
"""

from .routes import auth_bp

__all__ = ['auth_bp']


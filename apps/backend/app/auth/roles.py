from typing import List

from fastapi import Depends, HTTPException, status

from app.auth.dependencies import get_current_user
from app.models.user import User


class RoleChecker:
    """
    Checks whether the authenticated user has one of the allowed roles.
    """

    def __init__(self, allowed_roles: List[str]):
        self.allowed_roles = allowed_roles

    def __call__(
        self,
        current_user: User = Depends(get_current_user),
    ) -> User:

        if current_user.role not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to perform this action."
            )

        return current_user


# ==========================================================
# Predefined Role Dependencies
# ==========================================================

allow_admin = RoleChecker(
    ["ADMIN"]
)

allow_manager = RoleChecker(
    ["ADMIN", "MANAGER"]
)

allow_user = RoleChecker(
    ["ADMIN", "MANAGER", "USER"]
)
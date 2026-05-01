"""Admin boundary policy.

Security must be enforced server-side. UI hiding is never authorization.
"""

from __future__ import annotations


class AdminAccessDeniedError(Exception):
    """Raised when a non-admin attempts an admin-only action."""


def require_admin(*, is_admin: bool) -> None:
    if not is_admin:
        raise AdminAccessDeniedError("admin access required")


def admin_boundary_state(*, is_admin: bool) -> dict[str, bool | str]:
    return {
        "is_admin": is_admin,
        "admin_access": is_admin,
        "enforced_by": "server_policy",
    }
